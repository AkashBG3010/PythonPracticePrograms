import random

print("---Welcome to Betting Game---")

stake = int(input("Enter the stake: \n"))
goal = int(input("Enter the goal: \n"))
trials = int(input("Enter number of trials: \n"))

total_bets = 0
total_wins = 0

for i in range(int(trials)):
    cash = stake
    while (cash > 0) & (cash < goal):
        total_bets = total_bets + 1
        if (random.randint(1, 2)) == 1:
            cash = cash + 1
        else:
            cash = cash - 1

    if cash == goal:
        total_wins = total_wins + 1

print("----------------RESULTS---------------")
total_loss = trials - total_wins
print(total_wins, " wins out of ", trials)
print("Percent of games won = ", ((total_wins / trials) * 100))
print("Percent of games Loss = ", ((total_loss / trials) * 100))

print("----End of Program-----")