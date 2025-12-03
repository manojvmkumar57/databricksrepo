#proper OOPS - structurized module

class num_ops:#Template/Structure/Framework/Blueprint that holds variables & functions
    bonus=10
    def calc_bonus(self,sal):
        return sal+(sal*(10/100))


class str_ops:#Template/Structure/Framework/Blueprint that holds variables & functions
    def calc_bonus(self,fname,lname):
        return fname+' '+lname
    def f1(self,x):
        return x.upper()
