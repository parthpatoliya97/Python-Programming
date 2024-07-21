import time
# time method to count the time reqired to execute 
# def usingwhile():
#     i=0
#     while i<50:
#         i=i+1
#         print(i)
# def usingfor():
#     for i in range(50):
#         print(i)
# init=time.time()
# usingfor()
# print(time.time()-init)
# init=time.time()
# usingwhile()
# print(time.time()-init)

# sleep method
# print(4)
# time.sleep(4)
# print("this is printed after 3 seconds")
import time
t=time.localtime()
formate_time=time.strftime("%Y-%m-%d-%H:%M:%s",t)
print(formate_time)