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

        # there are some failing HTTP requests, so we need to enter
        # a more error-resistant mode (like real browsers do)
        self.sess.set_error_tolerant(True)

        # we don't need images
        self.sess.set_attribute('auto_load_images', False)

        # if we wanted, we could also configure a proxy server to use,
        # so we can for example use Fiddler to monitor the requests
        # performed by this script
        #sess.set_proxy('10.80.2.13', 80)

        # visit homepage and log in
        self.sess.visit('/')

        self.r = get_cache('event')

    def _region(self):
        # Select all region list
        region_label = self.sess.at_xpath('//li[@id="cntRegion"]')
        region_label.at_xpath('div/input').click()

        regions = region_label.xpath('div[@class="ddrrl"]/ul/li/div')
        pdb.set_trace()
        [ self.r._client.lpush('regions',pickle.dumps(region)) for region in regions ]

    def _select_region(self):
        # Click on one
        region = pickle.load( self.r._client.lpop('regions') )
        pdb.set_trace()
        region.at_xpath('span').click()
        self.sess.render('sample.jpg')

    def defi(self):

        event = sess.at_xpath('//li[@id="cntEvent"]')
        oneevent = event.at_xpath('div[@class="ddrrl"]/ul/li/div')
        # Click on one event
        oneevent.at_xpath('span').click()

        day = sess.at_xpath('//li[@id="cntDate"]')
        #onedate = day.at_xpath('div[@class="ddrrl"]/ul/li/div')
        onedate = day.xpath('div[@class="ddrrl"]/ul/li/div')[1]
        # Click on one day
        onedate.at_xpath('span').click()

        # New page
        onecinemahall = sess.at_xpath('//div[@class="dl"]/h5')
        # Click on the cinema hall
        sess.at_xpath('//div[@class="dl"]/h5/a').click()

        # Cinema hall page
        onemovie = sess.at_xpath('//div[@class="btc"]/div[@class="dl"]/h5')
        onetiming = sess.at_xpath('//div[@class="btc"]/div[@class="dr"]/a')
        onetiming.click()

        # Select passenger page
        time.sleep(10)
        time.sleep(20)
        sess.at_xpath('//select[@id="tikCat"]').set('0002')
        sess.at_xpath('//select[@id="tikCat"]').select_option()
        sess.at_xpath('//select[@id="cmbQty"]/option').set_attr('value','1')
        sess.at_xpath('//a[@id="chseats"]').click()

        # Seat layout page
        time.sleep(20)
        seat_table = sess.at_xpath('//div[@id="tblSeatInfo"]/table/tbody')
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
bms._region()
bms._select_region()
