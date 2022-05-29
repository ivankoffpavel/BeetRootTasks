import random
i=0
while i < 5:
    gen = random.randint(1, 1000)
    if gen % 5 ==0:
        i+=1
        print(gen)