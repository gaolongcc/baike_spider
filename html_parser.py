
#-*-coding: utf-8 -*-
from bs4 import  BeautifulSoup
import re
import urlparse

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # <a href="http://www.ygdy8.com/html/gndy/dyzz/20170422/53803.html">
        links = soup.find_all('a', href=re.compile(r"http://www.ygdy8.com/html/gndy/dyzz/")) #/i/\d+\.html
        for link in links:
            new_url = link['href']
            #new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url
        #
        name_node = soup.find('div', class_="title_all").find('font', attrs={'color': '#07519a'})#.find('h1')
        res_data['movie_name'] = name_node.get_text()
        #改变节点值，得到目标的下载地址
        address_node = soup.find('td', attrs={'style': 'WORD-WRAP: break-word'}).find('a')
        res_data['address'] = address_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
