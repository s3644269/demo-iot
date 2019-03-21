import logging

logging.basicConfig(level=logging.ERROR)


class Pizza:
    quantity = None

    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.getLogger("PizzaMaker").debug(f"Pizza created: {self.name} (${self.price})")

    def make(self, quantity=1):
        if int(quantity) > 0:
            self.quantity = quantity
            logging.debug("Made {} {} pizza(s)".format(quantity, self.name))
        else:
            raise PizzaError("Cannot make zero or negative pizza")

    def eat(self, quantity=1):
        if int(quantity) <= self.quantity:
            self.quantity -= quantity
            logging.info("Ate {} pizza(s)".format(quantity, self.name))
        else:
            raise PizzaEatingError(f"Cannot eat more than {self.quantity} pizza/s!!!")


class PizzaError(Exception):
    pass


class PizzaMakingError(PizzaError):
    pass


class PizzaEatingError(PizzaError):
    pass


pizza_01 = Pizza("artichoke", 15)
try:
    pizza_01.make(1)
    pizza_01.eat(2)
except PizzaError as e:
    logging.error(e)


pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
pizza_02.eat()
