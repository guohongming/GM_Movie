from flask import Flask, render_template, request
from models import database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my name is blank guo'
db = database.DataBase()


# 首页
@app.route('/')
def index():
    data, key = db.get_index_data()
    # print(info6s_from_db[0])
    return render_template('index.html', data_movies_6=data, key_index=key)


# 单个电影信息
@app.route('/subject/<this_id>')
def item(this_id):
    item_info = db.get_iterm_data(this_id)
    return render_template('item.html', item=item_info)


# 搜索
@app.route('/search', methods={'POST'})
def search():
    key = request.form['data']
    info_all = db.search_from_key_name(key)

    return render_template('search.html', key=key, search_data=info_all)


# 分类/分页
@app.route('/tag/<this_tag>', methods={'GET'})
def classify(this_tag):
    skip = request.args.get('skip')
    limit = request.args.get('limit')
    if int(skip) < 0:
        skip = 0
    data = db.classify_data_from_tag(this_tag, skip, 10)
    # print(data)
    pre_skip = int(skip)-10
    next_skip = int(skip)+10
    return render_template('classify.html', classify_data=data, the_tag=this_tag, the_skip=skip, the_limit=10,
                           Previous=pre_skip, next=next_skip)


if __name__ == "__main__":

    app.run(debug=True)
