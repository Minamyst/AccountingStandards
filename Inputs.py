#Main file for application


from datetime import datetime, date, timedelta
import sys

class TakeInps:
    def __init__(self, start_year, cost, MarVal, AS10, AS16, AS26, AS28, AS19):
        self.cost =cost
        self.MarVal=MarVal
        self.start_year = start_year
        self.AS10 = AS10
        self.AS16 = AS16
        self.AS19 = AS19
        self.AS26 = AS26
        self.AS28 = AS28

    def get_inputs_start_year(self):
        start_year_input = input("Enter the current year of financial year: ")
        start_year = int(start_year_input)
        return start_year
    
    def calculate_value(self):
        met_1 = input("Enter Method of Valuation (LIFO, FIFO, or average): ")
        if met_1.lower() == "lifo":
            print("Method not accepted under AS 2")
            sys.exit()
        else:
            cost = float(input("Enter the cost: "))
            MarVal = float(input("Enter Market Value: "))
            self.cost = cost  # Update the cost attribute of the class instance
            self.MarVal = MarVal  # Update the MarVal attribute of the class instance
        return cost, MarVal

        

# Creating an instance of TakeInps
trialer = TakeInps(start_year=None, MarVal=None, cost=None, AS10=None, AS16=None, AS26=None, AS28=None, AS19=None)







  
  
