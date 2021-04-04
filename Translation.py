#A translation / replacement Program
def translate (text) :
    translation = ""
    for letter in text :
        if letter in "AEIOUaeiou" :
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
