__author__ = 'Guo'
import pandas as pd
import time
# import redis
from flask import current_app
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def train():
    ds = pd.read_csv('sample-data.csv')
    print(ds)
    return 1

    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    # print(tf)
    tfidf_matrix = tf.fit_transform(ds['description'])
    print(tfidf_matrix)
    cosine_similarities = linear_kernel(tfidf_matrix,tfidf_matrix)
    for idx, row in ds.iterrows():
        simlar_indices = cosine_similarities[idx].argsort()[:-20:-1]
        simlar_items = [(cosine_similarities[idx][i],ds['id'][i]) for i in simlar_indices]
        flattened = sum(simlar_items[1:],())
        print(flattened)
        print(row['id'])




if __name__ == '__main__':
    train()




