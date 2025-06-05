class Customer:
    def __init__(self,name):
        self.__name =name
        self.orders = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,customername):
        if isinstance(customername,str) and len(customername) >= 1 and len(customername) <= 15:
            self.__name = customername
        else:
            raise ValueError ("Customer name must be strings or between 1 to 15 characters ") 
        
    def list_orders(self):
         return self.orders
    def coffees(self):
        unique_coffee = []
        for order in self.orders:
            coffee = order.coffee

            if coffee not in unique_coffee:
                unique_coffee.append(coffee)

        return unique_coffee

    def create_order(self,coffee,price):
        from order import Order
        new_order = Order(self,coffee,price)
        coffee.orders.append(new_order)
        self.orders.append(new_order)
        

    @classmethod
    def regular_customer(cls,coffee):
        top_customer = None
        highest_total = 0

        for order in coffee.orders:
            customer = order.customer
            total = sum(o.price for o in customer.orders if o.coffee == coffee)

            if total > highest_total:
                highest_total = total
                top_customer  = customer


        return top_customer
        
    
    
    
    
    
    
    
    
    
    
    




