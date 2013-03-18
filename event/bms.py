import pdb
import time
import random
import pickle
import dryscrape
from django.core.cache import get_cache
from dryscrape.driver.webkit import Node

class BMS():
    def __init__(self):
        # set up a web scraping session
        self.r = get_cache('event')
        return
        self.sess = dryscrape.Session(base_url = 'http://in.bookmyshow.com')
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('javascript_can_open_windows', False)
        #sess.set_proxy('10.80.2.13', 80)
        pdb.set_trace()
        self.set_cookie()
        #self.sess.set_html('','')
        try:
            self.sess.visit('/')
        except Exception,e:
            print e
        self.sess.visit('/')

        self.r = get_cache('event')
        self._select_cinema()

    def _go_home_page(self):
        self.sess.at_xpath('//div[@class="bmslogo"]/a').click()

    def set_cookie(self):
	cookies = ['Rgn=%7Ctext%3DBangalore%7CCode%3DBANG%7C; path=/; expires=Fri, 21-Dec-2014 06:24:45 GMT; domain=.bookmyshow.com;']
        #cookies = ['Rgn=%7CCode%3DBANG%7Ctext%3DBangalore%7C; path=/; expires=Fri, 21-Dec-2014 06:24:45 GMT; domain=.bookmyshow.com;']
        [self.sess.set_cookie(cookie) for cookie in cookies]

    def _select_cinema(self):
        self.sess.at_xpath('//input[@id="rdbCinema"]').click()

    def _select_cinema_field(self):
        self.sess.at_xpath('//div[@class="ddrbg"]/input').click()

    def _select_particular_cinema(self, count):
        self._select_cinema_field()
        return self.sess.xpath('//div[@class="ddrrl"]/div/ul/li')[count]

    def _select_particular_day(self):
        return self.sess.xpath('//div[@id="cmbMovieDate"]/div[@class="ddrrl"]/div/ul/li')[0]

    def _view_movies_listing(self):
        return self.sess.xpath('//div[@id="dMovies"]/div[@id="dMoviesList"]/div')

    def _movie_information(self, movie):
        return movie.at_xpath('div/div/div/span/a')

    def _movie_timmings(self, movie):
        return movie.xpath('div[@class="showlist"]/div')

    def _timming_information(self, timming):
        return timming.at_xpath('span/a[@href="javascript:;"]')

    def _ticket_types(self):
        return self.sess.xpath('//select[@id="tikCat"]/option')

    def _ticket_types_listing(self, val):
        self.sess.at_xpath('//select[@id="tikCat"]').set(val)
        self.sess.at_xpath('//select[@id="tikCat"]').select_option()
        self.sess.at_xpath('//select[@id="cmbQty"]').set('1')
        self.sess.at_xpath('//select[@id="cmbQty"]').select_option()

    def _close_seating_layout(self):
        self.sess.at_xpath('//div[@id="tblSeatLayout"]/div/a').click()

    def crawl(self):
        count = 0
        while True:
            try:
                cinema = self._select_particular_cinema(count)
            except Exception,e:
                print 'No more cinemas', e
                break
            print '-----------------'
            time.sleep(1)
            print cinema.text()
            cinema.click()

            day = self._select_particular_day()
            day.click()

            for movie in self._view_movies_listing():
                movie_name = self._movie_information(movie)
                print movie_name.text()
                
                for timming in self._movie_timmings(movie):
                    times = self._timming_information(timming)
                    if times is None:
                        print 'Timming not AV'
                        continue
                    print times.text()
                     
                    times.click()

                    for ticket_type in self._ticket_types():
                        if ticket_type.get_attr('value') is not '':
                            val = ticket_type.get_attr('value')
                            print val
                            self._ticket_types_listing(val)
                            time.sleep(3)
                            # Retrieve occupnacy
                            print 'Occupacy fetch'
                            pdb.set_trace()

                            # Close the overlay
                            self._close_seating_layout()
            self._go_home_page()
            self._select_cinema()
            count+=1
            exit()
        

    def snapshot(self, title):
        self.sess.render("%s.png" %title)

    def _seat_avail(self):
        # Seat layout page
        time.sleep(20)
        seat_table = self.sess.at_xpath('//div[@id="tblSeatInfo"]/table/tbody')
        print len(seat_table.xpath('tr'))

        for row in seat_table.xpath('tr'):
            seat_count = row.xpath('td') 
            if seat_count == 1:
                # Mentions the class name
                status = seat_count[0].text()
                continue
            for seat in seat_count:
                if seat.text()!='':
                    continue
                print seat.xpath('img').get_attr('src')
                # Logic for calculating the percentage filled or not
            len(tb.xpath('tr')[1].xpath('td/img'))

    def add_in_cache(self, theater_name, occupancy, total, corner):
        print 'Adding ', theater_name
        self.r.set(theater_name, {'occu'  : occupancy,
                                  'total' : total,
                                  'cotner': corner,
                                  'lat'   : random.randrange(1000),
                                  'lon'   : random.randrange(1000)
                                 })

    def temp_filler(self):
        for i in range(100):
            self.add_in_cache(random.randrange(1000), random.randrange(100), random.randrange(50),random.randrange(10) )
     


bms = BMS()
#bms.crawl()
bms.temp_filler()
