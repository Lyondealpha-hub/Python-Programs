



def _vowels_count() :
    userinput = input("Enter a message here : ")
    arr = list(userinput)
    length = len(arr)
    vowel_arr = []


    for letter in arr :
        if letter in "aeiou" :
            vowel_arr.append(letter)
            lent = len(vowel_arr)

    print("there are ", lent, " vowels in this arraylist : ", vowel_arr)
        #else :
        #    print("letter " + letter + " not a vowel")

if __name__ == "__main__" :
    _vowels_count()
