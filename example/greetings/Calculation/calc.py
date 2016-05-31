__author__ = 'Adebayo'


class Calc:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def item_sum(self, num):
        self.items = num
        if len(self.items) == 1:
            return self.items[0]
        else:
            return self.items[0] + self.item_sum(self.items[1:])

    def __str__(self):
        return self.item_sum(self.items)

if __name__ == '__main__':
    print(Calc().item_sum([1,2,3,5]))


class Factorial:

    def __init__(self):
        self.fact = 1

    def factorial(self, num):
        self.fact = num
        if self.fact == 0 or self.fact == 1:
            return 1
        else:
            return self.fact * self.factorial(self.fact - 1)

    def __str__(self):
        return self.factorial(self.fact)

if __name__ == '__main__':
    print(Factorial().factorial(1))


