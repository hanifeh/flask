from . import app, models


@app.route('/')
def show_all():
    return 'hello'


@app.route('/food/create')
def food_create():
    food_instance = models.Food(
        name='pizza',
        region=['italy'],
    )
    food_instance.save()
    return food_instance.to_json(), 201
