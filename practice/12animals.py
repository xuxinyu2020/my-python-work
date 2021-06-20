"""继承和多态练习"""
class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

dog = Dog()
cat=Cat()
dog.run()
cat.run()

print(isinstance(dog,Animal))
print(isinstance(dog,Dog))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())