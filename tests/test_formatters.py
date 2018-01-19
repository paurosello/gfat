"""Tests for `declared_register` package."""
import pytest

from utils import formatters


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_fill_spaces_formatter(response):
    assert formatters.fill_spaces("", {"length": 0}) == ""
    assert formatters.fill_spaces("", {"length": 1}) == " "
    assert formatters.fill_spaces("", {"length": 2}) == "  "
    assert formatters.fill_spaces("", {"length": 3}) == "   "

def test_fill_spaces_formatter_overflow(response):
    assert formatters.fill_spaces("aaaaaaa", {"length": 0}) == ""
    assert formatters.fill_spaces("aaaaaab", {"length": 1}) == "b"
    assert formatters.fill_spaces("aaaaabb", {"length": 2}) == "bb"
    assert formatters.fill_spaces("aaaabbb", {"length": 3}) == "bbb"

def test_fill_spaces_formatter_int(response):
    assert formatters.fill_spaces(1, {"length": 0}) == ""
    assert formatters.fill_spaces(1, {"length": 1}) == "1"
    assert formatters.fill_spaces(11,{"length": 2}) == "11"
    assert formatters.fill_spaces(1, {"length": 3}) == "  1"
