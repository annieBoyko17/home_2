import random
class cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 10
        self.friskiness = 0
        self.alive = True
    def to_eat(self):
        print("Time to eat!")
        self.gladness += 4
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.friskiness -= 3
    def to_play(self):
        print("Time to play")
        self.gladness += 3
        self.friskiness += 5
    def to_shame(self):
        print("My mistress is angry((")
        self.gladness -= 6
        self.friskiness -= 2
    def is_alive(self):
        if self.friskiness < -9:
            print("Laziness")
            self.alive = False
        elif self.gladness <= 1:
            print("Depression…")
            self.alive = False
        elif self.friskiness > 90:
            print("I`m the fannies cat!")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Friskiness = {round(self.friskiness, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4:
            self.to_shame()
            self.end_of_day()
            self.is_alive()


lucky = cat(name="Lucky")
for day in range(365):
 if lucky.alive == False:
    break
 lucky.live(day)