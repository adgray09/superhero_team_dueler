class Animal:
    def __init__(self, name, sleep_time):
        self.name = name
        self.sleep_time = sleep_time

    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleep_time))

#dog = Animal("Sophie", 12)
#dog.sleep()


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()