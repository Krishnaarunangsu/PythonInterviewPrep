import json


class JSONDataExtractor:
    """
    Class for JSON Data Extractor
    """
    def __init__(self):
      """
      Initialization
      """
      self.json_data=None
      self.key=None
      self.value=None

    def extract_data(self,input_key)->str:
        """

        Args:
            input_key:

        Returns:

        """
        with open('data.json', 'r') as file:
            self.json_data = json.load(file)

        # Print the data
        print(self.json_data)
        self.value=self.json_data.get(input_key)
        print(f'The Value is:{self.value}')


if __name__=="__main__":
    json_data_extractor=JSONDataExtractor()
    json_data_extractor.extract_data("age")


# https://medium.com/@sharath.ravi/python-function-to-extract-specific-key-value-pair-from-json-data-7c063ecb5a15