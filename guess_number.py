import random

n = input("Enter a minimal number: ")
m = input("Enter a maximal numebr: ")

n = int(n)
m = int(m)

rn = random.randint(n, m)
    
while True:
    answer = input("Guess the number: ")
    answer = int(answer)

    if (rn == answer):
        print("Collect!")
        break
    else:
        print("Wrong!")