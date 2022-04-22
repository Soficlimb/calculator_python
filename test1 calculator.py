
a = float (input("Input the first number: "))

what = input('What function? (+,-,*,\) :')

b = float (input("Input the second number:"))


if what == "+":
    c = a + b

    print ("Resalt:" + str(c))


elif what == "-":
     c = a - b

     print ("Resalt:" + str(c))

elif what == "*":
     c = a * b

     print ("Resalt:" + str(c))

elif what == "/":
     c = a / b

     print ("Resalt:" + str(c))

else:
     print ("Invalid operation!")    

input()     

    

  
