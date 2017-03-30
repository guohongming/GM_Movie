__author__ = 'Guo'

# coding: utf-8
from bs4 import BeautifulSoup
import re
from lxml import etree

class SelectData(object):

    def __init__(self,html='', id = '' ):
        self.__html = html
        self.__id = id

    # 取链接
    def select_urls(self):
        bs = BeautifulSoup(self.__html)
        urls_bs = bs.find_all('table', {'width':"100%", 'class':""})
        urls = []
        for url_b in urls_bs:
            urls.append(url_b.a['href'])
        return urls


    def select_content(self):
        bs = BeautifulSoup(self.__html)

        result = []

        wrapper_bs = bs.find('div',{'id':'wrapper'})
        # print(wrapper_bs)
        # 获取名字和年份
        try:
            titles = wrapper_bs.find('h1').find_all('span')
            title_name = titles[0].get_text()
            title_year = titles[1].get_text()
        except:
            title_name = wrapper_bs.find('h1').span.get_text()
            title_year = None
        # print(title_name,title_year)


        article_bs = wrapper_bs.find('div',{'class':'article'})
        # print(article_bs)
        subject_wrapper_bs = article_bs.find('div',{ 'class':"subjectwrap clearfix"}) #图片，info，评分
        subject_bs = subject_wrapper_bs.find('div',{ 'class':"subject clearfix"})
        # 图片链接
        try:
            pic_bs = subject_bs.find('a', {'class':"nbgnbg"}).img
            pic_url = pic_bs['src']   # 图片的链接
        except:
            pic_url = None


        info_bs = subject_bs.find('div',{'id':'info'})
        # print(info_bs)
        directedBy_names = info_bs.find_all('span',{'class':'attrs'})

        # 导演,编剧，主演
        try:
            directer_name = directedBy_names[0].a.get_text()
        # print(directer_name)
        except:
            directer_name = None

        try:
            maker_name = directedBy_names[1].a.get_text()
        except:
            maker_name = None
        # print(maker_name)
        try:

            actors_bs = directedBy_names[2].find_all('a')
            act_names =[]
            for ac in actors_bs:
                name = ac.get_text()
                act_names.append(name)
        except:
            act_names= []
        # print(act_names)

        # 类型
        kinds_bs = info_bs.find_all('span',{ 'property':"v:genre"})
        # print(kinds_bs)
        kinds_name = []
        for kind in kinds_bs:
            kinds_name.append(kind.get_text())
        # print(kinds_name)

        # 地区
        try:
            area_name_bs  = kinds_bs[-1]. find_next_sibling().find_next_sibling()
            area_name = area_name_bs.next_sibling
            area_name = str(area_name)
        except:
            area_name = None
        #　print(area_name)


        # 语言
        language_bs = area_name_bs.find_next_sibling().find_next_sibling()
        language = language_bs.next_sibling
        language = str(language)
        # print(language)

        # 日期
        release_date_bs = info_bs.find_all('span',{ 'property':"v:initialReleaseDate"})
        release_date = []
        for date in release_date_bs:
            release_date.append(date.get_text())

        # print(release_date)


        # runtime
        try:
            run_time_bs = info_bs.find('span',{'property':"v:runtime"})
            runtime = run_time_bs.get_text()
        except:
            runtime = None
        # print(runtime)


        # 又名
        try:
            other_name_bs = run_time_bs.find_next_sibling().find_next_sibling()
            other_name = str(other_name_bs.next_sibling)
        except:
            other_name = None
        # print(other_name)

        # imdb
        try:
            imdb_url_bs = info_bs.find('a',{'rel':'nofollow'})
            imdb_url = imdb_url_bs['href']
        except:
            imdb_url = None
        # print(imdb_url)


        # 评分
        score_bs = subject_wrapper_bs.find('div',{'id':'interest_sectl'})
        score = score_bs.find('strong',{'class':'ll rating_num'}).get_text()
        # print(score)

        result.extend((self.__id,title_name,title_year,pic_url,directer_name,maker_name,act_names,kinds_name,area_name,language,release_date,runtime,other_name,imdb_url,score))
        return result


if __name__ == '__main__':
    pass


