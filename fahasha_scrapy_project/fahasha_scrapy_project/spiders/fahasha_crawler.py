import scrapy
from urllib.parse import urlencode

API_KEY = '48d206e607f0b84bf1206aedd3e03df3'


def get_scraperapi_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class FahashaCrawlerSpider(scrapy.Spider):
    name = "fahasha_crawler"
    # allowed_domains = ["www.fahasa.com"]
    # start_urls = ["https://www.fahasa.com/sach-trong-nuoc.html"]
    # banned = ["lam-vuon-thu-y", "bao-tap-chi", "the-duc-the-thao-giai-tri", "phong-thuy-kinh-dich",
    #           "van-hoa-nghe-thuat-du-lich", "dam-y"]
    # start_page = {'thieu-nhi': 0, 'giao-khoa-tham-khao': 0, 'van-hoc-trong-nuoc': 0, 'tam-ly-ky-nang-song': 0,
    #               'kinh-te-chinh-tri-phap-ly': 45, 'khoa-hoc-ky-thuat': 32, 'nuoi-day-con': 27,
    #               'lich-su-dia-ly-ton-giao': 30, 'chinh-tri-phap-ly-triet-hoc': 16, 'nu-cong-gia-chanh': 10,
    #               'tieu-su-hoi-ky': 13, 'am-nhac-my-thuat-thoi-trang': 3, 'van-hoa-nghe-thuat-du-lich': 9}

    def start_requests(self):
        # category_list = ["thieu-nhi", "giao-khoa-tham-khao", "van-hoc-trong-nuoc", "tam-ly-ky-nang-song"]
        # category_list = ["kinh-te-chinh-tri-phap-ly", "khoa-hoc-ky-thuat", "nuoi-day-con", "chinh-tri-phap-ly-triet-hoc"]
        # category_list = ["tieu-su-hoi-ky", "nu-cong-gia-chanh", "am-nhac-my-thuat-thoi-trang",
        #                  "van-hoa-nghe-thuat-du-lich", "lich-su-dia-ly-ton-giao"]
        # for category in category_list:
        #     link = f'https://www.fahasa.com/sach-trong-nuoc/{category}.html?p=1'
        #     yield scrapy.Request(url=get_scraperapi_url(link), callback=self.discover_book_urls,
        #                          meta={'category': category, "page": 1})

        links = ['https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=71', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=64', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=61', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=57', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=52', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=45', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=39', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=38', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=36', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=34', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=33', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=32', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=31', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=23', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=22', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=19', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=18', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=17', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=15', 'https://www.fahasa.com/sach-trong-nuoc/thieu-nhi.html?p=8', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=53', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=43', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=42', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=41', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=40', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=38', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=37', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=33', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=32', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=31', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=30', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=28', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=27', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=24', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=23', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=22', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=21', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=19', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=13', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=10', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=7', 'https://www.fahasa.com/sach-trong-nuoc/giao-khoa-tham-khao.html?p=5', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=45', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=43', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=42', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=37', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=36', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=32', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=31', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=29', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=28', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=22', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=17', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=18', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=12', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=11', 'https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?p=4', 'https://www.fahasa.com/sach-trong-nuoc/tam-ly-ky-nang-song.html?p=30', 'https://www.fahasa.com/sach-trong-nuoc/tam-ly-ky-nang-song.html?p=29', 'https://www.fahasa.com/sach-trong-nuoc/tam-ly-ky-nang-song.html?p=27', 'https://www.fahasa.com/sach-trong-nuoc/tam-ly-ky-nang-song.html?p=18', 'https://www.fahasa.com/sach-trong-nuoc/tieu-su-hoi-ky.html?p=3', 'https://www.fahasa.com/sach-trong-nuoc/tieu-su-hoi-ky.html?p=10', 'https://www.fahasa.com/sach-trong-nuoc/nu-cong-gia-chanh.html?p=8', 'https://www.fahasa.com/sach-trong-nuoc/nu-cong-gia-chanh.html?p=3', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=34', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=31', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=26', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=19', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=18', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=17', 'https://www.fahasa.com/sach-trong-nuoc/lich-su-dia-ly-ton-giao.html?p=16', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=43', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=39', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=36', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=28', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=17', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=15', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=14', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=11', 'https://www.fahasa.com/sach-trong-nuoc/kinh-te-chinh-tri-phap-ly.html?p=10', 'https://www.fahasa.com/sach-trong-nuoc/khoa-hoc-ky-thuat.html?p=29', 'https://www.fahasa.com/sach-trong-nuoc/khoa-hoc-ky-thuat.html?p=28', 'https://www.fahasa.com/sach-trong-nuoc/khoa-hoc-ky-thuat.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/khoa-hoc-ky-thuat.html?p=21', 'https://www.fahasa.com/sach-trong-nuoc/khoa-hoc-ky-thuat.html?p=19', 'https://www.fahasa.com/sach-trong-nuoc/nuoi-day-con.html?p=25', 'https://www.fahasa.com/sach-trong-nuoc/nuoi-day-con.html?p=16', 'https://www.fahasa.com/sach-trong-nuoc/nuoi-day-con.html?p=4', 'https://www.fahasa.com/sach-trong-nuoc/chinh-tri-phap-ly-triet-hoc.html?p=6', 'https://www.fahasa.com/sach-trong-nuoc/chinh-tri-phap-ly-triet-hoc.html?p=8']

        for link in links:
            s = link.replace('https://www.fahasa.com/sach-trong-nuoc/', '').replace('.html?p=', ' ')
            category = s.split()[0]
            page = s.split()[1]
            yield scrapy.Request(url=get_scraperapi_url(link), callback=self.discover_book_urls,
                                 meta={'category': category, "page": page})

    # def parse(self, response):
    #     category_list = response.css("ol.m-child-category-list li a::attr(href)").extract()
    #     self.log("i am crawling home link")
    #     for category_link in category_list[0:1]:
    #         category = category_link.split("/")[-1].replace(".html", '')
    #         yield scrapy.Request(url=category_link, callback=self.discover_book_urls, meta={'category': category, "page": 1})


    def discover_book_urls(self, response):
        main_ca = response.meta['category']
        page = response.meta['page']
        self.log(f"i am crawling book list link at page {page}")
        book_url_list = response.css("h2.product-name-no-ellipsis a::attr(href)").extract()
        for idx, book_url in enumerate(book_url_list):
            if "series" not in book_url and "combo" not in book_url:
                yield scrapy.Request(url=book_url, callback=self.parse_book, meta={'category': main_ca,
                                                                                   'page': page,
                                                                                   'order': idx})
    #
    #     if page == 1:
    #         available_page = response.css('div#pagination.pages ol li a::text').extract()
    #         last_page = available_page[-1]
    #         for page_num in range(2, int(last_page) if int(last_page) <= 100 else 100):
    #             search_url = f'https://www.fahasa.com/sach-trong-nuoc/{main_ca}.html?p={page_num}'
    #             yield scrapy.Request(url=get_scraperapi_url(search_url), callback=self.discover_book_urls,
    #                                  meta={'category': main_ca, 'page': page_num})


    def parse_book(self, response):
        # self.log("i am crawling book")
        book_id = response.css("tbody tr td::text").extract()[0].replace("\t", '').strip()
        title = response.css("h1::text").extract()[1].replace("\n", '').strip()
        price = response.css("p.special-price span.price::text").get().replace("\xa0", '')
        author = response.css("div.product-view-sa-author span").extract()[1]
        publisher = response.css("tbody tr td.data_publisher::text").get().replace("\t", '').strip()
        weight = response.css("tbody tr td.data_weight::text").get().replace("\t", '').strip()
        number_of_pages = response.css("tbody tr td.data_size::text").get().replace("\t", '').strip()
        type_of_book = response.css("tbody tr td.data_book_layout::text").get().replace("\t", '').strip()
        description = " ".join(response.css("div#desc_content.std p::text").extract())
        yield {
            "category": response.meta['category'],
            "page": response.meta['page'],
            "order": response.meta['order'],
            "id": book_id,
            "title": title,
            "price": price,
            "weight": weight,
            "author": author,
            "number_of_pages": number_of_pages,
            "type": type_of_book,
            "publisher": publisher,
            "desc": description
        }



