import requests
import time
import csv
from bs4 import BeautifulSoup

csv_file = open("3.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['駅名', '乗降客数（日）', '人口総数', '男性人口', '男性人口比率', '0～14歳人口', '15～64歳人口', '65歳以上人口', '昼間人口', '世帯数', '一人世帯数', '一人世帯率', '小売事業所数', '小売業年間商品販売額', '全産業事業所数', '飲食店事業所数', '生徒学生数', '0～9歳人口(比率)', '10～19歳人口(比率)', '20～29歳人口(比率)', '30～39歳人口(比率)', '40～49歳人口(比率)', '50～59歳人口(比率)', '60～69歳人口(比率)', '70～79歳人口(比率)', '80歳以上人口(比率)', '買回り品(事業所数比率)', '最寄り品(事業所数比率)', '全産業従業者総数'])
    
for i in range(8452, 9397):
    print(i)
    url = ('https://storestrategy.jp/?category=1&area=1&pref=14&id=' + str(i))
    res = requests.get(url)

    soup = BeautifulSoup(res.content, "lxml")
    title = soup.find('p', class_='contents_lv03_subtitle').text[:-9]

    output = []
    output.append(title)
    try:
        for tr in soup.find_all('tr'):

            if tr.find('td', class_='udot'):
                for tr in tr.find_all('td', class_='udot'):
                    span = tr.find_all('span', class_='yellow')
                    if span:
                        data = span[0].text
                        if data != '':
                            output.append(data)
                            break
        csv_writer.writerow([i, output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8], output[9], output[10], output[11], output[12], output[13], output[14], output[15], output[16], output[17], output[18], output[19], output[20], output[21], output[22], output[23], output[24], output[25], output[26], output[27], output[28]])
    
    except Exception as identifier:
        pass


csv_file.close()
