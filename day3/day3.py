import string

fsd1 = open("sd1.txt", "r").read().splitlines()
# fsd2 = open("sd2.txt", "r").read().splitlines()
fd1 = open("d1.txt", "r").read().splitlines()
# fd2 = open("d2.txt", "r").read().splitlines()

def get_priority(alpha, letter):
    if alpha:
        return alpha[letter]
    else:
        alpha = populate_alpha(alpha)
        return alpha[letter]

def populate_alpha(alpha):
    counter = 1
    for letter in string.ascii_lowercase:
        alpha[letter] = counter
        counter += 1
    
    for letter in string.ascii_uppercase:
        alpha[letter] = counter
        counter += 1
    
    return alpha

sacks = []
alpha = {}

# Common items in same rucksack
for items in fd1:
    sacks.append(items[0:int(len(items)/2)])
    sacks.append(items[int(len(items)/2):])

priority = 0
for cargo1, cargo2 in zip(*[iter(sacks)]*2):
    common = list(set(cargo1).intersection(cargo2))
    if len(common) > 0:
        for item in common:
            priority += get_priority(alpha, item)

print(priority)

groups = []
# Common items in groups
priority = 0
for sack1, sack2, sack3 in zip(*[iter(fd1)]*3):
    badge = set(sack1).intersection(sack2).intersection(sack3)
    if len(badge) > 0:
        for item in badge:
            priority += get_priority(alpha, item)

print(priority)


# a-z = 1-26
# A-Z = 27-52