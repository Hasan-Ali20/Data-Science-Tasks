'''I will first prompt the user to input their swimming, cycling and running time and store them in variables
converting the input into an integer because the user might input their triathlon time specific which may have decimal places and not whole integers and
this will cause a disruption in our code, so this is why I asked the input to be nearest the minute; allowing our code to run smoothly'''
swimming = int(input("Please enter your swimming time to the nearest minute: "))
cycling = int(input("Please enter your cycling time to the nearest minute: "))
running = int(input("Please enter your running time to the nearest mintue: "))

time = (swimming + cycling + running) #Calculates the time by adding swimming, cycling and running together
print (f"Your triathlon time was {time} minutes") #Displays the triathlon time in minutes, using f string converts everything into string

#Checks the total time against various conditions and prints different messages as outputs
if 0 <= time <= 100:
    print ("Provincial Colours awarded!") #If the time is between 0 and 100 minutes (including 0 and 100)
elif 101 <= time <= 105:
    print ("Provincial Half Colours awarded!") #If the time is between 101 and 105 minutes (inclusive)
elif 106 <= time <= 110:
    print ("Provincial Scroll awarded!") #If the time is between 106 and 110 minutes (inclusive)
elif time > 111: 
    print ("No award!") #If the time is greater than 111 minutes
else:
    print ("Invalid, try again!") #If no conditions are met, this will be the default output message 