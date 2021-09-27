import hashlib


def md5(n):
    return hashlib.md5(str(n).encode('utf-8')).hexdigest()

# print(md5(123))
for i in range(1,999):
    # print(i)
    # print(md5(i))
    if md5(i).startswith('202cb9'):
        print(i)


n123='202cb962ac59075b964b07152d234b70'
