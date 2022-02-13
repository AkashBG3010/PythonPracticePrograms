import sys
from io import StringIO
from TemperatureConversion import conversion1, conversion2


def test_conversion1_output_for_tens() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    conversion1(26)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_conversion1_input_any(capsys) -> None:  # to check the output matches expected output
    conversion1(14)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 224\n224  is the power of 2\nDecimal value of  224 is: \n011100000'


def test_conversion1_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    conversion1(0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_conversion1_input_large(capsys) -> None:  # to check the output matches expected output
    conversion1(154)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 169\n169  is the power of 2\nDecimal value of  224 is: \n010101001'


def test_conversion2_output_for_tens() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    conversion2(26)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_conversion2_input_any(capsys) -> None:  # to check the output matches expected output
    conversion2(14)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 224\n224  is the power of 2\nDecimal value of  224 is: \n011100000'


def test_conversion2_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    conversion2(0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_conversion2_input_large(capsys) -> None:  # to check the output matches expected output
    conversion2(154)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 169\n169  is the power of 2\nDecimal value of  224 is: \n010101001'

