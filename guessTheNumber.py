import random

print("Guess The Number!")
number= random.randint(1, 100)
chances= 0
print("Guess A Number Between 1 and 100: ")
while chances<5:
    guess= int(input("Guess: "))
    if guess== number:
        print("Congratulation!!")
        break
    elif guess> number:
        print("Too High, Try Again")
    else:
        print("Too Low, Try Again")
    chances+=1

if chances > 5:
    print("You Lost...The Number Was", number)