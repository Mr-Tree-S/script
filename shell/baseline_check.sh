#!/bin/sh

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
