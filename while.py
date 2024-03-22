#we have 2 variables, where 'num' and 'count' are set at 0
#another variable 'user_input' prompts the user to enter a number and stores it as a float, using float just in case a user enters a number with a decimal
num = 0 
count = 0
user_input = float(input("Please enter a number (to exit enter -1): "))

#using a 'while loop', it allows the user to keep entering a number when the number the user enters is not -1
#everytime a user enters a number, the user's number will be added together and stored in the variable 'num'
#everytime a user enters a new number the count will go up by 1
while user_input != -1: 
    num += user_input
    count += 1
    user_input = float(input("Please enter a number (to exit enter -1): "))

#the 'if' statement will check for any valid counts above 0 
#if true then the code will display the average number by dividing the 'num' by the 'count' 
#by using ':.2f" in our code will display the average to 2 decimal places to make the number look sensible
#however if the first number the user enters is -1 then the program will display to the user that no valid numbers have been entered
if count > 0: 
    average = num/count
    print (f"The average of the numbers that were inputted is: {average:.2f}")
else:
    print ("No valid numbers have been entered please try again!")