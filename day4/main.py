fsd1 = open("sd1.txt", "r").read().splitlines()
fd1 = open("d1.txt", "r").read().splitlines()
fd2 = open("d2.txt", "r").read().splitlines()

elf_pairs = [pair.split(',') for pair in fd1]

counter = 0
for pairs in elf_pairs:
    elf1_assignment = [int(x) for x in pairs[0].split('-')]
    elf2_assignment = [int(x) for x in pairs[1].split('-')]

    if(elf1_assignment[0] == elf1_assignment[1]):
        elf1_work = set([elf1_assignment[0]])
    else:
        elf1_work = set(range(elf1_assignment[0], elf1_assignment[1] + 1))
    
    if(elf2_assignment[0] == elf2_assignment[1]):
        elf2_work = set([elf2_assignment[0]])
    else:
        elf2_work = set(range(elf2_assignment[0], elf2_assignment[1] + 1))

    if (len(elf1_work.intersection(elf2_work)) + len(elf2_work.intersection(elf1_work))) > 0:
        counter += 1

print(counter)