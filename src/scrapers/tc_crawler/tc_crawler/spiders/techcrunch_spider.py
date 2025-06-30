import scrapy

class TechCrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]

    def parse(self, response):
        articles = response.css("a.loop-card__title-link")

        for article in articles:
            title = article.css("::text").get()
            link = article.attrib.get("href")

            if title and link:
                yield response.follow(link, callback=self.parse_article, meta={
                    "title": title.strip(),
                    "link": link
                })

        # Pagination support (load more pages)
        current_page = response.url.split("/page/")[-1] if "/page/" in response.url else "1"
        next_page_num = int(current_page) + 1
        next_page_url = f"https://techcrunch.com/page/{next_page_num}/"

        if next_page_num <= 50:  # You can increase this if needed
            yield response.follow(next_page_url, callback=self.parse)

    def parse_article(self, response):
        title = response.meta["title"]
        link = response.meta["link"]

        pub_date = response.css("div.wp-block-post-date time::attr(datetime)").get()
        paragraphs = response.css("p.wp-block-paragraph::text").getall()
        description = " ".join([p.strip() for p in paragraphs if p.strip()])

        yield {
            "source": "TechCrunch",
            "title": title,
            "link": link,
            "pub_date": pub_date,
            "description": description
        }
