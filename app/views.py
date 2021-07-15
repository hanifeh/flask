from flask_pymongo import PyMongo

from . import app

app.config['MONGO_URI'] = 'mongodb://maktab:123456@localhost:27017/maktab?authSource=admin'
mongo = PyMongo(app)


@app.route('/all')
def show_all():
    all_docs = mongo.db.flask.find()
    print(all_docs)
    return all_docs[0]['name']
