import time

print(time.time())

print("Hello Time Module")

time.sleep(5)
print("This is printed after 5 seconds of delay !!!")

localtime = time.localtime()
formatedTime = time.strftime("%y-%m-%d %H:%M:%S",localtime)
print(formatedTime)