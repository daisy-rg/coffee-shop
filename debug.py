

from model.customer import Customer
from model.cofee import Coffee
from model.order import Order

def debug():
   
    alice = Customer("Alice")
    bob = Customer("Bob")

    
    latte = Coffee("Latte", 3.5)
    espresso = Coffee("Espresso", 2.0)

    
    order1 = Order(alice, latte, latte.price)
    order2 = Order(bob, espresso, espresso.price)
    order3 = Order(alice, espresso, espresso.price)


    print("\n--- Customers and Their Orders ---")
    for customer in [alice, bob]:
        print(f"\nCustomer: {customer.name}")
        for order in customer.orders:
            print(f"  Ordered: {order.coffee.name} which cost ${order.coffee.price}")

    print("\n--- Coffees and Their Orders ---")
    for coffee in [latte, espresso]:
        print(f"\nCoffee: {coffee.name}")
        for order in coffee.orders:
            print(f"  Ordered by: {order.customer.name}")

if __name__ == "__main__":
    debug()