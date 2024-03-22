#the task itself asks us to prompt the user to enter three different integers, hence it is is casted as an integer and not a float
#the user is prompted to enter three different integers
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a different integer: "))
num3 = int(input("Please enter another integer that is unique to the first two: "))

sum = num1 + num2 + num3 #numbers the user enters will be added together and stored in the variable 'sum' 
print (sum) #displays the sum of the three numbers

minus = num1 - num2 #users number 1 will be substracted by their number 2 and stored in the variable 'minus'
print(minus) #displays the number you get when you subtract the users number 1 by their number 2

multiply = num3 * num1 #users number 3 will be multipled by their number 1 and stored in the variable 'multiply'
print(multiply) #displays the number you get when you multiple the users number 3 by their number 1

divide = sum / num3 #users numbers added together will be divided by the users number 3 and stored in the variable 'divide' 
print (divide) #displays the number you get when you divide the sum of the users number by their number 3