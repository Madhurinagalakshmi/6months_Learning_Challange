
class ExpenseAnalayzer:
    def __init__(self,expenses):
        self.expenses = expenses
    
    def find_total(self):
        if(len(self.expenses)==0):
            return 0
        total = 0
        for key in self.expenses.keys():
            total += self.expenses[key]
        return total
    def find_average(self):
        if(len(self.expenses)==0):
            return 0
        total = 0
        for key in self.expenses.keys():
            total += self.expenses[key]
        return total/len(self.expenses)
    
    def find_highest(self):
        if(len(self.expenses)==0):
            return None
        else:
            iterator = iter(self.expenses.items())
            first_pair = next(iterator)
            k,v = first_pair
            maxi = v
            for key in self.expenses.keys():
                maxi = max(maxi,self.expenses[key])
            return maxi
        
    def find_lowest(self):
        if(len(self.expenses)==0):
            return None
        else:
            iterator = iter(self.expenses.items())
            first_pair = next(iterator)
            k,v = first_pair
            mini = v
            for key in self.expenses.keys():
                mini = min(mini,self.expenses[key])
            return mini
        
    