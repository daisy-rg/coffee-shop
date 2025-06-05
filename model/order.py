from .customer import Customer
from .cofee import Coffee


class Order:
    def __init__(self,customer:Customer,coffee:Coffee,price):
        if not isinstance(customer,Customer) :
            raise TypeError ("customer must be an instance of the Customer class")
       
        self.customer = customer

        if not isinstance(coffee,Coffee):
            raise TypeError ("coffee must be an instance of the Coffee class")
        
        self.coffee = coffee
        
        if not isinstance(price,(float,int)):
            raise TypeError ("Price must be a number")
        elif price <= 0:
            raise ValueError ("Price must be a positive number")
        else:
            self.price = price
        
        
        self.customer.orders.append(self)
        self.coffee.orders.append(self)