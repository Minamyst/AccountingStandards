from datetime import datetime, date, timedelta

today = date.today()
current_time = datetime.now().time()
now = datetime.now()


class FinancialYear:
    def __init__(self, start_year):
        self.start_year = start_year

    def get_current_financial_year(self):
        start_date = datetime(self.start_year, 4, 1)
        end_date = datetime(self.start_year + 1, 3, 31)

        return start_date, end_date


from Inputs import InputTaken

financial_year = FinancialYear(start_year)

start_date, end_date = financial_year.get_current_financial_year()

print("Financial Year Start Date:", start_date.strftime("%d-%m-%y"))
print("Financial Year End Date:", end_date.strftime("%d-%m-%y"))




