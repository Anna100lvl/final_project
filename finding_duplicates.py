import pandas as pd


#Этот код позволять получить только неповторяющиеся рецепты. В 'recipes_100.csv' повторы начинаются после рецепта с индексом 30, так что было принято решение обрезать оригинальный файл до этого индекса, чтобы получить только неповторяющиеся рецепты.
df = pd.read_csv('recipes_100.csv')
recipes = df.recipe_name
nondups = recipes.drop_duplicates(keep='first')
print(nondups)
