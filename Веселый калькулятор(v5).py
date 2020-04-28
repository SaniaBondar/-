#Веселый калькулятор 
print(" Добро пожаловать в весёлый калькулятор :)\n Я рад, что ты решил мною воспользоваться!\n У меня в арсенале имеется:\
\n Сложение ('+') и вычитание ('-')\n Умножение ('*') и деление ('/')\n Возведение в степень ('**')\n Деление по модулю ( '%' ) и целочисленное деление ('//')")
counter = 0
while counter < 3:
    what = input(" Говори что нужно посчитать ( + , - , * , / , ** , % , // ), либо можем отложить на потом (Q): ")
    if what[0]=="q":
        False
        break
    elif what[0]=="Q":
        False
        break
    elif what[0]=="й":
        False
        break
    elif what[0]=="Й":
        False
        break
    elif what[0]=="+":
        True
    elif what[0]=="-":
        True
    elif what[0]=="/":
        True
    elif what[0]=="*":
        True
    elif what[0]=="**":
        True
    elif what[0]=="%":
        True
    elif what[0]=="//":
        True
    else:
        counter += 1
        print(" Выбрана неверная операция, используй подсказки в скобках!")
        if counter == 2:
            print (" Еще одна попытка и программа закроется ;)")
        elif counter == 1:
            print (" Еще две попытки и программа закроется ;)")
        elif counter == 3:
            print(" Программа закрылась, попробуй потом, может быть кто-то подскажет что ты сделал не так")
        continue

    counter = 0
    
    try:
        a = float(input(" Введите первое число: "))
    except (TypeError, ValueError):
            print("Введите заново число, а не что-то другое!")
    try:
        b = float(input(" Введите второе число: "))
    except (TypeError, ValueError):
            print("Введите заново число, а не что-то другое!")
    print("***Ответ***")

    if what == "+":
        print ( a,"+",b,"=",a + b)
    elif what == "-":
        print ( a,"-",b,"=",a - b)
    elif what == "*":
        print ( a,"*",b,"=",a * b)
    elif what == "/":
        if b != 0:
            print ( a,"/",b,"=",a / b)
        else:
            b = 0
            print (" На ноль делить нельзя, ты не знал? :D")
    elif what == "**":
        print ( a,"**",b,"=",a ** b)
    elif what == "%":
        print ( a, "%",b, "=", a % b )
    elif what == "//":
        if b != 0:
            print ( a, "//",b, "=", a // b )
        else:
            b = 0
            print (" На ноль делить нельзя, ты не знал? :D")