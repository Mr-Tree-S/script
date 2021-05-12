#!/bin/bash

echo_G(){
	echo -e "\033[32m $1 \033[0m"
}
echo_R(){
	echo -e "\033[31m $1 \033[0m"
}

a=(0 1 3 8)
for i in ${a[@]};do
	expr $i % 2 &> /dev/null
	if [ $? = 1 ];then
		echo_G "$i##OK"
	else
		echo_R "$i##NOT"
	fi
done
