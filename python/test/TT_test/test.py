# coding=gbk
import json
import re

FileName = ""
ethernet = []
hw_id = []

with open('config.boot', 'r') as config:
    for line in config:
        #print(line)
        if(re.match('^[a-zA-Z].*', line)):
            FileName = re.match('^[a-zA-Z].*|^}', line).group().split()[0]
            print(FileName)
        elif(re.search('.*{', line)):
            key = re.search('.*{', line).group().split()[1]
            print(key)
            ethernet.append(key)
            if(key == "lo"):
                ethernet.pop()
        elif (re.search('.*}', line)):
            continue
        else:
            val = line.split()[1]
            print(val)
            hw_id.append(val)

result = []
for i in range(len(ethernet)):
    dic = {'ethernet':ethernet[i],'hw_id':hw_id[i]}
    result.append(dic)

print("###"+FileName+"###")
newFile = FileName
with open(newFile, 'w') as name:
    for i in range(len(result)):
        jsonData = json.dumps(result[i])
        name.write(jsonData+','+'\n')

