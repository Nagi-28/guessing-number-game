'''def greet():
    print("hello")
name=input()
print(name)
greet()

def greet(word):
    msg="hello"+word
    print(msg)
name=input()
g=greet(word=name)
a=int(input())
factorial = 1
for i in range(1,a+1):
  factorial*= i
  print(factorial)
def factorial(n):
  if n==1:
    return 1
  return n*factorial(n-1)
num=int(input())
res=factorial(num)
print(res)
class animal:
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "woof!woof"
class cats(animal):
    def sound(self):
        return "meow"
d=dog()
c=cats()
print(d.sound())
print(c.sound()) 
#python project###
import random
def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0  # Initialize attempt counter
    
    while True:
        # Ask the user to input a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check the guess and give feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break  # End the game when the correct guess is made

# Run the game
guess_the_number()
###############################################

n=int(input())
sum=0
for i in range(1,n+1):
  sum=sum+(i**2)
print(sum)
rows=int(input())
columns=int(input())
for i in range(1,rows+1):
    print(columns*"*")
n=input()
num=''
for i in n:
    num=num+(i+"   ")
print(num)'''
n=int(input())
sum=0
for i in range(1,n+1):
    a=int(input())
    sum=sum+i
average=sum/n 
print(average)
