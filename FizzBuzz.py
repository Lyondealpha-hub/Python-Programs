#A program that changes multiple of 3 to fizz, multiple of 5 to buzz and multiple of
#both 3 and 5 to fizzbuzz

print("A program for a FIZZBUZZ ")

for i in range(1,101):
    if i%3==0:
        print( i, "\t","Fizz")
    if i%5 == 0:
        print(i, "\t","Buzz")
    if i%3==0 and i%5==0:

        print(i, "\t","FizzBuzz")
