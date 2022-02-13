import sys
from io import StringIO
from SquareRoots import squareRoot


def test_squareRoot_output_for_tens() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    squareRoot(26)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_squareRoot_input_any(capsys) -> None:  # to check the output matches expected output
    squareRoot(14)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 224\n224  is the power of 2\nDecimal value of  224 is: \n011100000'


def test_squareRoot_output_for_zero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    squareRoot(0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_squareRoot_input_large(capsys) -> None:  # to check the output matches expected output
    squareRoot(154)
    out, err = capsys.readouterr()
    assert out == 'Number after swapping Nibbles through bytes: \n 169\n169  is the power of 2\nDecimal value of  224 is: \n010101001'


