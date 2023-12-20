#Main file for application


from datetime import datetime, date, timedelta

class TakeInps:
    def __init__(self, start_year, AS2, AS10, AS16, AS26, AS28, AS19):
        self.AS2 = AS2
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

# Creating an instance of TakeInps
trialer = TakeInps(start_year=None, AS2=None, AS10=None, AS16=None, AS26=None, AS28=None, AS19=None)







  
  
