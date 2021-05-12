#!/bin/sh


if [ $1 = "clean" ];then
	rm ./*.gz
else
	T=`date "+%F_%T"`
	tar -zcf /root/Desktop/"$T"bak.tar.gz $*
fi

