import datetime
class DateFormat():

    @classmethod
    def convert_data(self,date):
        return datetime.datetime.strftime(date,'%d/%m/%y')
    