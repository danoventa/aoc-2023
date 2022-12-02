fsd1 = open("sample_data1.txt", "r").read().splitlines()
fsd2 = open("sample_data2.txt", "r").read().splitlines()
fd1 = open("data1.txt", "r").read().splitlines()
fd2 = open("data2.txt", "r").read().splitlines()


decoder = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

choice_score = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

referee = {
    "ROCK:SCISSORS": 0,
    "ROCK:PAPER": 6,
    "SCISSORS:ROCK": 6,
    "SCISSORS:PAPER": 0,
    "PAPER:ROCK": 0,
    "PAPER:SCISSORS": 6
}

# Part 1
my_score = 0
for round in fsd1: 
    elf1,elf2 = round.split()
    elf1_play = decoder[elf1]
    elf2_play = decoder[elf2]

    my_score +=  choice_score[elf2_play]

    if elf1_play == elf2_play:
        my_score += 3
    else :
        my_score += referee["{}:{}".format(elf1_play, elf2_play)]


print(my_score)

### Part 2

decoder2 = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": lambda elf1: "SCISSORS" if elf1 == "ROCK" else "ROCK" if elf1 == "PAPER" else "PAPER",
    "Y": lambda elf1: elf1,
    "Z": lambda elf1: "PAPER" if elf1 == "ROCK" else "ROCK" if elf1 == "SCISSORS" else "SCISSORS"
}

my_score2 = 0
for round in fd1: 
    elf1,elf2 = round.split()
    elf1_play = decoder2[elf1]
    elf2_play = decoder2[elf2](elf1_play)

    my_score2 +=  choice_score[elf2_play]

    if  elf2_play == elf1_play:
        my_score2 += 3
    else:
        my_score2 += referee["{}:{}".format(elf1_play, elf2_play)]

print(my_score2)