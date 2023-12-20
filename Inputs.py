#Main file for application
Class InputTaken
  def __init__(self,start_year_input,AS2,AS10,AS16,AS26,AS28,AS19):
  self.AS2= AS2
  self.start_year_input= start_year_input
  self.AS10= AS10
  self.AS16=AS16
  self.AS19= AS19
  self.AS26= AS26
  self.AS28= AS28
  
  def get_inputs_user(self):
  start_year_input = input("Enter the current year of financial year: ")
  start_year = int(start_year_input)
  
  
  