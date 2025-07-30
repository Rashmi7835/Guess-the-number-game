print("..............guess the no game..............")
import random
n=random.randint(1,100)
a=-1
guesses=1

while(a != n) :
    a=int(input("guess the number:"))
    if(a<n):
        print("higher no please!!")
        guesses+=1
    elif(a>n):
        print("lower no please!!")
        guesses+=1

print(f'you have guessed the number {n} corrrectly in {guesses} attempt')
