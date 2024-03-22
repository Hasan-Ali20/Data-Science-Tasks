str_manip = input("Please enter a sentence of your choice: ") #prompts the user to enter a sentence of their choice and stores it in the variable 'str_manip'
print(len(str_manip)) #displays the lengeth of the sentence the user entered

last_letter = str_manip[-1:] #extracts the last letter of the original sentence and stores it in the variable 'last_letter'
new_sentence = str_manip.replace(last_letter, "@") #the last letter of the sentence is replaced with @ and stored in the variable 'new_sentence'
print(new_sentence) #the modified string is displayed

backwards = str_manip[::-1] #reverses the original sentence and stores it in the variable 'backwards'
three = backwards[0:3] #extracts the first three characters of the reversed sentence and stores it in the variable 'three'
print(three) #the modified string is displayed

word_three = str_manip[0:3] #extracts the first theee characters of the original sentence and stores it in the variable 'word_three'
last_word = str_manip[-2:] #extracts the last two characters of the original sentence and stores it in the variable 'last_word'
five = word_three + last_word #concatenates the first three characters with the last two characters and stores it in trhe variable 'five'
print(five) #displays the modified result 