import scrapy


class DadospremierleagueSpider(scrapy.Spider):
    name = 'dadospremierleague'
    #allowed_domains = ['soccerstats.com']
    start_urls = ['https://www.soccerstats.com/latest.asp?league=england']

    def parse(self, response):
      for dados in response.css('.trow3 .trow3 b'):
            yield {
               'Partidas jogadas': response.css('.trow3 .trow3 td:nth-child(1) b::text').get(),
                '(%) Vitórias do time da Casa': response.css('td:nth-child(2) .trow3:nth-child(1) td:nth-child(2) b::text').get(),
                '(%)vitórias do Visitantes':response.css('.trow3~ .trow3+ .trow3 td:nth-child(2) b::text').get(),
                'Over 1,5 ': response.css('.trow3 .trow3:nth-child(1) td:nth-child(5) b::text').get(),
                'Média de gols por jogo': response.css('.trow3 .trow3 font b::text').get(),
                'Média de gols do time da Casa': response.css('td~ td+ td .trow3:nth-child(1) td~ td+ td b::text').get(),
                'Média de gols marcados pelo time visitante': response.css('td~ td+ td .trow3:nth-child(2) td~ td+ td b::text').get(),
                'Gols marcado entre 0-15min': response.css('#btable:nth-child(18) .odd:nth-child(2) td:nth-child(2)::text').get(),
                'Gols marcado entre 16-30min': response.css('#btable:nth-child(18) .odd:nth-child(3) td:nth-child(2)::text').get(),
                'Gols marcado entre 31-45min': response.css('#btable:nth-child(18) .odd:nth-child(4) td:nth-child(2)::text').get(),
                'Gols marcado entre 46-60min': response.css('#btable:nth-child(18) .odd:nth-child(5) td:nth-child(2)::text').get(),
                'Gols marcado entre 61-75min': response.css('h3+ #btable .odd:nth-child(6) td:nth-child(2)::text').get(),
                'Gols marcado entre 76-90min': response.css('h3+ #btable .odd+ .odd:nth-child(7) td:nth-child(2)::text').get(),
                'Periodo do 1º Gol': response.css('h3+ #btable .odd:nth-child(2) td:nth-child(2) font::text').get(),
                'Total de gols no periodo do 1º Gol': response.css('#btable:nth-child(29) .odd:nth-child(2) td:nth-child(3)::text').get(),
                'Periodo do 2º Gol': response.css('h3+ #btable .odd+ .odd:nth-child(3) td:nth-child(2) font::text').get(),
                'Total de gols no periodo do 2º Gol': response.css('#btable:nth-child(29) .odd:nth-child(3) td:nth-child(3)::text').get(),
                'Periodo do 3º Gol': response.css('h3+ #btable .odd~ .odd+ .odd:nth-child(4) td:nth-child(2) font::text').get(),
                'Total de gols no periodo do 3º Gol': response.css('#btable:nth-child(29) .odd:nth-child(4) td:nth-child(3)::text').get(),
                'Total de Gols marcado no 1º Tempo': response.css('#btable:nth-child(24) .odd:nth-child(2) td:nth-child(2)::text').get(),
                'Total de Gols marcado no 2º Tempo': response.css('#btable:nth-child(24) .odd+ .odd td:nth-child(2)::text').get()
            }
        #pass
