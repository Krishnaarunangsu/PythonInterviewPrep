from custom_exception.custom_exception import DividendError
class Division:
    """
    Class for Division

    Attributes:
        new_list:list
    Methods:
        division_norm(self,multiplier_1:int, multiplier_2:int)
            Returns a list of integers divisible by 7 but  not divisible by 5
        division_list_comprehend(self, multiplier_1: int, multiplier_2: int)
            Returns a list of integers divisible by 7 but  not divisible by 5



    """
    new_list=[]
    def __init__(self, start:int, end:int)->int:
        """

        Args:
            start:
            end:
        Returns:

        Raises:
              DividendError
        """
        if not isinstance(start,int) or not isinstance(end, int):
            raise DividendError('Dividend is not an integer', 100)
        else:
            if start < 0:
                raise DividendError('Dividend is less than zero', 101)
            elif end <= 0:
                raise DividendError('Dividend is less than or equal to zero', 100)
            else:
                self.start = start
                self.end = end

    def division_norm(self, multiplier_1:int, multiplier_2:int)->list:
        """

        Args:
            multiplier_1:
            multiplier_2:

        Returns:
            new_list:list
                    A list of integers divisible by 7 but  not divisible by 5

        Raises:
            ZeroDivisionError

        """
        i: int
        for i in range(self.start, self.end):
            # print(i%7)
            if multiplier_1 ==0 or multiplier_2==0:
                raise ZeroDivisionError('Divisor is zero')
            if i % multiplier_1 == 0 and i % multiplier_2 != 0:
                    print(i)
                    self.new_list.append(i)
        print(self.new_list)
        return self.new_list



    def division_list_comprehend(self, multiplier_1: int, multiplier_2: int) -> list:
            """

            Args:
                self:
                multiplier_1:
                multiplier_2:

            Returns:
                new_list:list
                    A list of integers divisible by 7 but  not divisible by 5

            Raises:
                ZeroDivisionError

            """
            if multiplier_1 ==0 or multiplier_2==0:
                raise ZeroDivisionError('Divisor is zero')
            new_list = [i for i in range(self.start, self.end) if i % multiplier_1 == 0 and i % multiplier_2 != 0]
            print(new_list)
            return new_list

if __name__=="__main__":
    division=Division(5,36)
    division.division_norm(7,5)
    division.division_list_comprehend(7,5)

