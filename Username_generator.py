import random

"""This is a very hard username generator.... """
name = input("Enter full name here : ")
first_letter = name[0]
space_index = name.find(" ")
emialString = ""
length = len(name)
print(length, space_index, space_index/2)
if length > space_index:
#this part deletes the first space between name and surname
#making it one full name
    name = name[:space_index] + name[space_index +1::]
    first_namepick = name[:int(space_index/2)]
#Here the second name after the space, reverses and due to
# half the length of the name it slices the name based on the number
    second_namepick = name[:int(length/2):-1]
    number = random.randrange(1,999)
    emailString = "@gmail.com"
    suggested_name = first_namepick + second_namepick+str(number) + emailString
print(suggested_name)


"""Or i can make the username generator very eazy by taking alone the first
letter of a full name and slicing few letters to add to the first letter
with an addition of a number"""






"""limiter = " "
name_1 = input("Enter fist_name : ")
name_2 = input("Enter second_name : ")
a = name_1[::-1]
b= name_2[0:5]
print("professional name generated ", limiter.join(a+b))"""
