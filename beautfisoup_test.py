# -*- encoding: utf-8 -*-
'''
@File    :   beautfisoup_test.py
@Time    :   2020/02/21 21:23:31
'''


from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
def test():
    print(soup.title)
    # name 
    print('soup.name: %s' % soup.name)
    print('soup.head.name: %s' % soup.head.name)
    print('soup.head: %s' % soup.head)
    print(soup.a)
    print(soup.p)
    print('*'*10)
    print(soup.p.attrs)
    print(soup.p['class'])  # soup.p.get('class')
    print('-' * 10)
    # NavigableString
    print('soup.p.string:  %s' % soup.p.string)

# test()

# =====================================
# find_all()
result = soup.find_all('b')
# print(result)



# B传正则表达式
import re  
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)


# 传列表
lit = ["a", "b"]
result = soup.find_all(lit)
# print(result)


# 传True
result = soup.find_all(True)
# print(result)


# 传方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

result = soup.find_all(has_class_but_no_id)
print(result)
