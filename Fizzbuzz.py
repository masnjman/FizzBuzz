for x in range(1, 101):
    if(not x%3 and not x%5):
        print("FizzBuzz")
        continue
    elif(not x%3):
        print("Fizz")
        continue
    elif(not x%5):
        print("Buzz")
        continue
    else:
        print(x)