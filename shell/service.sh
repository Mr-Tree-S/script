#!/bin/sh

echo_G(){
	echo  "\033[32m $1 \033[0m"
}
echo_R(){
	echo  "\033[31m $1 \033[0m"
}

a=`netstat -anpt | grep "::$1" | awk '{print $6}'`
service=`cat /etc/services | grep -w "$1" | awk '{print $1}'`

if [ $a ];then
	if [ $a = LISTEN ];then
		echo_G LISTEN
	elif [ $a = ESTABLISHED ];then
		echo_G ESTABLISHED
	fi
else
	echo_R Opposss!!!
	systemctl start $service
fi
