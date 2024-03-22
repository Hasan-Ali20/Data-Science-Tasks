age = int(input("Please enter your age: ")) #This prompts the user to enter their age and converts the input to an integer, which is then stored in the variable called age
#Next we will check multiple age condiitions and print corresponding messages 
if age > 100:
    print ("Sorry, you're dead.") #If the age is over 100
elif age >= 65:
    print ("Enjoy your retirment!") #If the age is 65 or older
elif age >= 40:
    print ("You're over the hill.") #If the age is between 40 and 64, including 40
elif age == 21:
    print ("Congrats on your 21st!") #If the age is exactly 21
elif age < 13:
    print ("You qualify for the kiddie discount.") #If the age is less than 13
else:
    print ("Age is but a number.") #If none of the conditions are met, this is the default output