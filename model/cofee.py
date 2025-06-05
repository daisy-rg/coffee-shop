class Coffee:
    def __init__(self,name,price):
        self.__name = name
        self.price = price
        self.orders = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,coffeename):
        if isinstance (coffeename, str)and len(coffeename) >= 3:
            self.__name = coffeename
        else:
            raise ValueError("Coffee name must be a string and has more than 3 characters")


    def list_orders(self):
         return self.orders

    def customers(self):
        unique_customer = []
        for order in self.orders:
            customer = order.customer

            if customer not in unique_customer:
                unique_customer.append(customer)

        return unique_customer

    def num_orders(self):
        return len(self.orders)
            
    def average_price(self):
        if len(self.orders) == 0:
                return 0
        else:
           total_price = 0
           for order in self.orders:
               total_price += order.price
            
            
        length =len(self.orders)
        average_price = total_price / length
        
        return average_price

            