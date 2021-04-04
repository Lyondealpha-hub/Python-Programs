word = input("Enter a word : ")
palindrome = word[::-1]
print(palindrome)
if word == palindrome :
    print(word, " is a palindrome")
else :
    print(word, " is not a palindrome")