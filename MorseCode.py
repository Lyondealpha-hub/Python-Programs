"""Create a Morse code prototype"""

morseCode_dict = {
    " ": "/", "a": ".-","b":".--", "c":".-*-","d":".----","e":".--%#--",
    "d": "..-", "e":"..--","f":"..-@-","g":"..----","h":"..-----","i":"...-",
    "j":"...--","k":"...---","l":"...--!-","m":"...--$--","n":"....-","o":"....--",
    "p":"....---","q":"....----","r":"....--&--","s":".....-","t":"..^..--","u":".....---",
    "v":".....----","x":".....--**--","y":"*.","z":"*-."

}

def convert_to_morse(userinput:str)-> str :
    new_string = ""

    for char in userinput :
        if char.lower() in morseCode_dict :
            new_string += morseCode_dict[char.lower()] + "\n"
        else :
            raise ValueError(f"invalid character: {char}")
    new_string = new_string[:len(new_string)-1]
    return new_string

def _start_interactively():
    while True :
        userinput = input("Enter message here : ")
        morsecode = convert_to_morse(userinput)
        print("Morse_Code : " + morsecode)

if __name__ == "__main__" :
    _start_interactively()
