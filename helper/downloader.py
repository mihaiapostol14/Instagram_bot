from icrawler.builtin import UrlListCrawler

class Downloader:

    def downloader(self, filename, dir_name=''):
        urllist_crawler = UrlListCrawler(downloader_threads=4,
                                         storage={'root_dir': dir_name})
        urllist_crawler.crawl(filename)