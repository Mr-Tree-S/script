#!/bin/sh


# 1.采集系统版本信息，追加到/root/sysinfo文件中
lsb_release -a >> /root/sysinfo
# 2.永久关闭selinux。
p2="/etc/selinux/config"
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" $p2
# 3.检查是否禁用root账户使用ssh登录系统，如存在隐患，则加固。
p3="/etc/ssh/sshd_config"
sed -i "/PermitRootLogin/d" $p3
echo "PermitRootLogin no" >> $p3
# 4.检查判断是否启用了sshd服务版本2，如存在隐患，则加固。
p4="/etc/ssh/sshd_config"
v4=`grep "Protocol" $p4
if [ $? = 1 ];then
	echo "Protocol 2" >> $p4
else
	sed -i "s/$v4/Protocol 2/g" $p4
fi
# 5.检查判断apache服务是否存在浏览器遍历目录的配置，如存在隐患，则加固。
p5="/etc/httpd/conf/httpd.conf"
sed -i "s/Options Indexes FollowSymLinks/Options FollowSymLinks/g" $p5
# 6.检查判断是否存在root以外UID为0的账户，如存在隐患，则加固。
cat /etc/passwd | awk -F: '{print $1 $3}' | grep "0"$ | grep -Fxv "root0" | awk -F0 '{print $(NF-1)}' | xargs -I {} userdel -r {}
# 7.检查/var/log/messages文件的底层属性是否有加固a属性存在，如存在隐患，则加固。
lsattr /var/log/messages | grep "\-a\-"
if [ $? = 0];then
	chattr +a /var/log/messages
fi
# 8.检查判断密码最长使用期限是否大于90天超过90天为不合格，如存在隐患，则加固。
p8="/etc/login.defs"
v8=`cat $p8 | grep ^"PASS_MAX_DAYS"`
v8_1=`cat $v8 | awk '{print $2}'`
if [ $v8_1 -gt 90];then
	sed -i "s/$v8/PASS_MAX_DAYS   90/g" $p8
fi
# 9.检查nginx是否关闭了头部版本信息，如存在隐患，则加固。
p9="/etc/nginx/nginx.conf"
sed -i "/^http/a\server_tokens off" $p9
