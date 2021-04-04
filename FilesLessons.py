
count = 0
while count == 5:
    userinput = input("Enter username : ")
    Age = int(input("Enter Age : "))
    gender = input("Enter Gender : ")
    Nationality = input("Enter nationality")
    count+=1
database = [
    ["Name " , "Age", "Gender", "Nationality"],
    [userinput,Age,gender,Nationality],
    [userinput,Age,gender,Nationality],
    [userinput,Age,gender,Nationality]
]

for row in database:
    print(row)