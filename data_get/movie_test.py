__author__ = 'Guo'

from spider import Spider
from select_data import SelectData
import csv

def get_urls():
    return

def write_file(filename,data):
    with open(filename, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(data)


def main():
    for i in range(37,100):
        print('正在抓取第',i+1,'页...')
        url= 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start='+str(i*20)+'&type=T'
    # url= 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=0&type=T'
        spider_1 = Spider()
        html,id = spider_1.get_html_from(url)           # 获取链接
        select_1 = SelectData(html)
        urls = select_1.select_urls()
        count = 0
        for link in urls:
            spider_a = Spider()
            html_a,id_a = spider_a.get_html_from(link)           # 获取电影内容
            select_data_a = SelectData(html_a,id_a)
            try:
                result = select_data_a.select_content()
            except:
                result = []
            # print(type(result))
            # print(result)
            if result!= []:
                print('success',count)
            write_file('movie_aiqing.csv',result)
            count +=1

if __name__ == '__main__':
    main()