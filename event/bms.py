import pdb
import time
import pickle
import dryscrape
from django.core.cache import get_cache
from dryscrape.driver.webkit import Node

class BMS():
    def __init__(self):
        # set up a web scraping session
        self.sess = dryscrape.Session(base_url = 'http://in.bookmyshow.com')
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)
        #sess.set_proxy('10.80.2.13', 80)
        self.sess.visit('/')

        self.r = get_cache('event')
      

    def crawl(self):
        for region in self._regions():
            print '-----------------'
            print region.text()
            region.click()
                 
            for event in self._events():
                print event.text()
                event.click()
                
                for day in self._days():
                    print day.text()
                    pdb.set_trace()
                    day.click()
                    self.snapshot(title=day.text())
                """
                    for cinemahall in self._cinemahalls():
                        print cinemahall.text()
                        cinemahall.click()
                        
                        for movie_timing in self._movies_timings():
                            self._select_movie_timing(movie_timing)
                            self.sess.render('sample1.png')
                """ 

    def snapshot(self, title):
        self.sess.render("%s.png" %title)

    def _regions(self, key='region'):
        # Select all region list
        region_label = self.sess.at_xpath('//li[@id="cntRegion"]')
        region_label.at_xpath('div/input').click()
        return region_label.xpath('div[@class="ddrrl"]/ul/li/div/span')

    def _events(self):
        # Event will be automatically bi clicked
        event = self.sess.at_xpath('//li[@id="cntEvent"]')
        return event.xpath('div[@class="ddrrl"]/ul/li/div/span')
        
    def _days(self):
        # Day will be automatically bi clicked
        day = self.sess.at_xpath('//li[@id="cntDate"]')
        return day.xpath('div[@class="ddrrl"]/ul/li/div/span')

    def _cinemahalls(self):
        # New page
        #return self.sess.at_xpath('//div[@class="dl"]/h5')
        clist = self.sess.xpath('//div[@id="dShowTimes"]/div[@class="btc"]/div[@class="dl"]/h5/a')
        pdb.set_trace()
        return clist
        
    def _movies_timings(self):
        # Cinema hall page
        return self.sess.xpath('//div[@id="dShowTimes"]/div[@class="btc"]')
        
    def _select_movie_timing(self, movie_time):
        movie = movie_time.at_xpath('div[@class="dl"]/h5/a')
        print movie.text()
        """
        for timing in movie_time.xpath('div[@class="dr"]/a'):
            timing.click()
            # Sleep for some time
            time.sleep(30)
        """

    def _select_passenger_class(self):
        # Select passenger page
        self.sess.at_xpath('//select[@id="tikCat"]').set('0002')
        self.sess.at_xpath('//select[@id="tikCat"]').select_option()
        self.sess.at_xpath('//select[@id="cmbQty"]/option').set_attr('value','1')
        self.sess.at_xpath('//a[@id="chseats"]').click()

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

bms = BMS()
bms.crawl()
