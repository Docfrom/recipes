from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salat': {
        'помидор, шт': 1,
        'огурец, шт': 1,
        'редис, шт': 3,
        'оливковое масло, мл': 10,
    },
    'sirnik': {
      'творог, кг': 0.5,
      'яйцо, шт': 2,
      'мука, г': 150,
      'молоко, мл': 200
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def calc_recipe(request, recipe_slug):
    recipe = DATA.get(recipe_slug)
    servings = int(request.GET.get('servings', 1))
    calculated_recipe = {}
    for ingridient, amount in recipe.items():
        calculated_recipe[ingridient] = amount * servings
    context = {
        'recipe': calculated_recipe
    }
    return render(request, 'calculator/index.html', context)