import pytest
from calculator import ExpertCalculator


@pytest.mark.parametrize("expression, expected_result", [
    # 5 syntax errors
    ("3.3.3", "Invalid character: ."),
    ("3^*2", "not valid"),
    ("(2)2+", "you used ) in wrong way"),
    ("7++", "not valid"),
    ("()", "can not get empty parentheses"),
    # empty string
    ("", "you need to enter something"),
    # gibberish string
    ("hkefiue", "Invalid character: h"),
    # tabs and white spaces
    ("          3      + 8", 11),
    # checking all the operators
    ("5+4", 9),
    ("4-6", -2),
    ("15*2", 30),
    ("16/4", 4),
    ("9^2", 81),
    ("21%3", 0),
    ("76@34", 55),
    ("4&-35", -35),
    ("98$23", 98),
    ("5!", 120),
    ("~-92", 92),
    ("34.56#", 18),
    ("~--3!", "can not be factorized"),
    ("2--3!", "can not be factorized"),
    # complicated expressions
    ("4.2 + 2.8 * 7.5 % 3.1 + 10.3$(-2.7)", 18.14),
    ("~-4.9 + 2.1^3.3 - 5.8$(-2.6) + 7.2 & 3.4", 14.069741950241463),
    ("((5!-2&-1)#+~-3.2%1.5*7)/4", 1.3500000000000003),
    ("3-2^4.5+(7!#/48)#-~3*100", 301.37258300203047),
    ("951#/73+~---3*(2-(8&3)$(7&2))", -2.7945205479452055),
    ("2*6$4%(3^2) + 7! + ~(8&2) + 5$(6&3)", 5055),
    ("~(7&4) + 5!-(2^8)## - 9*(6$3) + 8%(1@2)", 58.5),
    ("~(9&(4$6)@2) ---- 3*8%(7^1) + 5!#", 2),
    ("6*7$8%(5^4) - 2! + ~(3&(9$2)@1)", 44),
    ("1! - 2%(3^(6&5))## + 7$(4&8)@9 + ~3", 4),
    ("8.5*(6$4)%(3.4^2) + ~-7! - (8&2) + 5$(6&3)", 5094),
    ("~(9.7&(4.1$6.8)@2.3) - 3.6*8.2%(7.1^1.5) + 5!", 85.93),
    ("60.4*7.3$8.9%(5.2^4.6)# + ~(3.9&(9.8$2.7)@1.6)", 534.8100000000001),
    ("3.6 + 4!@1.8 - ~2.3*(8.5$7.1)#%(5.6^6.3) + 9.2", 55.599999999999994),
    ("~5.3 --- 6.8^3.5%2.1# + 4! --- 7.4$(8.1&1.6)@9.2", 7.79231903791894),
    ("6.4*7.3$8.9%(5.2#^4.6) + ~(3.9#&(9.8$2.7)@1.6)", 51.260000000000005),
    ("~(5.6&4.7) + 3!*(2.2^1.8) - 8.5#*(6.1$2.3) + 7.4%(1.9@2.6)", -58.54655095530779),
    ("~7.3 --9.2$(8.1&1.4)@5.9 + 3.8", -7.1499999999999995)
])
def test_calculate(expression, expected_result, monkeypatch):
    """
    tests the calculator for a variety of situations
    :param expression: the expression that the calculator gets
    :param expected_result: what i suppose to get
    :param monkeypatch: feature that simulate the input
    :return: if the calculator returned what i expected
    """
    calculator = ExpertCalculator()
    monkeypatch.setattr('builtins.input', lambda _: expression)
    assert calculator.calculate() == expected_result
