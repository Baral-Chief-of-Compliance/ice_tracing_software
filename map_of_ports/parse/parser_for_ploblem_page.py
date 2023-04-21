from bs4 import BeautifulSoup
import requests
import time
import json


page = requests.get(f"https://www.myshiptracking.com/ru/ports?sort=ID&page=56")
page_html = page.text
soup = BeautifulSoup(page_html, "lxml")
all_ports_on_page = soup.find_all('tr')
all_ports_on_page.pop(0)

with open(f'../data/page_myshiptracking/page_56.json', 'w', encoding="utf-8") as file:

    for el in all_ports_on_page:
        td = el.find_all("td")
        type_of_port = td[2].text
        size_of_port = td[3].text
        a = el.find("a")
        name_of_port = a.text
        print(f"имя порта: {name_of_port}")
        print(f"тип порта: {type_of_port}")
        print(f"размер порта: {size_of_port}")
        print(f"ссылка: https://www.myshiptracking.com/{a['href']}")

        page_port = requests.get(f"https://www.myshiptracking.com/{a['href']}")
        page_port = page_port.text
        soup_for_page = BeautifulSoup(page_port, 'lxml')
        all_inf_about_port = soup_for_page.find('tbody').find_all('td')
        print(f"UN/LOCODE: {all_inf_about_port[0].text}")
        print(f"Страна: {all_inf_about_port[2].text}")

        longitude = all_inf_about_port[3].text
        longitude = float(longitude[:len(longitude) - 1])
        print(f"Долгота: {longitude}")

        latitude = all_inf_about_port[4].text
        latitude = float(latitude[:len(latitude) - 1])
        print(f"Широта: {latitude}")

        print(f"Часовой пояс: {all_inf_about_port[11].text}")
        port_dict = {
            "name": name_of_port,
            "type": type_of_port,
            "size": size_of_port,
            "UN_LOCODE": all_inf_about_port[0].text,
            "country": all_inf_about_port[2].text,
            "longitude": longitude,
            "latitude": latitude,
            "link": f"https://www.myshiptracking.com/{a['href']}"
            }
        json.dump(port_dict, file)
        file.write(",\n")
        print("\n\n")
        # time.sleep(1)

    file.close()