from code_challenges.roman_numerals import roman_to_arabic

def test_function_exists():
  assert roman_to_arabic

def test_one():
    num = 'I'
    actual = roman_to_arabic(num)
    expected = 1
    assert actual == expected


def test_two():
    num = 'II'
    actual = roman_to_arabic(num)
    expected = 2
    assert actual == expected


def test_four():
    num = 'IV'
    actual = roman_to_arabic(num)
    expected = 4
    assert actual == expected


def test_fifty():
    num = 'XXL'
    actual = roman_to_arabic(num)
    expected = 50
    assert actual == expected


def test_seven():
    num = 'VII'
    actual = roman_to_arabic(num)
    expected = 7
    assert actual == expected


def test_ten():
    num = 'X'
    actual = roman_to_arabic(num)
    expected = 10
    assert actual == expected


def test_155():
    num = 'CXXLV'
    actual = roman_to_arabic(num)
    expected = 155
    assert actual == expected


def test_1984():
    num = 'MCMLXXXIV'
    actual = roman_to_arabic(num)
    expected = 1984
    assert actual == expected


def test_eighty():
    num = 'LXXX'
    actual = roman_to_arabic(num)
    expected = 80
    assert actual == expected
