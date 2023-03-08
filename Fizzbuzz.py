#Creating a loop for variable x to increment by one from 1 to 100
for x in range(1, 101):
    #Checking if x is both a multiple of 3 and of 5,
    #if so, printing "FizzBuzz" and going on to the next number
    if(not x%3 and not x%5):
        print("FizzBuzz")
        continue
    #Checking if x is a multiple of 3,
    #if so, printing "Fizz" and going on to the next number
    elif(not x%3):
        print("Fizz")
        continue
    #Checking if x is a multiple of 5,
    #if so, printing "Buzz" and going on to the next number
    elif(not x%5):
        print("Buzz")
        continue
    #In the case that none of the conditions above are met,
    #the number "x" is printed
    else:
        print(x)