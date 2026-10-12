print("Welcome to sentence analysis\n")
print("You have to give a sentence with 5 words\n")
print("Lets start\n")
str=input("enter your string:")
print("\n")
words=str.split()
print("The number of words:",len(words),"\n")
words_join=''.join(words)
print("sentence without spaces:",words_join,"\n")
unique_char=''.join(dict.fromkeys(words_join))
print("sentence with only unique char:",unique_char,"\n")
print("The first word:",words[0],"& The last word:",words[len(words)-1],"\n")
new_word=words_join.lower()
rev=new_word[::-1]
print("The reverse sentence:",rev,"\n")
if(new_word==rev):
 print("Palindrome\n")
else:
 print("Not palindrome\n") 
print("The length of individual words:",len(words[0]),len(words[1]),len(words[2]),len(words[3]),len(words[4]))
 
