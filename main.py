# -*- coding: utf-8 -*-

from scrapy.cmdline import execute

import sys
import os




import sys
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(["scrapy", "crawl", "jobbole"])
    #execute(["scrapy", "crawl", "zhihu_sel"])
except:
    print("Unexpected error:", sys.exc_info()) # sys.exc_info()返回出错信息