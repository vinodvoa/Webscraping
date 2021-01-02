from bs4 import BeautifulSoup

import time
import requests
import pandas as pd 
import openpyxl as pyxl

OPTICURL = 'https://www.bhphotovideo.com/explora/videos/tag/optic?page='
EVENTSPACEURL = 'https://www.bhphotovideo.com/explora/videos/event?page='

def get_link_from_bandh(urlparm, filename):
    page = requests.get(urlparm)

    soup = BeautifulSoup(page.content, 'lxml')

    page_count = soup.find('div', class_='custom-pager-count')
    count = int(page_count.text[11:14])

    page_counter = 0
    item_counter = 0
    data = []

    while item_counter < count:
        url = urlparm + str(page_counter)
        
        print(url)

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'lxml')

        divtags = soup.findAll('div', class_='views-field views-field-label')

        for divtag in divtags:
            page_list = []

            title = divtag.span.a.text
            page_list.append(title)

            link = 'https://www.bhphotovideo.com' + divtag.span.a.get('href')
            
            page_list.append(link)
            data.append(page_list)

            # posted = divtag.div.div.div.span.text
            # print(posted)

            item_counter += 1

        page_counter += 1

        time.sleep(1)

    df = pd.DataFrame(data, columns = ['Title', 'Link'])

    save_file_name = filename + '.xlsx'

    df.to_excel(save_file_name)


if __name__ == "__main__":
    get_link_from_bandh(OPTICURL, 'bandhoptic')
    # get_link_from_bandh(EVENTSPACEURL, 'bandhevent')