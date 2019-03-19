import logging

logging.basicConfig(level=logging.FATALc)


class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.info("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logging.info("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        logging.info("Ate {} pizza(s)".format(quantity, self.name))


pizza_01 = Pizza("artichoke", 15)
pizza_01.make()
pizza_01.eat()

pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
pizza_02.eat()