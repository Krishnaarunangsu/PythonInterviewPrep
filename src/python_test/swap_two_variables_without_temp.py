class SwapTwoVariablesWithoutTemp:
    """
    Swap two variables without temp
    """
    def __init__(self):
        """

        """
        self.a=None
        self.b=None
    def swap_two_variables_without_temp(self):
        """

        Returns:

        """
        self.a, self.b=self.b, self.a

    def print_swapped_values(self, a, b):
        """

        Args:
            a:
            b:

        Returns:

        """
        self.a=a
        self.b=b
        self.swap_two_variables_without_temp()
        print(f'Swapped Values:{self.a,self.b}')


if __name__=="__main__":
    swap_variables_without_temp=SwapTwoVariablesWithoutTemp()
    x=input("Enter the 1st number:")
    print(x)
    y=input("Enter the 2nd number:")
    print(y)
    swap_variables_without_temp.print_swapped_values(x,y)