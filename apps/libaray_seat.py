from bs4 import BeautifulSoup
import requests

def print_library_seat():
    url = 'https://lib.anyang.ac.kr/lib/SlimaPlus.csp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div tags with class "seat"
    div_tags = soup.find_all('div', class_='main_seat_list')

    text = []

    # Extract the text from span tags inside each div tag
    for div_tag in div_tags:
        span_tags = div_tag.find_all('span')
        for span_tag in span_tags:
            text.append(span_tag.text)

    # print(text)

    the_frist_reading_room = text[0:4]
    the_frist_reading_room = ' '.join(the_frist_reading_room)
    # print(the_frist_reading_room)

    the_second_reading_room = text[4:8]
    the_second_reading_room = ' '.join(the_second_reading_room)
    # print(the_second_reading_room)

    Suri_reading_room = text[8:12]
    Suri_reading_room = ' '.join(Suri_reading_room)
    # print(Suri_reading_room)

    seat = [the_frist_reading_room, the_second_reading_room,Suri_reading_room]
    # print(seat)


    return seat



# library_seat()


