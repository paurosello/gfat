#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `declared_register` package."""
import pytest

from one_eight_two.classes.declarant import Declarant
from one_eight_two.classes.declared_register import DeclaredRegister

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_length_fields(response):
    register = Declarant()
    total_length = reduce((lambda x, y: x + y), list(map(lambda x: x["length"], register.fields_meta)))
    assert total_length == 250
