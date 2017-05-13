__author__ = 'Guo'
__author__ = 'Guo'
import pandas as pd
import time
# import redis
import csv
from flask import current_app
import pymongo
from movieapp.models import database
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

db = database.DataBase()

def train():
    ds = pd.read_csv('test2.csv')
    # print(ds)
    #print(ds['description'])
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    # print(tf)
    tfidf_matrix = tf.fit_transform(ds['description'])

    cosine_similarities = linear_kernel(tfidf_matrix,tfidf_matrix)

    for idx, row in ds.iterrows():
        simlar_indices = cosine_similarities[idx].argsort()[:-30:-1]
        simlar_items = [(cosine_similarities[idx][i],ds['id'][i]) for i in simlar_indices]
        flattened = sum(simlar_items[1:],())
        print(simlar_items)
        relation = []
        for item in simlar_items:
            item_copy = str(item[1])
            relation.append(item_copy)

        print(relation)
        # print(str(row['id']))
        data = {
            'id': str(row['id']),
            'relation': relation
        }
        print(type(data))
        db.write_movie_relation(data)


def write_file(filename,data):
    with open(filename, 'a',encoding='utf-8', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(data)


def set_title():
    write_file('test2.csv',['id','description'])


def get_data():

    with open('movie_aiqing.csv', 'r') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if row[0]=='':
                continue
            line = []
            desc =str(row[1]+row[4]+row[7]+row[14]+row[6])
            '''
            print(row[6])
            if row[6]==[]:
                desc = '空'
            else:
                desc = ' '.join(eval(row[6]))
            print(desc)
            desc = str("'"+desc + "'")
            '''
            #desc = desc.replace('[', ' ')
            #desc = desc.replace(']', ' ')
            #print(desc)
            line.extend((row[0],desc))
            write_file('test2.csv', line)


if __name__ == '__main__':
    #set_title()
    #get_data()
    train()



