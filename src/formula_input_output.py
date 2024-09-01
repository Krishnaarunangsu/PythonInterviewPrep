import math
class FormulaCalculation:
    """
    Class for FormulaCalculation
    """
    C=50
    H=30
    def __init__(self,input_d):
        """

        Args:
            input_d:
        """
        self.input_d=input_d
        self.list_num=None
        self.list_digit=None
        self.list_cal=None
    def calculate(self):
        """

        Returns:

        """
        print(type(self.input_d))
        self.list_num = self.input_d.split(",")
        print(self.list_num)
        self.list_digit = [int(x) for x in self.list_num if isinstance(int(x), int)]
        print(self.list_digit)
        self.list_cal = [round(math.sqrt(2 * (10 * x) / 5))  for x in self.list_digit]
        print(self.list_cal)

if __name__=="__main__":
    input=input("Enter the numbers:")
    calculate_formula=FormulaCalculation(input)
    calculate_formula.calculate()
