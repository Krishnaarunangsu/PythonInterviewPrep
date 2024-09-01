class InputOutputString:
    """
    class for Taking a string input and convert to uppercse and print
    """
    def __init__(self):
        """

        """
        self.input_string=""
        self.output_string=""

    def get_input_string(self):
        """

        Returns:

        """
        #self.input_string=input("Enter the string:")
        self.input_string ="krishna"

    def print_string_upper(self):
        """

        Returns:


        """
        self.output_string=self.input_string.upper()
        return self.output_string
