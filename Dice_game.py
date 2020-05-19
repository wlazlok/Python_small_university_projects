import random

class Die:
    def __init__(self, sides):
        self._sides = sides
        self._value = None
    def roll(self):
        self._value = random.randint(1, self._sides)
    def get_sides(self):
        return self._sides
    def get_value(self):
        return self._value

die_computer = Die(8);
die_user = Die(6)

sum_comuter = 0
sum_user = 0
next_throw = True

while next_throw == True and sum_user < 21:
    die_user.roll()
    sum_user += die_user.get_value()
    if sum_comuter not in range(18, 21):
        die_computer.roll()
        sum_comuter += die_computer.get_value()
    print("Score: ", sum_user)

    if sum_user >= 21 or sum_comuter >= 21:
        break
    choice = input("Thorw (y/n)")
    next_throw = True if choice == 'y' or choice == "Y" else False
while sum_comuter < sum_user < 22:
    die_computer.roll()
    sum_comuter += die_computer.get_value()
print("Your score: ", sum_user)
print("Computer score: ", sum_comuter)

if sum_user > 21:
    print("You lose")
elif sum_comuter > 21:
    print("You win")
elif sum_comuter == sum_user:
    print("Draw")
elif sum_user > sum_comuter:
    print("You win")
else:
    print("You lose")