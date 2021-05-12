#!/bin/bash

echo_G(){
	echo -e "\033[32m $1 \033[0m"
}
echo_R(){
	echo -e "\033[31m $1 \033[0m"
}


for i in `cat ~/Desktop/ip.txt`;do
	ping -c 2 $i &> /dev/null
	if [ $? = 0 ];then
		echo_G "$i##OK"
	else
		echo_R "$i##NOT"
	fi
done
