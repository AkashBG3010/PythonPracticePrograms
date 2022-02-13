import sys
from io import StringIO
from DecimalToBinary import decimalToBinary


def test_decimalToBinary_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    decimalToBinary(0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_decimalToBinary_output_for_one() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    decimalToBinary(1)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_decimalToBinary_output_for_hundred() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    decimalToBinary(100)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_decimalToBinary_output_for_negative() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    decimalToBinary(-5)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_decimalToBinary_output_for_symbol() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    decimalToBinary('@')
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_decimalToBinary_input_zero(capsys) -> None:  # to check the output matches expected output
    decimalToBinary(0)
    out, err = capsys.readouterr()      # Fail, because it will not take input as 0
    assert out == AssertionError


def test_decimalToBinary_input_negative(capsys) -> None:  # to check the output matches expected output
    decimalToBinary(-5)
    out, err = capsys.readouterr()      # Fail, because it will not take input as 0
    assert out == AssertionError


def test_decimalToBinary_input_one(capsys) -> None:  # to check the output matches expected output
    decimalToBinary(1)
    out, err = capsys.readouterr()      # Fail, because it will not take input as 0
    assert out == AssertionError


def test_decimalToBinary_input_symbol(capsys) -> None:  # to check the output matches expected output
    decimalToBinary('-')
    out, err = capsys.readouterr()      # Fail, because it will not take input as 0
    assert out == TypeError
