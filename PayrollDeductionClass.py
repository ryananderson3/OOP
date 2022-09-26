
class PayrollDeduction():

    def __init__(self,d,da,a,idn):
        self.description = d
        self.date = da
        self.amount = a
        self.idNum = idn
    
    def get_Description(self):
        return self.description
    
    def get_Date(self):
        return self.date
    
    def get_ChargeAmount(self):
        return self.amount

    def get_payIDNum(self):
        return self.idNum
