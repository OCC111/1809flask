import requests
import re
import json
from lxml import etree



def getdata():

    url = 'https://wap.nvshens.com/gallery/ugirl/2.html'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }

    for i in range(1,100):
        start_url = 'https://wap.nvshens.com/gallery/ugirl/' + str(i) +'.html'

        html = requests.get(url=start_url,headers=headers).text
        gettitle(html)

def gettitle(html):

    l_list = etree.HTML(html)
    l = l_list.xpath('//span[@class="ck-icon"]/mip-img/@alt')

    print(l,end="\n")


if __name__ == '__main__':
    getdata()

