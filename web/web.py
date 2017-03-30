from flask import Flask, render_template, url_for
from models import  database


app = Flask(__name__)

db = database.DataBase()


@app.route('/')
def index():
    data,key  = db.get_index_data()
    # print(info6s_from_db[0])
    return render_template('index.html',data_movies_6 = data, key_index = key)


@app.route('/subject/<this_id>')
def item(this_id):
    item_info, item_stars = db.get_iterm_data(this_id)
    return render_template('item.html',item = item_info,itemstarsto5 = item_stars)


@app.route('/tag/<this_tag>')
def classify(this_tag):

    return render_template('classify.html',the_tag = this_tag)


if __name__ == "__main__":

    app.run(debug = True)
