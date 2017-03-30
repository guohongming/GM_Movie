__author__ = 'Guo'

import csv
import pymongo
from datetime import datetime

def main():

    client = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db = client['movie']
    # coll = db.movieinfo
    file_name = 'movie_aiqing.csv'
    n= 0
    with open(file_name,newline='')as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if row[0] == '':
                continue
            id = row[0]
            name = row[1]
            issue_year = row[2]
            img_url = row[3]
            director = row[4]
            screenwriter = row[5]
            stars = eval(row[6])
            types = eval(row[7])
            area = row[8]
            language = row[9]
            release_time = eval(row[10])
            duration = row[11]
            alternate_name = row[12]
            imdb_url = row[13]
            score = row[14]

            data = {
                'id':id,
                'name':name,
                'issue_year':issue_year,
                'img_url':img_url,
                'director':director,
                'screenwriter':screenwriter,
                'stars':stars,
                'types':types,
                'area':area,
                'language':language,
                'release_time':release_time,
                'duration':duration,
                'alternate_name':alternate_name,
                'imdb_url':imdb_url,
                'score':score
            }
            result = db.movieinfo.insert_one(data)
            print(n,result)
            n+= 1

if __name__ == '__main__':
    main()



'''

{
		"address": {
			"street": "2 Avenue",
			"zipcode": "10075",
			"building": "1480",
			"coord": [-73.9557413, 40.7720266]
		},
		"borough": "Manhattan",
		"cuisine": "Italian",
		"grades": [
			{
				"date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
				"grade": "A",
				"score": 11
			},
			{
				"date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
				"grade": "B",
				"score": 17
			}
		],
		"name": "Vella",
		"restaurant_id": "41704620"
	}
'''