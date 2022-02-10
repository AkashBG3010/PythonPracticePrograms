import random  # Importing random library

print("---Welcome to Betting Game---")


def startGame(stake, goal, trials):         # Function to start the game operation
    total_bets = 0  # Variables
    total_wins = 0  # Variables

    for i in range(int(trials)):  # Iterating till yhe number of trials
        cash = stake
        while (cash > 0) & (cash < goal):  # Specifying conditions for the gamplay
            total_bets = total_bets + 1
            if (random.randint(1, 2)) == 1:
                cash = cash + 1  # Incrementing if won
            else:
                cash = cash - 1  # Decrementing if won

        if cash == goal:
            total_wins = total_wins + 1  # if goal meets condition, then it holds good

    print("----------------RESULTS---------------")  # Printing the results
    total_loss = trials - total_wins
    print(total_wins, " wins out of ", trials)
    print("Percent of games won = ", ((total_wins / trials) * 100))
    print("Percent of games Loss = ", ((total_loss / trials) * 100))


stake = int(input("Enter the stake: \n"))   # Reading user input
goal = int(input("Enter the goal: \n"))     # Reading user input
trials = int(input("Enter number of trials: \n"))       # Reading user input

startGame(stake, goal, trials)      # Function Calling


print("----End of Program-----")