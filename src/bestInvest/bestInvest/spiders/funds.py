import scrapy


class FundsSpider(scrapy.Spider):
    name = 'funds'
    start_urls = ['http://fundsexplorer.com.br/']

    def parse(self, response):
        nomes = response.css('#destaques_home a::text').getall()
        c = 0
        for fundos in response.css('.card_destaques_home'):
            yield{
                'nome' : nomes[c],
                'preco' : fundos.css('.cotacao_destaques_home::text').get(),
                'setor' : fundos.css('li:nth-child(1) strong::text').get(),
                'pvp' : fundos.css('li:nth-child(2) strong::text').get(),
                'dy' : fundos.css('li~ li+ li strong::text').get()
            }
            c += 1
