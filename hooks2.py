#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import datetime
import calendar
import web
import json

from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, SINCLAIR_FONT, CP437_FONT, TINY_FONT
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.led_matrix.device import max7219

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)


urls = ('/.*', 'hooks', '/favicon.ico', 'icon')

app = web.application(urls, globals())


class hooks:
    def GET(self):
        user_data = web.input(id=" ")
	print(user_data)
	msg = user_data['id']
        # print(msg)
        i = 0
        loop = 3
        # reserve the display 
        with open('busy.txt', 'w') as the_file:
           the_file.write('1')
	while i < loop:
            device.clear()
            show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
            time.sleep(5)
            i += 1
        # release the display
        with open('busy.txt', 'w') as the_file:
            the_file.write('0')
        # write the web page
        return "<h1>" + user_data.id + "<h1>"

if __name__ == '__main__':
    app.run()