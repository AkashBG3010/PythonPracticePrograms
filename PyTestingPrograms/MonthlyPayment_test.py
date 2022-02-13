import sys
from io import StringIO
from MonthlyPayment import calculatePayment


def test_calculatePayment_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    calculatePayment(0, 0, 0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_calculatePayment_output_for_one() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    calculatePayment(1,1,1)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_calculatePayment_output_for_null() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    calculatePayment('','','')
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_calculatePayment_output_for_negative() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    calculatePayment(-5,6,-354)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_calculatePayment_output_for_symbol() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    calculatePayment('@','-','.')
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_calculatePayment_input_zero(capsys) -> None:  # to check the output matches expected output
    calculatePayment(0,0,0)
    out, err = capsys.readouterr()      # Fail, because it will not take input as 0
    assert out == ZeroDivisionError


def test_calculatePayment_input_negative(capsys) -> None:  # to check the output matches expected output
    calculatePayment(-5,-1,-32)
    out, err = capsys.readouterr()      # Fail, because it will not take input as -ve
    assert out == AssertionError


def test_calculatePayment_input_one(capsys) -> None:  # to check the output matches expected output
    calculatePayment(1,1,1)
    out, err = capsys.readouterr()      # Fail, because it will not take input as 1
    assert out == AssertionError


def test_calculatePayment_input_symbol(capsys) -> None:  # to check the output matches expected output
    calculatePayment('-','/','`')
    out, err = capsys.readouterr()      # Fail, because it will not take input as symbol
    assert out == TypeError
