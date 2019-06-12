def clean20(x):
    for i in range(1,21):
        if x%i:
            return 0
    return 1

start=1
while True:
    if clean20(start):
        break
    start+=1

print("Smallest positive number evenly divisible by 1 to 20: %d\n"%start)