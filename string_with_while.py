from typing import List


def filter_string(input_string: str) -> List[str]:
    result = []
    index = 0
    count = 0
    max_length = 100
    while index < len(input_string) and count < max_length:
        char = input_string[index]
        if char.lower() not in ['m', 'n']:
            result.append(char)
            count += 1
        index += 1
    return result


def calculate_distance(*, time: int, speed: int, weight: int) -> str:
    if time <= 0 or speed <= 0 or weight <= 0:
        raise ValueError("Час, швидкість і вага повинні бути не менше 0!")

    distance = speed*time
    return f"Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, і подолав відстань {distance} метрів"
