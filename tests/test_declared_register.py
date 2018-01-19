#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `declared_register` package."""
import pytest

from one_eight_two.classes.declared_register import DeclaredRegister

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_init_fields(response):
    register = DeclaredRegister()
    assert register.exercise == None
    assert register.register_type == "2"

def test_length_fields(response):
    register = DeclaredRegister()
    total_length = reduce((lambda x, y: x + y), list(map(lambda x: x["length"], register.fields_meta)))
    assert total_length == 250

def test_formatter_field(response):
    register = DeclaredRegister()
    assert register.get_formatted_field("blanks") == " " * 118

def test_length_representation(response):
    register = DeclaredRegister()
    assert len(register.get_representation()) == 250

def test_empty(response):
    register = DeclaredRegister()
    assert register.get_representation() == "2" + str(" "*249)
