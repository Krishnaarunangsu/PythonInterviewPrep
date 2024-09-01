# Converting Celsius to fahrenheit
class CelsiusFahrenheit:
    """
    Class to convert Celsius to Fahrenheit
    """
    constant_value=32
    def __init__(self):
        """
            Initialization
        """
        self.temperature_celsius=None
        self.temperature_fahrenheit=None

    def convert_celsius_fahrenheit(self)->float:
        """
        Converts Temperature in Celsius to Fahrenheit
        Returns:
            temperature_fahrenheit
        Raises
            TypeError

        """
        self.temperature_fahrenheit = (9 / 5) * self.temperature_celsius+self.constant_value
        return self.temperature_fahrenheit

    def display_temperature_fahrenheit(self,temperature_celsius):
        """
        Displays the temperature in Fahrenheit
        Args:
            temperature_celsius:

        Returns:

        Raises
            TypeError

        """
        try:
            if isinstance(float(temperature_celsius),float):
                self.temperature_celsius=float(temperature_celsius)
                self.temperature_fahrenheit=self.convert_celsius_fahrenheit()
        except:
            raise ValueError(f'Input Temperature is not in right format')
        print(f'The temperature in Fahrenheit is:{self.temperature_fahrenheit}')


if __name__=="__main__":
    celsius_fahrenheit=CelsiusFahrenheit()
    celsius_temperature=input("Enter the temperature in Celsius:")
    print(f'Type of the input:{type(celsius_temperature)}')
    celsius_fahrenheit.display_temperature_fahrenheit(celsius_temperature)

