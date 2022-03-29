#!/bin/sh


<< part1
一、系统配置部分（注意执行过成功输出友好信息，例如开始配置IP地址，开始关闭selinux）
1.设置系统IP地址为192.168.3.100，子网掩码255.255.255.0，网关192.168.3.1，首选DNS为202.106.0.20，备用DNS设置为114.114.114.114。并且使配置生效。
2.修改配置文件永久禁用selinux，且使用命令设置当前selinux为宽容模式enforce为0。清空iptables，关闭firewalld禁用firewalld。
3.生成本地repo文件，将系统安装光盘设置为本地YUM源。
4.使用yum安装vsftpd与httpd服务，并且启动vsftpd与httpd服务，后将systemctl  status  vsftpd与httpd的内容重定向到/root/services.txt文件中。
5. 配置服务器的rsyslog服务，将公共消息日志和认证日志保存通过UDP协议传输到日志收集服务器192.168.3.1中。
part1


info(){
        echo "$1" >> /root/sysinfo
}
sec(){
        echo -e "\033[31m $1 \033[0m"
}

a1=`ifconfig | head -1 |awk -F: '{print $1}'`
p1="/etc/sysconfig/network-scripts/ifcfg-$a1"
# 1
a1=`ifconfig | head -1 |awk -F: '{print $1}'`
p1="/etc/sysconfig/network-scripts/ifcfg-$a1"
echo "start change IP NETMASK DNS1 DNS2"
sed -i 's/dhcp/static/g' $p1
sed -i '/IPADDR/d' $p1
sed -i "$ a IPADDR=192.168.3.100" $p1
sed -i '/NETMASK/d' $p1
sed -i "$ a NETMASK=255.255.255.0" $p1
sed -i '/BROADCAST/d' $p1
sed -i "$ a BROADCAST=192.168.3.1" $p1
sed -i '/DNS/d' $p1
sed -i "$ a DNS1=202.106.0.20" $p1
sed -i "$ a DNS2=114.114.114.114" $p1
systemctl restart network.service
echo "change finish"

# 2
p2="/etc/sysconfig/selinux"
sed -i 's/SELINUX=enforcing/SELINUX=disable/g' $p2
echo "stop selinux"
setenforce 0
echo "clean iptables"
iptables -F
echo "stop firewalld"
systemctl stop firewalld
systemctl disable firewalld

# 3

# 4
echo "yum vsftpd"
yum install -y vsftpd &> /dev/null
echo "yum httpd"
yum install -y httpd &> /dev/null
echo "start vsftpd"
systemctl start vsftpd
systemctl status vsftpd > /root/services.txt
echo "start httpd"
systemctl start httpd
systemctl status httpd >> /root/services.txt

# 5
p5="/etc/rsyslog.conf"
sed -i 's/#$ModLoad imudp/$ModLoad imudp/g' $p5
sed -i 's/#$UDPServerRun 514/$UDPServerRun 514/g' $p5
sed -i "$ a *.* @192.168.3.1:514" $p5
echo "start rsyslog"
systemctl start rsyslog


<< part2
二、基本信息采集部分（注意保存的信息优化输出显示，并且信息之间加入明显的“分割符”，保存到/root/sysinfo）（20分）
sysinfo文件格式例如：
操作系统版本为：xxxxxxx
-------------------------
ip地址为：
子网掩码为：
默认网关为：
首选DNS为：
-------------------------

6.采集系统版本信息，追加到/root/sysinfo文件中
7.采集系统IP地址，子网掩码，默认网关，首选DNS，追加到/root/sysinfo文件中
8.采集系统硬盘信息，磁盘分区，挂载点，分区使用量等，追加到/root/sysinfo文件中
9.采集系统内存信息，最大内存，已用内存，剩余内存等，追加到/root/sysinfo文件中
10.采集系统当前开放的“端口号”和所对应的“程序名称”，追加到/root/sysinfo文件中
part2


