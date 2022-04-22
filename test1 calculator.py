#Калькулятор V1 (цветной)

#from colorama import init
#from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
#init()

#print( Fore.BLACK ) #цвет текста
#print( Back.GREEN ) #цвет фона

what = input('Что делаем? (+,-,*,\) :')

#print( Back.CYAN)

a = float (input("введи певое число: "))
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

    

  
