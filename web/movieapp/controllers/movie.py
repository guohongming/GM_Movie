from flask import Flask, render_template, request
from flask import Blueprint, redirect, url_for
from movieapp.models import myjinjafilter, database


movie_blueprint = Blueprint(
    'movie',
    __name__,
    template_folder='./templates'
)

db = database.DataBase()


# 首页
@movie_blueprint.route('/')
def index():
    data, key = db.get_index_data()
    # print(info6s_from_db[0])
    return render_template('index.html', data_movies_6=data, key_index=key)


# 单个电影信息

@movie_blueprint.route('/subject/<this_id>')
def item(this_id):
    item_info = db.get_iterm_data(this_id)
    return render_template('item.html', item=item_info)


# 搜索
@movie_blueprint.route('/search', methods={'POST'})
def search():
    key = request.form['data']
    info_all = db.search_from_key_name(key)

    return render_template('search.html', key=key, search_data=info_all)


# 分类/分页
@movie_blueprint.route('/tag/<this_tag>', methods={'GET'})
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


@movie_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404





