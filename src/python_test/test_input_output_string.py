from src.python_test.input_output_test import InputOutputTest


def test_print_string_upper():
    ip = InputOutputTest()
    ip.get_input_string()
    assert ip.print_string_upper() == 'ccc'
