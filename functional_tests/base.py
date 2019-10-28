from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from unittest import skip

import os
import time
import unittest
import pdb

MAXWAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('browser.cache.disk.enable', False)
        self.profile.set_preference('browser.cache.memory.enable', False)
        self.profile.set_preference('browser.cache.offline.enable', False)
        self.profile.set_preference('network.http.use-cache', False)

        self.browser = webdriver.Firefox(self.profile)
        staging_server = os.environ.get('STAGING_SERVER')

        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def waitfor_row_listtable(self, row_text):
        starttime = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - starttime > MAXWAIT:
                    raise e
                time.sleep(0.5)