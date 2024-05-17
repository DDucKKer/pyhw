from age_checker import check_age


def test_one_check_age():
    expected_result = "Передано не валідне значення віку!"
    age = -5
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_two_check_age():
    expected_result = "Ти дитина!"
    age = 10
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_three_check_age():
    expected_result = "Потрібно працювати!"
    age = 30
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_four_check_age():
    expected_result = "Щасливої пенсії!"
    age = 70
    actual_result = check_age(age)
    assert actual_result == expected_result
