<<<<<<< HEAD:practice_problem_solutions (2026)/practice245.py
# Print in Order


from threading import Event
class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst) -> None:
        
        printFirst()
        self.first_done.set()


    def second(self, printSecond) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()


    def third(self, printThird) -> None:

        self.second_done.wait()        
        printThird()
=======
# CodeWars - Product of consecutive Fib numbers

def product_fib(_prod):
    a, b = 0, 1
    while a * b != _prod and a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]

print(product_fib(4895)) # [55, 89,  True]
print(product_fib(5895)) # [89, 144, False]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice245.py
