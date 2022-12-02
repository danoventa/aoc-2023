f = open("data_1.txt", "r").read().splitlines()

elves = []
food = []
for calories in f: 
    if(calories == ''):
        elves.append(food)
        food = []
    else: 
        food.append(int(calories))

macks1 = max(sum(elve) for elve in elves)
macks2 = sum(sorted([sum(elve) for elve in elves])[-3:])

print(macks1)
print(macks2)