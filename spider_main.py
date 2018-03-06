
#-*-coding: utf-8 -*-
import url_manager, html_downloaded, html_parser, html_outputer
#from baike_spider import url_manager, html_downloaded, html_parser, html_outputer
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloaded.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 22:
                    break
                count = count + 1
            except:
                print 'craw failed'
                self.outputer.output_text()


if __name__=="__main__":
    root_url = "http://www.dytt8.net/html/gndy/jddy/20160320/50523.html"
    root_handers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)