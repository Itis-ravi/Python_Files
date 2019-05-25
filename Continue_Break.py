# Continue is used to check if a condition is met then skip that particular iteration 
# Break is used to skip all the iteration once a comdition has been met

for i in range(6):
    if i==3:
        continue
    print('Hello',i)

print()

for i in range(4):
    if i==3:
        break
    print('Hello',i)
