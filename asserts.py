import pandas as pd


def create_data_frame(file_name: str) -> pd.core.frame.DataFrame:
    """Эта функция принимает в качестве аргумента название .csv файла и создает из него датафрейм."""
    original_df = pd.read_csv(file_name)
    nonduplicate_recipes = original_df[original_df.index < 31]
    return nonduplicate_recipes


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
