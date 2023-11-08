from threading import *
from time import sleep
# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
# t1=hi()
# t2=hello()
# t1.start()
# sleep(0.2)
# t2.start()
# print(t1.daemon)
# # t1.join()
# # t2.join()
# print("Bye")

def exam():
    for i in range (20):
        print("Teaching session",i)
        sleep(0.7)

t1=Thread(target=exam)

t1.daemon=True
t1.start()
sleep(3)
print("Exam time \n Exam over")