import pandas as pd
import json
import matplotlib.pyplot as plt


def create_data_frame(file_name: str) -> pd.core.frame.DataFrame:
  """Эта функция принимает в качестве аргумента название .csv файла и создает из него датафрейм."""
  original_df = pd.read_csv(file_name)
  nonduplicate_recipes = original_df[original_df.index < 31]
  return nonduplicate_recipes


def rework_time_to_minutes(time_string: str) -> int:
  """Функция, которая преобразовывает строку формата "% hrs % mins" в целочисленное значение минут, вычисленное для этой строки.
  Наример, '3 hrs 15 mins' будет == 195. При вводе строки неправильного формата вернет 0."""
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


def get_recipes_with_chicken(data_frame: pd.core.frame.DataFrame) -> list:
  """Функция для поиска рецептов (recipe), в которых используется курица (chicken) в качестве ингридиента (ingredients).
  В качестве аргумента принимает датафрейм, который необходимо обработать. 
  Возвращает список названий рецептов, в которых используется курица (chicken) в качестве ингридиента (ingredients)."""
  all_recipes = list(data_frame.ingredients)
  recipes_with_chicken = []
  for i in range(len(all_recipes)):
    if 'chicken' in all_recipes[i]:
      recipes_with_chicken.append(data_frame.recipe_name[i])
  return recipes_with_chicken


def get_longest_time_recipes(data_frame: pd.core.frame.DataFrame) -> list:
  """Функция для поиска трех рецептов (recipe), время приготовления (total_time) которых самое долгое.
  В качестве аргумента принимает датафрейм, который необходимо обработать. 
  Возвращает список названий рецептов, время приготовления которых самое долгое"""
  total_time_list = list(data_frame.total_time)
  time_in_minutes_list = []
  for e in total_time_list:
    time_in_minutes_list.append(rework_time_to_minutes(e))
  sorted_time_in_minutes_list = sorted(time_in_minutes_list, reverse=True)
  longest_recipes = []
  for i in range(3):
    longest_recipes.append(data_frame.recipe_name[time_in_minutes_list.index(sorted_time_in_minutes_list[i])])
  return longest_recipes


def get_recipes_for_servings(data_frame: pd.core.frame.DataFrame) -> dict:
  """Данная функция выводит названия блюд (recipe), которые можно приготовить на каждое количество человек (servings).
  В качестве аргумента принимает датафрейм, который необходимо обработать. 
  Возвращает словарь, в котором ключами являются количество персон, на которые можно приготовить блюда, 
  а значениями - блюда на это количество персон."""
  unique_servings_list = sorted(list(data_frame.servings.unique()))
  recipes_for_each_servings = dict()
  for e in unique_servings_list:
    recipes_for_one_number = data_frame[data_frame.servings == e]
    recipe_names_for_dict = list(recipes_for_one_number.recipe_name)
    recipes_for_each_servings[int(e)] = recipe_names_for_dict
  return recipes_for_each_servings


def save_answers_to_json_file(data_frame: pd.core.frame.DataFrame):
  """Данная функция сохраняет ответы, полученные в трех предыдущих функция в .json файле.
  В качестве аргумента принимает датафрейм, который необходимо обработать."""
  answer = {
    'Recipes with chicken as ingredient' : get_recipes_with_chicken(data_frame),
    'Three recipes with longest time taken to bake' : get_longest_time_recipes(data_frame),
    'Recipes for each number of servings': get_recipes_for_servings(data_frame)
  }

  with open("answers.json", "w") as json_file:
      json.dump(answer, json_file, indent=2)


def make_ratings_histograme(data_frame: pd.core.frame.DataFrame):
  """Данная функция создает гистограмму рейтинга блюд на основе данных из датафрейма.
  В качестве аргумента принимает датафрейм, который необходимо обработать."""
  ratings = data_frame.rating
  plt.title('Rating of recipes')
  plt.xlabel('Rating')
  plt.ylabel('Number of recipes')
  plt.hist(ratings, bins=30, color='green')
  plt.savefig('rating_of_recipes.png')


def main():
  """Функция, которая необходима для запуска остальных функций в пределах данного файла."""
  actual_data_frame = create_data_frame('recipes_100.csv')
  get_recipes_with_chicken(actual_data_frame)
  get_longest_time_recipes(actual_data_frame)
  get_recipes_for_servings(actual_data_frame)
  save_answers_to_json_file(actual_data_frame)
  make_ratings_histograme(actual_data_frame)


main()