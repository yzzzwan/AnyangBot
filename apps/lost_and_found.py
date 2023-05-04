from bs4 import BeautifulSoup
import requests



def lost_items_list():
    url = 'https://www.anyang.ac.kr/main/communication/lost-found.do'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    lost_items = soup.select('td.b-td-left.b-td-title a')

    lost_items_link=[]

    for lost_item in lost_items:
        # print(lost_item.text.strip())
        lost_items_link.append(lost_item['href'])

    return lost_items_link

def lost_item_detail(link):
    lost_item_details = []

    for i in range(5):
        url = 'https://www.anyang.ac.kr/main/communication/lost-found.do' + link[i]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        lost_items = soup.select('table tr:nth-child(2) td')

        lost_item_info=[]
        for lost_item in lost_items:
            # print(lost_items_detail.text.strip())
            lost_item_info.append(lost_item.text.strip())

        lost_item_details.append(lost_item_info)

    return lost_item_details
    # # ex_ lost_items = [책 분실물, 에어팟 분실물, 안경 분실물 ...]



# links = lost_items_list()
# print(lost_item_detail(links))
#






