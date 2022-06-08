import euclid_gcd

def test_return_correct_gcd():
    assert 1 == euclid_gcd.euclid_gcd(1, 11)
    assert 2 == euclid_gcd.euclid_gcd(2, 12)
    assert 10 == euclid_gcd.euclid_gcd(40, 70)
    assert 21 == euclid_gcd.euclid_gcd(1071, 462)
