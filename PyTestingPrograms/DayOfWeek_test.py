import sys
from io import StringIO
from DayOfWeek import dayofweek, isDayRange


def test_dayofweek_output_for_allOne() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    dayofweek(1, 1, 1)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_dayofweek_output_for_allZero() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    dayofweek(0, 0, 0)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_dayofweek_output_for_largeInput() -> None:  # to check the output is printing or not
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    dayofweek(31, 12, 2020)
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())


def test_dayofweek_are_one(capsys) -> None:  # to check the output matches expected output
    dayofweek(1, 1, 1)
    out, err = capsys.readouterr()
    assert out == "The day is:  4\n"


def test_dayofweek_are_zero(capsys) -> None:  # to check the output matches expected output
    dayofweek(0, 0, 0)
    out, err = capsys.readouterr()
    assert out == "The day is:  2\n"


def test_dayofweek_are_largeNum(capsys) -> None:  # to check the output matches expected output
    dayofweek(31, 12, 2020)
    out, err = capsys.readouterr()
    assert out == "The day is:  3\n"


# def isDayRange(capsys) -> None:  # to check the output matches expected output
#     isDayRange(54)
#     # isDayRange.day = 54
#     out, err = capsys.readouterr()
#     assert out == "Entered day is not valid! Try day range(1-31)"
