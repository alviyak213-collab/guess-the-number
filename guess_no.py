import random 
print("this is a number guessing game")
number = random.randint(1 , 20)
guess = None 

while guess != number:
    guess = int(input("guess a number between 1-20: "))
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print("yaah ! you have gussed it")
        print("the number was" , number) 