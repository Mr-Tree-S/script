import time
time_s=13302926676614765/1000000-11644473600
time_e=13302931775387901/1000000-11644473600
print(time_s)
print(time.strftime("%Y-%m-%d-%H:%M:%S %x",time.gmtime(time_s)))

print(time_e)
print(time.strftime("%Y-%m-%d-%H:%M:%S %x",time.gmtime(time_e)))
