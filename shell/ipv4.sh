#!/bin/bash


echo_G(){
	echo -e "\033[32m $1 \033[0m"
}
echo_R(){
	echo -e "\033[31m $1 \033[0m"
}

#grep -P ^'(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))' $1


read -p "请输入ip地址：" ip
echo $ip | grep -P ^'(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))'
if [ $? = 0 ];then
	d1=`echo $ip|awk -F. '{print $1}'`
	d2=`echo $ip|awk -F. '{print $2}'`
	d3=`echo $ip|awk -F. '{print $3}'`
	d4=`echo $ip|awk -F. '{print $4}'`
	if [ $d1 -eq 127 ];then
		echo "不可设置回环地址"
	elif [ $d1 -eq 255 ] && [ $d2 -eq 255 ] && [ $d3 -eq 255 ] && [ $d4 -eq 255 ];then
		echo "不可设置广播地址"
	elif [ $d1 -eq 0 ] && [ $d2 -eq 0 ] && [ $d3 -eq 0 ] && [ $d4 -eq 0 ];then
		echo "不可设置全0"
	elif [ $d1 -lt 128 ];then
		if [ $d2 -eq 255 ] && [ $d3 -eq 255 ] && [ $d4 -eq 255 ];then
			echo "不可设置广播地址"
		elif [ $d2 -eq 0 ] && [ $d3 -eq 0 ] && [ $d4 -eq 0 ];then
			echo "不可主机位不可设置全0"
		else
		mask=255.0.0.0
		echo "A类地址，掩码为$mask"
		fi
	elif [ $d1 -lt 192 ];then
		if [ $d3 -eq 255 ] && [ $d4 -eq 255 ];then
			echo "不可设置广播地址"
		elif [ $d3 -eq 0 ] && [ $d4 -eq 0 ];then
			echo "不可主机位不可设置全0"
		else
		mask=255.255.0.0
		echo "B类地址，掩码为$mask"
		fi
	elif [ $d1 -lt 224 ];then
		if [ $d4 -eq 255 ];then
			echo "不可设置广播地址"
		elif [ $d4 -eq 0 ];then
			echo "不可主机位不可设置全0"
		else
		mask=255.255.255.0
		echo "C类地址，掩码为$mask"
		fi
	elif [ $d1 -ge 224 ];then
		echo "请输入小于223.255.255.254的IP地址"
	fi
else
	echo "fail"
	exit 1
fi

P=/etc/sysconfig/network-scripts/ifcfg-eno16777736
sed -i 's/dhcp/static/g' $p
sed -i 'IPADDR/d' $p
sed -i "$ a IPADDR=$ip" $P
sed -i 'NETMASK/d' $p
sed -i "$ a NETMASK=$mask" $P

service network restart
if [[ $? -eq 0 ]];then
	echo "network service restart success"
	ifconfig		
else 
	echo "network service restart fail"
	exit 1
fi
