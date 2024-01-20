import random
a=random.randint(0,9)
input_1=int(input("Enter the number: "))
count=0
while input_1: 
    if input_1 < a:
        int(input("Higher number please\n"))
    else:
        pass
    if input_1 > a:
        int(input("Lower number please\n"))
    else:
        count+=1
    if input_1==a:
        print("You guessed the right number with",count,"guesses")
        