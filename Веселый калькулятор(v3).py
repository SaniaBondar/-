#Веселый калькулятор
print("Добро пожаловать в веселый калькулятор, я рад, что ты решил мною воспользоваться)\n У меня в арсенале имеется:\n Сложение ('+')\n Вычитание ('-')\n Умножение ('*')\n Деление ('/')\n Возведение в степень ('**')")
flag = True
while flag:
    what = input("Говори что нужно посчитать ( + , - , * , / , ** ), либо можем отложить на потом (q): ")
    if what[0]=="q":
        flag = False
        break
    elif what[0]=="+":
        flag = True
    elif what[0]=="-":
        flag = True
    elif what[0]=="/":
        flag = True
    elif what[0]=="*":
        flag = True
    elif what[0]=="**":
        flag = True
    else:
        print("Выбрана неверная операция, используй подсказки в скобках! ;) ")
        continue
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if what == "+":
        print (a,"+",b,"=",a + b)
    elif what == "-":
        print (a,"-",b,"=",a - b)
    elif what == "*":
        print (a,"*",b,"=",a * b)
    elif what == "/":
        if b != 0:
            print (a,"/",b,"=",a / b)
        else:
            b = 0
            print ("На ноль делить нельзя, ты не знал? :D")
    elif what == "**":
        print (a,"**",b,"=",a ** b)