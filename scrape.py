import requests
import time
import csv
from bs4 import BeautifulSoup

csv_file = open("data3.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['index', '駅名', '乗降客数（日）', '人口総数', '男性人口', '男性人口比率', '0～14歳人口', '15～64歳人口', '65歳以上人口', '昼間人口', '世帯数', '一人世帯数', '一人世帯率', '小売事業所数', '小売業年間商品販売額', '全産業事業所数', '飲食店事業所数', '生徒学生数', '0～9歳人口(比率)', '10～19歳人口(比率)', '20～29歳人口(比率)', '30～39歳人口(比率)', '40～49歳人口(比率)', '50～59歳人口(比率)', '60～69歳人口(比率)', '70～79歳人口(比率)', '80歳以上人口(比率)', '買回り品(事業所数比率)', '最寄り品(事業所数比率)', '全産業従業者総数'])
    
for i in range(961, 5000):
    print(i)
    url = ('https://storestrategy.jp/?category=1&area=1&pref=14&id=' + str(i))
    res = requests.get(url)

    soup = BeautifulSoup(res.content, "lxml")
    title = soup.find('p', class_='contents_lv03_subtitle').text[:-9]

    output = []
    output.append(i)
    output.append(title)
    adjust = 0
    try:
        for tr in soup.find_all('tr'):
            if tr.find('td', class_='udot'):
                count = 0
                for td in tr.find_all('td', class_='udot'):
                    if count % 3 == 0:
                        span = td.find_all('span', class_='yellow')
                        if span:
                            data = span[0].text
                            if data != '':
                                output.append(data)
                                if count >= 3:
                                   break 
                                count += 1
                    if adjust == 0:
                        adjust += 1
                    else:
                        count += 1
        csv_writer.writerow(output)
    
    except Exception as identifier:
        pass


csv_file.close()
