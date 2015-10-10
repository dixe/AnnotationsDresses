import scrapy

class AmazoneSpider(scrapy.Spider):
    name = "amazon"
    allow_domains = ["http://www.amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=lp_1040660_ex_n_4?rh=n%3A7141123011%2Cn%3A10445813011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024&bbn=10445813011&ie=UTF8&qid=1444505262"
    ]

    def parse(self, response):
        filename = "Response.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
