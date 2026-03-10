import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("english", "English"),
    ("checking a long phrase many words", "Checking a long phrase many words"),
    ("пишем на кириллице", "Пишем на кириллице"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("$inserting a special character", "$inserting a special character"),
    (" we put a space at the begining", " we put a space at the begining")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" English", "English"),
    (" Пишем на кириллице", "Пишем на кириллице"),
    ("     Много пробелов", "Много пробелов"),
    ("No space", "No space")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("Space after end str    ", "Space after end str    "),
    ("       ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected_bool", [
    ("English", "E", True),
    ("Russian", "C", False),
    ("345", "4", True),
    ("@#$", "#$", True)
])
def test_contains_positive(input_str, symbol, expected_bool):
    assert string_utils.contains(input_str, symbol) == expected_bool


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_bool", [
    ("Register", "I", False),
    ("Rev", "r", False),
    ("Space", " ", False),
    ("", "a", False),
    ("   ", "&", False)
])
def test_contains_negative(input_str, symbol, expected_bool):
    assert string_utils.contains(input_str, symbol) == expected_bool


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Beard", "d", "Bear"),
    ("Kenwood", "Ken", "wood"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hurdy Gurdy", "", "Hurdy Gurdy"),
    ("7568", "G", None),
    ("Forest", " ", None)
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
