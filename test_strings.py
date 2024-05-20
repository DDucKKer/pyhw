import pytest
from string_with_while import filter_string
from string_with_while import calculate_distance


strings = [
    ("", []),
    ("abcdef", ['a', 'b', 'c', 'd', 'e', 'f']),
    ("mnMNmn", []),
    ("aMnBnmC", ['a', 'B', 'C']),
    ("a" * 101, ["a"] * 100),
    ("a" * 50 + "mn" * 50 + "b" * 50, ["a"] * 50 + ["b"] * 50),
    ("123!@#mnMN", ['1', '2', '3', '!', '@', '#']),
]


@pytest.mark.parametrize('input_string, expected', strings)
def test_cold(input_string, expected):
    assert filter_string(input_string) == expected


distance_strings = [
    (10, 3, 1000, "Транспортний засіб вагою 1000 кг рухався 10 секунд зі швидкістю 3м/сек, і подолав відстань 30 метрів")
]

@pytest.mark.parametrize('time, speed, weight, expected', distance_strings)
def test_calculate_distance(time, speed, weight, expected):
    assert calculate_distance(time=time, speed=speed, weight=weight) == expected


@pytest.mark.parametrize("time, speed, weight", [
    (-1, 3, 1000),
    (10, -3, 1000),
    (10, 3, -1000),
])
def test_calculate_distance_raises_value_error(time, speed, weight):
    with pytest.raises(ValueError, match="Час, швидкість і вага повинні бути не менше 0!"):
        calculate_distance(time=time, speed=speed, weight=weight)
