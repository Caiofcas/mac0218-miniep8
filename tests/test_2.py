import pytest

import euclid_gcd


def test_real_numbers():
    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd(1.7, 11.123)

    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd(1, 11.123)

    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd(1.7, 11)


def test_strings():
    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd("1", "11")

    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd(1, "11")

    with pytest.raises(TypeError):
        euclid_gcd.euclid_gcd("1", 11)
