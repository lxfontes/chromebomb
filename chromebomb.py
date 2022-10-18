#!/usr/bin/env python3

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import window


prefs = {'profile.default_content_setting_values': {'javascript': 1, 'images': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2, 'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}, "intl.accept_languages": "en,en-US,en-GB"}

opts = Options()
#opts.add_argument('--headless')
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--start-maximized")
opts.add_argument("--disable-infobars")
opts.add_argument("--disable-gpu")
opts.add_argument("--enable-strict-powerful-feature-restrictions")
opts.add_argument('--disable-web-security')
opts.add_experimental_option( "prefs", prefs)
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

launch_path = os.path.join(os.path.dirname(__file__), "launch.html")

for i in range(0, 1):
    start = time.time()
    driver.get('file://' + launch_path)
    end = time.time()
    print(end - start)


time.sleep(100)
driver.quit()
