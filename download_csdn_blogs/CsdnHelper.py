#coding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import re
from DBHelper import DBHelper


class CsdnHelper:
    """login CSDN"""
    csdn_login_url = "https://passport.csdn.net/account/login?ref=toolbar"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    blog_url = "http://write.blog.csdn.net/postlist/"

    def __init__(self):
        self._session = requests.session()
        self._headers = CsdnHelper.headers

    def login(self, username, password):
        """login main function"""
        form_data = self._prepare_login_form_data(username, password)
        response = self._session.post(CsdnHelper.csdn_login_url, data=form_data)
        #valid = False
        if 'UserNick' in response.cookies:
            nick = response.cookies['UserNick']
            print("Login succeed")
            print(urllib.unquote(nick))
            return True
        else:
            print("Login failed, invalid username or password")
            return False

    def _prepare_login_form_data(self, username, password):
        """Get data for login submission"""
        response = self._session.get(CsdnHelper.csdn_login_url)
        login_page = BeautifulSoup(response.text, "lxml")
        login_form = login_page.find('form', id='fm1')

        lt = login_form.find('input', attrs={'name': 'lt'})['value']
        execution = login_form.find('input', attrs={'name': 'execution'})['value']
        eventId = login_form.find('input', attrs={'name': '_eventId'})['value']

        form = {
            "username": username,
            "password": password,
            "lt": lt,
            "execution": execution,
            "_eventId": eventId
        }

        return form

    def _get_blog_count(self):
        """Get total counts of blog"""
        response = self._session.get(CsdnHelper.blog_url)
        blog_page = BeautifulSoup(response.text, 'lxml')
        span = blog_page.find('div', class_='page_nav').span
        print(span)
        a = span.string
        pattern = re.compile(u'(\s*\d+)条\s*共(\s*\d+)页')
        result = pattern.findall(a)
        blog_count = int((result[0][0]).strip())
        page_count = int((result[0][1]).strip())
        print("Total count is : ", blog_count," , splitted into pages ",page_count)
        return (blog_count, page_count)

    def readArticles(self):
        """Get article"""
        blog_count, page_count = self._get_blog_count()
        for index in range(1, page_count + 1):
            url = 'http://write.blog.csdn.net/postlist/0/0/enabled/' + str(index)
            print(url)
            response = self._session.get(url)
            page = BeautifulSoup(response.text, 'lxml')
            links = page.find_all('a', href=re.compile(r'http://blog.csdn.net/flsmgf/article/details/(\d+)'))
            for link in links:

                blog_name = link.string
                blog_url = link['href']
                # print(blog_name +","+ blog_url)
                db = DBHelper()
                db.insertArticles(blog_name, blog_url, 1, 1)

if __name__ == '__main__':
    csdn_helper = CsdnHelper()
    username = raw_input("Input the username:")
    password = raw_input("Input the password:")
    if csdn_helper.login(username, password):
        csdn_helper.readArticles()
    else:
        print("Login failed, denied for the former steps!")
