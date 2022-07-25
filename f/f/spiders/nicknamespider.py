import scrapy

class NicknamesSpider(scrapy.Spider):
    name = 'nicknames'
    start_urls = [
        'https://www.op.gg/leaderboards/tier?champion=&region=na',
        'https://www.op.gg/leaderboards/tier?region=na&page=3'
    ]

    def parse(self, response):
        for player in response.css("table.css-4lctyh exo2f213"):
            yield {
                'name' : player.css('strong.summoner-name::text').get()
            }