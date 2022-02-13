import sys
from io import StringIO
from VendingMachine import countCurrency


def test_countCurrency_output_for_tens() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    countCurrency(26)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_countCurrency_input_any(capsys) -> None:  # to check the output matches expected output
    countCurrency(14)
    out, err = capsys.readouterr()
    assert out == ''


def test_countCurrency_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    countCurrency(0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_countCurrency_input_large(capsys) -> None:  # to check the output matches expected output
    countCurrency(154)
    out, err = capsys.readouterr()
    assert out == ''
