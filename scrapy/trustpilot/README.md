使用website_crawler爬到的網址，去下載評論。
在此路徑中執行
<pre>
scrapy crawl trustpilot
</pre>
並在trustpilot/spiders/scraper.py中修改公司評論路徑
<pre>
import re
import pandas as pd
import scrapy

class Pages(scrapy.Spider):
    name = "trustpilot"

    company_data = pd.read_csv('trustpilot/consolidate_company_urls.csv')
</pre>
