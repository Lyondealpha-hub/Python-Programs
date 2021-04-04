

def _reserve():
    userinput = input("Enter message here : ")
    arr = list(userinput)
    length = len(arr)
    reverse_message = " "

    for letter in range(length-1,-1,-1) :
        reverse_message += userinput[letter]
    print(reverse_message);

if __name__ == "__main__" :
    _reserve()
