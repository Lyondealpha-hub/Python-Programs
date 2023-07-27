
print("A program to hold and calc house hold items")

setupCat = ''
header = list("")
subheader = list("")
array = [
[header],
[subheader]
]
subcat = ''
while setupCat != '0':
    setupCat = str((input('Please Enter your Household Categories : ')))
    header += [setupCat]
print("*******************************************************************")
print("*******************************************************************")
while subcat != '0' or subcat != len(header) :
     subcat = str(input("Please Enter in your subcatergories respectively: "))
     subheader += [subcat]



print(header)
print(subheader)



#n = input("Please Enter the header for the category:")
#item = [""]
#try:
#    x = item +n
#except:
 #   x = n

#item = [n]
#print(item[0])
