
userinput = input("Enter sentence here : ")
length = len(userinput)
print(length)

if length%2 == 0:
    userinput = userinput[:int(length/2)]
    print(userinput)
else:
    print(userinput + " is odd -> String is invalid")
