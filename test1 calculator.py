

what = input('What function? (+,-,*,\) :')

#print( Back.CYAN)

a = float (input("Input the first number: "))
b = float (input("Введи второе число:"))

#print( Back.MAGENTA)

if what == "+":
    c = a + b

    print ("Результат:" + str(c))


elif what == "-":
     c = a - b

     print ("Результат:" + str(c))

elif what == "*":
     c = a * b

     print ("Результат:" + str(c))

elif what == "/":
     c = a / b

     print ("Результат:" + str(c))

else:
     print ("Выбрана неверная операция!")    

input()     

    

  
