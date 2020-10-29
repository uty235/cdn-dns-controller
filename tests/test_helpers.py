import unittest
import pytest
from context import Helper


@pytest.mark.parametrize('digit', [
	13,
	15,
	18,
	0,
	1
])
def test_random_string_generation(digit):
	helpers = Helper()
	result = helpers.get_random_string(length=digit)

	assert len(result) == digit
