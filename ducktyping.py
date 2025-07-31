class bird:
    fly = True

class weirdObject:
    alive = False

class eangle(bird):
    def speak(self):
        print("EEEERRRRGGHEEEEAAAAH")

class crow(bird):
    def speak(self):
        print("CAW!")

class chicken(bird):
    def speak(self):
        print("Kuk-kukuk")

class radio(weirdObject):
    def sound(self):
        print("bla bla bla")

class car(weirdObject):
    def sound(self):
        print("Honk!")

birds = [eangle(), crow(), chicken()]

weirdObjects = [radio(), car()]


for bird in birds:
    bird.speak()
    print(bird.fly)

for weirdObject in weirdObjects :
    weirdObject.sound()
    print(weirdObject.alive)

