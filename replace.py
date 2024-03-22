sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog." #original statement has ! in it and stored in the variable 'sentence'
new_sentence = sentence.replace("!", " ") #replaces the ! in the sentence with blank spaces and stores the modified string in 'new_sentence'
print (new_sentence) #displays the modified string 

upper_sentence = new_sentence.upper() #converts the entire sentence to uppercase and stores it in the variable 'upper_sentence'
print (upper_sentence) #displays the modified string 

reverse_sentence = upper_sentence[::-1] #reverses the order of the characters in the sentence and stores it in the variable 'reverse_sentence'
print(reverse_sentence) #displays the modified string 