import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('треба поїсти')
        self.gladness -= 10
        self.progress += 5

    def to_sleep(self):
        print('Час спати')
        self.gladness += 5

    def to_chill(self):
        print('Час відпочити')
        self.gladness += 10
        self.progress -= 2

    def is_alive(self):
        if self.progress <= 5:
            print('Виправляйся!')
        elif self.gladness <= 0:
            print('Ти сумний')
        elif self.progress >= 10:
            print('Ти молодець')

    def end_of_the_day(self):
        print(f"gladness - {self.gladness}")
        print(f" progress - {round(self.progress, 2)}")

    def live(self, day):
        day = 'Сьогодні день ' + str(day) + ' по імені - ' + self.name
        print(f"{day:^80}")
        kubik = random.randint(1, 3)
        if kubik == 1:
            self.to_study()
        elif kubik == 2:
            self.to_sleep()
        elif kubik == 3:
            self.to_chill()
        self.is_alive()
        self.end_of_the_day()


men = Student(name='сігма')

for day in range(365):
    if men == False:
        break
    men.live(day)