#made a variable 'rows' storing the integer 9, indicating that we want 9 lines for our '*' pattern
rows = 9 

#using a 'for' loop with 'range(1, rows + 1)', means we will iterate from 1 to 9 (inclusive)
#this loop will create the rows for our pattern

#the 'if' statement checks if the current iteration is less than or equal to 5
#if true, it prints '*' characters, and the number of '*' depends on the current iteration, this will be done in an ascending order

#using the 'else' statement, when the iteration is from rows 6-9 the '*' symbol will be printed but in a descending order
#using (rows - i + 1) ensures that even if the result of the code calculates to 0, we print at least 1 '*' in the last row 

#the result is a pattern where '*' characters increase for the first 5 rows and decrease for the next 4 rows
for i in range(1, rows + 1):
    if i <= 5:
        
        print("*" * i)
    else:
        
        print("*" * (rows - i + 1))