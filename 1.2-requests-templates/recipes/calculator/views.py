from django.http import HttpResponse
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
    # можете добавить свои рецепты ;)
}


def home(request):
    # template_name = 'calculator/index.html'
    # return render(request, template_name)
    return


def recipe(request, food):
    servings = request.GET.get('servings', 1)
    print(servings)
    # if food:
    #     content = DATA[food]
    context = {
        'recipe': DATA[food],
        'servings': int(servings),
        'multiplied_amounts': {ingredient: amount * servings for ingredient, amount in DATA[food].items()}
    }
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
#     context = {
#       'recipe': {
#         'ингредиент1': 1,
#         'ингредиент2': 2,
#       }
#     }
#     return render(request, context)