echo "##开始基本信息采集##"
# 6 7 8 9 10
p6="/root/sysinfo"
a6=`cat /etc/redhat-release`
echo "操作系统版本为：$a6" > $p6
echo "-------------------------" >> $p6
b6=`grep "IPADDR" $p1 | awk -F= '{print $2}'`
echo "ip地址为：$b6" >> $p6
c6=`grep "NETMASK" $p1 | awk -F= '{print $2}'`
echo "子网掩码为：$c6" >> $p6
d6=`grep "BROADCAST" $p1 | awk -F= '{print $2}'`
echo "默认网关为：$d6" >> $p6
e6=`grep "DNS1" $p1 | awk -F= '{print $2}'`
echo "首选DNS为：$e6" >> $p6
echo "-------------------------" >> $p6
echo "系统硬盘信息：" >> $p6
lsblk >> $p6
echo "-------------------------" >> $p6
echo "磁盘分区：" >> $p6
fdisk -l >> $p6
echo "-------------------------" >> $p6
echo "挂载点/分区使用量：" >> $p6
df -h >> $p6
echo "-------------------------" >> $p6
echo "内存信息：" >> $p6
free -h >> $p6
echo "-------------------------" >> $p6
echo "端口及服务：" >> $p6
netstat -nlptu >> $p6
echo "##基本信息采集结束##"


<< part3
三、基线检查部分（注意保存的信息优化输出显示，并且信息之间加入分割字段，保存到/root/ security）（40分）
security文件格式例如：
**********开始检查是否存在克隆root账户***********
检查通过，未发现克隆root账户。
**********开始检查密码最长使用期限***********
检查未通过，密码最长使用期限不合规

11.检查判断是否存在root以外UID为0的账户。
12.检查判断密码最长使用期限是否大于90天超过90天为不合格。
13.检查判断是否删除了系统登录banner信息。
14.检查判断是否响应ICMP协议请求。
15.检查判断sshd服务是否更换默认连接端口。如未加固，使用脚本加固，并且在security文件中保存加固完成以及加固配置项。例如：某某某配置已加固，加固内容为XXXXX改为2020。
16.检查判断sshd服务是否禁止root远程登录系统。如未加固，使用脚本加固，并且在security文件中保存加固完成以及加固配置项。例如：某某某配置已加固，加固内容为XXXXX 改为no。
17.检查判断apache服务是否存在浏览器遍历目录的配置。
18.检查apache是否启用了404错误页面重定向。
19.检查apache服务是否关闭了版本信息。如未加固，使用脚本加固，并且在security文件中保存加固完成以及加固配置项。例如：某某某配置已加固，加固内容为XXXXX改为yes 。
20.检查/var/log/messages文件的底层属性是否有加固a属性存在。如未加固，使用脚本加固，并且在security文件中保存加固完成以及加固配置项。例如：某某某配置已加固。加固内容为------a-----   /var/log/messages
part3


echo "##开始基线检查##"
# 11
cat /etc/passwd | awk -F: '($3 == 0) { print $1 }'|grep -v '^root$'
if [ $? = 0 ];then
	echo "存在root以外UID为0的账户" >> /root/security
else
	echo "不存在root以外UID为0的账户" >> /root/security
 
fi
# 12
p12="/etc/login.defs"
a12=`cat $p12 | grep ^"PASS_MAX_DAYS"`
b12=`echo $a12 | awk '{print $2}'`
if [ $b12 -gt 90 ];then
	echo "密码最长使用期限大于90不合格，已加固" >> /root/security
 
        sed -i "s/$a12/PASS_MAX_DAYS   90/g" $p12
else
	echo "密码最长使用期限小于90合格" >> /root/security
 
fi
# 13

# 14
a14=`cat /proc/sys/net/ipv4/icmp_echo_ignore_all`
if [ $a14 = 0 ];then
	echo "响应ICMP请求" >> /root/security
 
else
	echo "不响应ICMP请求" >> /root/security
 
fi
# 15
grep -Fx "Port 22" /etc/ssh/sshd_config
if [ $? = 0 ];then
	sed -i "s/Port 22/Port 2020/g" /etc/ssh/sshd_config
	echo "sshd Port 已加固为2020" >> /root/security
 
else
	echo "sshd Port 无需加固" >> /root/security
	
fi
# 16
grep  -Fx "PermitRootLogin yes" /etc/ssh/sshd_config
if [ $? = 0 ];then
	sed -i "s/PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
	echo "sshd 禁止root远程登陆 已加固" >> /root/security
 
else
	echo "sshd root远程登陆 无需加固" >> /root/security
 
fi
# 17
grep   "Options Indexes" /etc/httpd/conf/httpd.conf
if [ $? = 0 ];then
	sed -i "s/Options Indexes /Options /g" /etc/httpd/conf/httpd.conf
	echo "apache服务存在目录遍历 已加固" >> /root/security
 
else
	echo "apache服务不存在目录遍历" >> /root/security
 
fi
# 18

# 19

# 20

echo "##基线检查结束##"
