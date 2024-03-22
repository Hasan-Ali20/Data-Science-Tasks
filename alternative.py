#we prompt the user to enter a sentence of their choice, casting it into a string and storing the input in the variable 'sentence'
#we then create an empty string that will store the modified sentence in the variable 'final_string' 
sentence = str(input("Please enter a sentence of your choice: ")) 
final_string = "" 

#using the 'for' loop we will iterate through each character in the variable 'sentence'
#then using the 'if' statement, if the index if the character is even, then it will be converted to uppercase and stored in the variable 'final_string' 
#and if the index of the character is odd, then it will be converted to lowercase and stored in the variable 'final_string'
#the variable 'final_string' will then be displayed with the modified string
for i in range(len(sentence)): 
    if i % 2 == 0:
        final_string += sentence[i].upper()
    else:
        final_string += sentence[i].lower()
print (final_string)

#we split the modified sentence into a list of words and stores it in the variable 'split_sentence'
#we create an empty list which will store the modified words in the variable 'join_sentence'
split_sentence = final_string.split() 
join_sentence = [] 

#using the 'for' loop we will iterate through each word in the modified sentence
#if the index is odd, convert the word to uppercase and add it to 'join_sentence'
#and if the index is even, convert the word to lowercase and add it to 'join_sentence'
for i in range(len(split_sentence)):
    if i % 2 == 1:
        join_sentence.append(split_sentence[i].upper())
    else:
        join_sentence.append(split_sentence[i].lower())

#joins the modified words together and stores it in the variable 'new_sentence'
new_sentence = " ".join(join_sentence)

#displays the modified sentence
print(new_sentence)