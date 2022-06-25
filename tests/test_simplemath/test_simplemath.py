from src.simplemath import simplemath


def test_we_can_add_two_numbers():
    assert simplemath.add(5,12) == 17

def test_we_can_calculate_the_number_to_the_power_of_another_numbers():
    assert simplemath.power_of(5,12) == 244140625

def test_we_can_subtract_two_numbers():
    assert simplemath.substract(5,12) == -7

def test_we_can_multiply_two_numbers():
    assert simplemath.multiply(5,12) == 60

def test_we_can_divide_two_numbers():
    assert simplemath.divide(5,12) == 0.4166666666666667