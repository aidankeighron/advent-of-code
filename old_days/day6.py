from util import init, load_day, load_file, result
import math
init()

# array = load_day(6)
# total = 1
# part_2 = False

# # Time:        44     70     70     80
# # Distance:   283   1134   1134   1491
time1 = 44707080
distance1 = 283113411341491


# print(part2)
#            10399622441600
# i*(44707080-i) 
a = 0
print(sum(1 for i in range(1, time1) if (i*(time1-i) > distance1)))
for i in range(1, time1):
    #     print(f'{i}/{int(3.7*10**7- 7.5*10**6)}')
#     speed = i
#     time = time1-i
    # print(i*(time1-i))
    if i*(time1-i) > distance1:
        a+=1
print(a)
# for i in range(int(7500000), int(37000000)):
#     print(f'{i}/{int(3.7*10**7- 7.5*10**6)}')
#     speed = i
#     time = time1-i
#     print(i*(time1-i))
#     if speed*time > distance1:
#         a+=1
# total*=a
# print(a)
# time1 = 70
# distance1 = 1134
# d= []
# a=0
# for i in range(time1):
#     speed = i
#     time = time1-i
#     d.append(speed*time)
# for i in d:
#     if i > distance1:
#         a+=1
# total*=a
# # print(a)
# # time1 = 70
# # distance1 = 1134
# # d= []
# # a=0
# # for i in range(time1):
# #     speed = i
# #     time = time1-i
# #     d.append(speed*time)
# # for i in d:
# #     if i > distance1:
# #         a+=1
# # total*=a
# # print(a)
# # time1 = 80
# # distance1 = 1491
# # d= []
# # a=0
# # for i in range(time1):
# #     speed = i
# #     time = time1-i
# #     d.append(speed*time)
# # for i in d:
# #     if i > distance1:
# #         a+=1
# # total*=a
# # print(a)
    


# result(total)