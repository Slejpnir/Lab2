import random
from collections import OrderedDict
def task1():
    a=[1,4,9,16,25,36,49,64,81,100]
    b=filter(lambda x:x % 2 ==0,a)
    for i in b:
        print(i)
def task2():
    n1=random.randint(1,10)
    n2=random.randint(1,10)
    a=[]
    b=[]
    for i in range(n1):
        a.append(random.randint(1,6))
    for i in range(n2):
        b.append(random.randint(1,6))
    a=set(a)
    b=set(b)
    c=list(a & b)
    print(a,sep=" ")
    print(b,sep=" ")
    print(c,sep=" ")
def check_number(in_number):
    #print(in_number)
    if in_number.isdigit():
        if int(in_number)>=1:
            return True
        else:
            return False
    else:
        return False

def ask_for_number(in_arg,test):
    while True:
        if test==False:
            number=input("Введите целое число больше 0: ")
        else:
            number=in_arg
        if check_number(number):
            number=int(number)
            break
        else:
            print("Введенное число неккоректно")
            if test==True:
                return False
            else:
                continue
    return number
def fib(n):
    l=[]
    a,b = 1,1
    l+=[a]
    while b<=n:
        l+=[b]
        a,b=b,a+b
    return l 

def task3(in_arg,test):
    number=ask_for_number(in_arg,test)
    if number!=False:
        print(fib(number))

def od(lst):
    d = OrderedDict.fromkeys(lst,None)
    return list(d.keys())

def str_rev(str):
    return " ".join(str.split()[::-1])

def task5():
    str=input("Введите строку: ")
    print(str_rev(str))

task=1
while task!=0:
    task=input("Номер задания (0-выход): ")
    if task=="1":
        task1()
    if task=="2":
        task2()
    if task=="3":
        if __name__ == "__main__":
            test_strings=["ABCD","0.8","-5","1","15"]
            for i in range(len(test_strings)):
                print("Тест №%s"%i)
                print("Вводимая строка: %s"%test_strings[i])
                task3(test_strings[i],True)
        else:
            task3(0,False)
    if task=="4":
        if __name__ == "__main__":
            test_strings=[[1, 6, 8, 9,6, -5,-5-5,12],["a","b","a","abc","ab"],[0.9,-0.67,0.98,0.67,-0.67],[True,True,False,True,False]]
            for i in range(len(test_strings)):
                print("Тест №%s"%i)
                print("Исходный список: %s"%test_strings[i])
                print(od(test_strings[i]))
    if task=="5":
        if __name__ == "__main__":
            test_strings=["Привет мир"," ","one two three","1 2 3"]
            for i in range(len(test_strings)):
                print("Тест №%s"%i)
                print("Исходный список: %s"%test_strings[i])
                print(str_rev(test_strings[i]))
        else:
            task5()