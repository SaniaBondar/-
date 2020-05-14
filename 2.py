data={}
flag = True 
S  = r'C:\Users\bonda\Downloads\conf.txt'
with open(S , 'r') as f:
    for line in f:
        if line[0] != "#" and line[0] !=';' and line[0] != '\n':
            list0 = line.split(' ', 1)

            x=len(list0)
            if x>1:
                key = list0[0]
                value = list0[1]
                data[key]= value
            elif x == 1:
                key = list0[0].rstrip('\n')
                value = "Значение не задано"
                data[key]= value                
while flag:
    try:
        key = input("Введите ключ>>> ")
        print ("Ключ>>>", key," Значение>>>", data[key])   
    except:
        print("Ключ>>>", key," Значение>>> Такого ключа не существует")
    counter = 0
    i = 2
    while True:
        command = input("Повторить? Да\Нет>>> ")
        if command == "Да":
            break
        elif command == "Нет":
            break
        elif counter == 3:
            exit()
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