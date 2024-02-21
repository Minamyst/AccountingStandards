class AS_2:
    def __init__(self, cost, MarVal):
        self.cost = cost
        self.MarVal = MarVal

    def get_cost(self):
        return self.cost

    def get_marval(self):
        return self.MarVal


from Inputs import TakeInps  

# Creating an instance of TakeInps
trialer = TakeInps(start_year=None, cost=None, MarVal=None, AS10=None, AS16=None, AS26=None, AS28=None, AS19=None)

# Calling the calculate_value() method
cost, MarVal = trialer.calculate_value()

# Now you can use cost and MarVal in the AS_2 class or perform any other operations


# Perform comparison or other operations as needed
if MarVal < cost:
    print("Inventory cost as per AS 2 is:", MarVal)
else:
    print("Inventory value as per AS 2 is:", cost)
