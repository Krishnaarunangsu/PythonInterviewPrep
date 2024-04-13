from custom_exception.custom_exception import IntegerCheckError
# n=6
# x=1
# while(n>1):
#     x=x*n
#     n=n-1
# print(x)

class FactorialCalculation:
    """
    Class For Factorial Calculation
    """
    def __init__(self, input:int):
        """

        Args:
            input:int
                Entered number for factorial calculation
        """
        self.factorial=None
        if not isinstance(input, int):
            raise IntegerCheckError("Entered input is not an integer", 100)
        else:
            if input < 0:
                raise IntegerCheckError("Entered integer is negative", 101)
            else:
                self.input=int(input)
                self.factorial=self.input*fact(self.input-1)
                # print(cls.factorial)

    def __str__(self):
        """

        Returns:

        """
        return str(self.factorial)




def fact(n):
    """

    Args:
        n:

    Returns:
        x: int
        Returns the factorial of a positive integer

    """
    fact_int=n
    if n==0:
        return 1
    else:
        return n*fact(n-1)

if __name__=="__main__":
    n=input("Enter a non-negative integer:")
    x=int(n)
    factorial_calculation=FactorialCalculation(x)
    print(f'Factorial Calculation:{factorial_calculation}')
