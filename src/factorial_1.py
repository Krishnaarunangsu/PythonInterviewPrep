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
    def __new__(cls, input:int):
        """

        Args:
            input:int
                Entered number for factorial calculation
        """
        cls.factorial=None
        if not isinstance(input, int):
            raise IntegerCheckError("Entered input is not an integer", 100)
        else:
            if input < 0:
                raise IntegerCheckError("Entered integer is negative", 101)
            else:
                cls.input=int(input)
                cls.factorial=cls.input*cls.fact(cls.input-1)
                # print(cls.factorial)
                return cls.factorial



    @classmethod
    def fact(cls,n):
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
            return n*cls.fact(n-1)

if __name__=="__main__":
    n=input("Enter a non-negative integer:")
    x=int(n)
    factorial_calculation=FactorialCalculation(x)
    print(f'Factorial Calculation:{factorial_calculation}')
