import random



def ranA():
    return random.random()

def ranB():   
    return random.random()


for i in range(1, 10000):
    print(ranA(), ranB())
    if(ranA() == ranB()):
        print("yes")
        break
    else:
        continue

print("\n\ndone")