from lxml import html
import requests

def usd_crawler():
    target = requests.get('https://www.tgju.org/profile/price_dollar_rl')
    parse_target = html.fromstring(target.content)
    usd_get = parse_target.xpath('//span[@class="price"]/text()')
    usd_str = str(usd_get)[2:9]
    usd = float(usd_str.replace(',',''))
    return str(usd)
