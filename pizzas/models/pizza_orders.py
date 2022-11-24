from models.pizza import Pizza

pizza1 = Pizza(10, "pepperoni", False, "L")
pizza2 = Pizza(10, "cheese", False, "L")
pizza3 = Pizza(10, "seafood", True, "M")

pizzas = [pizza1, pizza2, pizza3]

def get_order(order_index):
    return pizzas[order_index]

def add_order(order):
    pizzas.append(order)