import requests
from bs4 import BeautifulSoup

index = 0
headers = {'referer': 'http://jandan.net',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


def save_img(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text, "lxml")
    # print(html.prettify())
    print(html.find_all('a', attrs={'class': 'view_img_link'}))
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href')) - 3: len(link.get('href'))]),
                  'wb') as jpg:
            jpg.write(requests.get("http:" + link.get('href')).content)
        print("正在抓取第%s条数据" % index)
        index += 1


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    save_img(url)
    # for i in range(0, 5):
    #     save_img(url)
    #     url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('a', {
    #         'class': 'previous-comment-page'}).get('href')
