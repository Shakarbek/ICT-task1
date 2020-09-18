# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 1
# print('Assel');
#
# # 2
# name = input("Your name: ", )
# print("Hello,", name)

# 3
# width=float(input(f"Enter the width: ", ))
# length= float(input("Enter the length: ",))
# area=width*length
# print(area, "meters")

# 4
# width=float(input(f"Enter the width in feet: ", ))
# length= float(input("Enter the length in feet: ",))
# area=width*length/43560
# print(area, "acres")

# 5
# small= int(input("Enter the number of small containers: "))
# large= int(input("Enter the number of large containers: "))
# refund= small*0.10+0.25*large
# print("Refund is $"+"{0:.2f}".format(refund))

# 6
# cost=float(input("Enter cost of meal:"))
# tax= 0.10*cost
# tip=0.18*cost
# grand_total=cost+tax+tip
# print("Tax:"+"{0:.2f}".format(tax)+"\n"+"Tip:"+"{0:.2f}".format(tip)+"\n"+"Grand total:"+"{0:.2f}".format(grand_total))

# 7
# n= int(input())
# sum=n*(n+1)/2
# print(sum)

# 8
# widgets=int(input("Widgets:"))
# gizmos=int(input("Gizmos:"))
# total_weight=widgets*75+gizmos*112
# print(total_weight, "grams")

# 9
# money= int(input())
# first= money*1.04
# second=first*1.04
# third=second*1.04
# print(round(first, 2), round(second, 2), round(third, 2))

# 10
# import math
# a= int(input())
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(math.log10(a))

# 11
# US=int(input())
# Canada=US*2.35
# print(Canada)

# 12
# import math
# t1= math.radians(input())
# g1= math.radians(input())
# t2= math.radians(input())
# g2= math.radians(input())
# distance= 6371.01*math.arccos (math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
# print(distance)

# 13 p-1 n-5 d-10 q-25 l-60(1$) t-2$(не поняла условие)
# cash=int(input())
# b_cash=int(input())
# a_cash=cash-b_cash
# if a_cash//200>0:
#     print(a_cash//200, "toonies")
#     a_cash=a_cash%200
#     if a_cash//100>0:
#         print(a_cash//100, "loonies")
#         a_cash=a_cash%100
#     elif a_cash//25>0:
#         print(a_cash//25, "quarters")
#         a_cash=a_cash%25
#     elif a_cash//10>0:
#         print(a_cash//10, "dimes")
#         a_cash=a_cash%10
#     elif a_cash//5>0:
#         print(a_cash//5, "nickels")
#         a_cash=a_cash%5
#     elif a_cash//1>0:
#         print(a_cash//1, "pennies")
#         a_cash=a_cash%1

# 14
# foot=int(input())
# inches=int(input())
# cm=foot*12*2.54+inches*2.54
# print(cm)

# 15
# foot=int(input())
# print(12*foot, "inches")
# print(foot/3, "yards")
# print(foot/5280, "miles")

# 16
# import math
# r=int(input())
# area= math.pi*r*r
# volume= 4*math.pi*math.pow(r,3)/3
# print(area)
# print(volume)

# 17
# import math
# m=int(input())
# t=int(input())
# q=4.186*m*t
# print(q)
# cash= q*2.77*math.pow(10, -7)*8.9
# print(cash)

# 18
# import math
# r=int(input())
# h=int(input())
# volume=math.pi*r*r*h
# print("{0:.1f}".format(volume))

# 19
# import math
# d=int(input())
# u=math.sqrt(2*9.8*d)
# print(u)

# 20
# P=int(input())
# V=int(input())
# T1=input()
# T2=input()
# temp1=int(T1[:-1])
# temp2=int(T2[:-1])
# scale1=T1[-1]
# scale2=T2[-1]
# R=8.314
# if scale1.upper()=="C":
#     result=273.15+temp1
# elif scale1.upper()=="F":
#     result=(temp1-32)*5/9+273.15
# elif scale2.upper()=="C":
#     result2=273.15+temp2
# elif scale2.upper()=="F":
#     result2=(temp2-32)*5/9+273.15
# n=P*V/(R*(result2-result))
# print(n)

# 21
# b=int(input())
# h=int(input())
# area= b*h/2
# print(area)

# 22
# import math
# s1= int(input())
# s2= int(input())
# s3= int(input())
# s=(s1+s2+s3)/2
# area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
# print(area)


# 23
# import math
# s=int(input())
# n=int(input())
# area=n*s*s/(4*math.tan(math.pi/n))
# print(area)

# 24
# days=int(input())
# hours= int(input())
# minutes=int(input())
# seconds=int(input())
# sec=days*24*60*60+hours*60*60+minutes*60+seconds
# print(sec)

# 25
# import time
# time1= int(input())
# d=time1//(86400)
# time1=time1%86400
# time_res = time.gmtime(time1)
# res = time.strftime("%H:%M:%S", time_res)
# if d<10:
#     day_res="0"+str(d)+":"
# elif d>=10:
#     day_res=str(d)+":"
# print(day_res+res)
#

# 26
# import time
# t = time.localtime()
# print ("%s " % time.asctime(t))

# 27
# h=int(input())
# h_s=input()
# w=int(input())
# w_s=input()
# if h_s=="inches" and w_s=="pounds":
#     BMI=w*703/(h*h)
# elif h_s=="meters" and w_s=="kilograms":
#     BMI=w/(h*h)
# print(BMI)

# 28
# T=float(input())
# V=float(input())
# if T<=10 and V>=4.8:
#     WCI = 13.12+0.6215*T-11.37*V*0.16+0.3965*T*V*0.16
#     print(round(WCI))
# else:
#     print("ERROR")

# 29
# C = float(input("Enter temperature in celsius: "))
# F = (C * 9/5) + 32
# K=C+273.15
# print(F, "Fahrenheit, ", K, "Kelvin")

# 30
# kpa = float(input("Input pressure in in kilopascals> "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: ",psi)
# print("The pressure in millimeter of mercury: " ,mmhg)
# print("Atmosphere pressure:" ,atm)

# 31
# n= int(input("Input a four digit numbers: "))
# sum=int(n%10+((n%100-n%10)/10)+n//1000+(n-(n//1000)*1000)//100)
# print("The sum of digits in the number is", sum)

# 32
# arr = []
# for i in range(3):
#     x=int(input())
#     arr.append(x)
# x_max=max(arr)
# x_min=min(arr)
# sum=0
# for i in range(3):
#     sum+=arr[i]
# mid=sum-x_max-x_min
# arr2=[x_min, mid, x_max]
# print(arr2)

# # 33
n= int(input())
cost=3.49
sale=3.49*0.6
total_cost=3.49*0.4*n
numbers = [cost, sale, total_cost]
for number in numbers:
    print(f'{number:9.2f}')