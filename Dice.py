import random
end = False
def roll ():
    n_of_dice = int(input("\nHow many dice do you want to roll per roll?: "))
    n_of_sides = int(input("\nHow many sides should each dice have?: "))
    for n in range(0, n_of_dice):   
        print("\n", random.randint(1, n_of_sides))

while end == False:
    roll()
    if input("\nDo you want to go again? (n=no): ") == "n":
        end == True
        break
           