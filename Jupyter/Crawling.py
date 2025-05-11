import requests

response = requests.get('https://shopping.naver.com/home')
html = response.text
print(html)

# %pip install requests

# %pip install bs4

from bs4 import BeautifulSoup

html_str = '''
<html>
    <body>
        <div id="content">
            <ul class = 'industry'>
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>스마트팩토리</li>
            </ul>
            <ul class = 'comlang'>
                <li>Python</li>
                <li>C++</li>
                <li>Javascript</li>
            </ul>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html_str, 'html.parser') # html 파싱싱


first_ul = soup.find('ul')
print(first_ul)
print(first_ul.text)
print(first_ul.get_text())


all_list = first_ul.findAll('li')
print(all_list)
print(all_list[0])
print(all_list[0].text)

for li in all_list :
    print(li.text)


find_ul = soup.find('ul', class_='comlang')
print(find_ul)
print(find_ul.text)


all_li = soup.select('li')
print(all_li)
print(all_li[0])
print(all_li[0].text)


all_li = soup.select('ul.industry > li')
print(all_li)
print(all_li[0])
print(all_li[0].text)


all_li = soup.select('ul.industry li')
print(all_li)
print(all_li[0])
print(all_li[0].text)


idid = soup.select('#content')
print(idid)
print(idid[0].text)


sss = '''
    <div class = "a">
        <a href="https://naver.com" class="dsc_thump"></a>
    </div>
'''

soup = BeautifulSoup(sss,"html.parser")


b = soup.select_one('div a')
print(b)
print(b['href'])
print(b['class'])


# 실습
search = input()

print('--------------------------')
response= requests.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={search}')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

news = soup.select('.news_tit')
for i in news :
    title = i.text
    link = i['href']
    print(title,link)


