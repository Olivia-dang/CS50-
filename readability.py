from cs50 import get_string

#get input
text = get_string("Text: ")
#initialise counters to 0: counter for letter, words, sentences, i
n_let = n_wor = n_sen = i = 0
#get length of text
length = len(text)

#while loop
while i<length:
     #count letters: simply be found using .isalpha() which sieves out alphabets and not the spaces in between
     if text[i].isalpha():
         n_let +=1
     #count words: first word followed by " ", second onwards: a letter immediately after " "
     if (i == 0 and text[i] != " ") or (i<length and text[i] == " " and text[i+1] != " "):
         n_wor +=1
     #count sentences: count ?.! then +1
     if text[i] == "!" or  text[i] == "?" or text[i] == ".":
         n_sen += 1
     i +=1
     
#use index math, remember to round
L = (n_let/n_wor) *100
S = (n_sen/n_wor) *100
index = round(0.0588 * L - 0.296 * S - 15.8)

#print out grades
if index<1:
    print("Before Grade 1")
elif index>16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
