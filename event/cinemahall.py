import pdb
import time
import pickle
import dryscrape
from django.core.cache import get_cache
from dryscrape.driver.webkit import Node

class CinemaHall():

    def __init__(self):
        # set up a web scraping session
        self.sess = dryscrape.Session(base_url = 'http://in.bookmyshow.com/buytickets/?srid=MWEST&eid=&cid=FNAN&did=20120622&ety=MT')
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)
        #sess.set_proxy('10.80.2.13', 80)
        self.set_cookie()
        self.sess.visit('')

        self.r = get_cache('event')

    def set_cookie(self):
        cookies = ['__utma=1.490339066.1340303086.1340303086.1340303086.1; expires=Sat, 21-Jun-2014 18:24:45 GMT; domain=.bookmyshow.com; path=/','__utmb=1.3.10.1340303086; expires=Thu, 21-Jun-2012 18:54:45 GMT; domain=.bookmyshow.com; path=/', '__utmc=1; domain=.bookmyshow.com; path=/', '__utmz=1.1340303086.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); expires=Fri, 21-Dec-2012 06:24:45 GMT; domain=.bookmyshow.com; path=/', 'psrc=MWEST; expires=Thu, 31-Dec-2020 23:59:59 GMT; domain=in.bookmyshow.com; path=/', 'fcine=%7Cc%3D%7Cp%3D%7CPC%3D%7Cpop%3DFNAN%3BFNCM%3BGLBS%3B%7C; expires=Thu, 31-Dec-2020 23:59:59 GMT; domain=in.bookmyshow.com; path=/']
        [self.sess.set_cookie(cookie) for cookie in cookies]

    def crawl(self):
        for movie_time in self._movies_timings():
            print '--------------'
            movie = movie_time.at_xpath('div[@class="dl"]/h5/a')
            print movie.text()
            for timing in movie_time.xpath('div[@class="dr"]/a'):
                print timing.text()
                timing.click()
                #self._close_overlay()
                self._select_passenger_class()
                self._seat_avail()

    def _movies_timings(self):
        # Cinema hall page
        return self.sess.xpath('//div[@id="dShowTimes"]/div[@class="btc"]')

    def _close_overlay(self):
        self.sess.at_xpath('//div[@class="fright"]/a').click()
        
    def _select_passenger_class(self):
        # Select passenger page
        time.sleep(10)
        self.sess.at_xpath('//select[@id="tikCat"]').set('0002')
        self.sess.at_xpath('//select[@id="tikCat"]').select_option()
        self.sess.at_xpath('//select[@id="cmbQty"]/option').set_attr('value','1')
        self.sess.at_xpath('//a[@id="chseats"]').click()

    def _seat_avail(self):
        # Seat layout page
        time.sleep(10)
        seat_table = self.sess.at_xpath('//div[@id="tblSeatInfo"]/table/tbody')

        avail = {}
        for row in seat_table.xpath('tr'):
            seat_count = row.xpath('td') 
            if len(seat_count) == 1:
                # Mentions the class name
                status = seat_count[0].text()
                avail[status] =  { 'filled':0,'empty':0 }
                continue
            for seat in seat_count:
                if seat.text()!='':
                    continue
                try:
                    chair_status = seat.at_xpath('img').get_attr('src')
                except Exception,e:
                    # Empty space is their
                    continue
                if chair_status.find('R_chair')>0:
                    avail[status]['filled']+=1
                else:
                    avail[status]['empty']+=1
                # Logic for calculating the percentage filled or not

        print avail

        self.sess.xpath('//div[@class="dslnr"]')[2].xpath('//img[@src="http://cnt.in.bookmyshow.com/in/ipl/close.gif"]')[-2].parent().click()


ch = CinemaHall()
ch.crawl()
