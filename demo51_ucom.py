import requests, bs4

URL1 = "https://www.uuu.com.tw/"

r1 = requests.get(URL1)
soup = bs4.BeautifulSoup(r1.content, "html.parser")
print(type(soup), soup.title.name, soup.title.string)

courseList = soup.find('div', {'id': 'course_list'})
for c in courseList:
    print(type(c), c)

courseLink = courseList.find_all('a')
for link in courseLink:
    print(link.p)
    print(link.get('href'))
