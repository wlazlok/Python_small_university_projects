import random
import sys
import time


class Ball:
    charged = False
    def __init__(self, number, isCharged):
        self.number = number
        self.charged = isCharged

    def __str__(self):
        return f"{self.number}, {self.charged}"

    def returnXD(self):
        return self.charged
    def returnNumber(self):
        return self.number

class LotteryMachine:

    balls_list = []
    tmp_count_charged = 0

    def __init__(self):
        for x in range(0, 49):
            number = random.randrange(6)
            if(number == 1 and self.tmp_count_charged < 6):
                self.tmp_count_charged += 1
                self.balls_list.append(Ball(x, True))
            else:
                self.balls_list.append(Ball(x, False))

    def print_list(self):
        for obj in self.balls_list:
            print(obj)

    def start(self, timeInSeconds):
        x = timeInSeconds/0.01
        x1 = 0
        while(x1 <= x):
            print(x1)
            self.lottery()
            time.sleep(0.01)
            x1 += 1
        self.stop()

    def stop(self):
        print("----------------------- WYNIKI ---------------------")
        for x in range(0, 6):
            print(self.balls_list[x].returnNumber())

    def lottery(self):
        a = random.randrange(0, 49)
        b = random.randrange(0, 49)
        while(a == b):
            b = random.randrange(0, 49)
        #print(str(a) + " " + str(b))
        x = self.balls_list[a]
        y = self.balls_list[b]
        self.balls_list[a] = y
        self.balls_list[b] = x

        for x in range(0, 49):
            if(self.balls_list[x].returnXD() == True):
                z = self.balls_list[x - 1]
                t = self.balls_list[x]
                self.balls_list[x] = z
                self.balls_list[x - 1] = t

class LottoPresenter:
    drawTime = 0
    def __init__(self):
        self.main()
    def main(self):
        print("Witamy w wielkim losowaniu!")
        choice = int(input("1.Start losowania\n2.Wyjscie"))
        if(choice == 1):
            drawTime = int(input("Podaj czas losowania (w sekundach):"))
            LotteryMachine().start(drawTime)
        else:
            sys.exit(0)

#LottoPresenter.main
#lm = LotteryMachine()
#lm.print_list()
#lm.start(5)

lp = LottoPresenter()
