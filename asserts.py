def rework_time_to_minutes(time_string: str) -> int:
    """Функция, которая преобразовывает строку формата "% hrs % mins" в целочисленное значение минут, вычисленное для этой строки"""
    time_string = str(time_string)
    total_minutes = 0 
    time_list = time_string.split()
    if 'hrs' in time_string and 'mins' in time_string:
        total_minutes = int(time_list[0]) * 60 + int(time_list[2])
    elif 'hrs' in time_string:
        total_minutes = int(time_list[0]) * 60
    elif 'mins' in time_string:
        total_minutes = int(time_list[0])
    return total_minutes


assert rework_time_to_minutes('random word') == 0
assert rework_time_to_minutes('random word else shit') == 0
assert rework_time_to_minutes(' ') == 0
assert rework_time_to_minutes(nonduplicate_recipes.total_time[1]) == 90
assert rework_time_to_minutes(nonduplicate_recipes.total_time[0]) == 0
assert rework_time_to_minutes('0 hrs 0 mins') == 0
assert rework_time_to_minutes('7 hrs 15 mins') == 435
assert rework_time_to_minutes('7 hrs') == 420
assert rework_time_to_minutes('15 mins') == 15