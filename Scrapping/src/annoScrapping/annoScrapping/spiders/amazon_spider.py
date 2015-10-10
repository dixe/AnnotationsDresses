import scrapy

class AmazoneSpider(scrapy.Spider):
    name = "amazon"
    allow_domains = ["http://www.amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=lp_1040660_ex_n_4?rh=n%3A7141123011%2Cn%3A10445813011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024&bbn=10445813011&ie=UTF8&qid=1444505262"
    ]

    def parse(self, response):
        followLinks = []

        sel = response.xpath("//div[contains(@id,'resultsCol')]")
        reses = sel.xpath(".//ul/li")
        i = 0
        for res in reses:
            indexes = len(res.xpath("./div/div/div/a/@href").extract())
            for j in range(indexes):
                link = res.xpath("./div/div/div/a/@href").extract()[j]
                if link.startswith("http"):
                    followLinks.append(link)
                    break

        # debuggin code kinda useful
        # with open("test.txt",'w') as f:
        #     f.write("\n".join(followLinks))
