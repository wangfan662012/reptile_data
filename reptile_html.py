import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_movies = requests.get('https://movie.douban.com/chart')
# 获取数据
bs_movies = BeautifulSoup(res_movies.text,'html.parser')
# 解析数据
list_movies= bs_movies.find_all('div',class_='pl2')
# 查找最小父级标签
list_all = []
# 创建一个空列表，用于存储信息
for movie in list_movies:
    tag_a = movie.find('a')
    # 提取第0个父级标签中的<a>标签
    name = tag_a.text.replace(' ', '').replace('\n', '')
    # 电影名，使用replace方法去掉多余的空格及换行符
    url = tag_a['href']
    # 电影详情页的链接
    tag_p = movie.find('p', class_='pl')
    # 提取父级标签中的<p>标签
    information = tag_p.text.replace(' ', '').replace('\n', '')
    # 电影基本信息，使用replace方法去掉多余的空格及换行符
    tag_div = movie.find('div', class_='star clearfix')
    # 提取父级标签中的<div>标签
    rating = tag_div.text.replace(' ', '').replace('\n', '')
    # 电影评分信息，使用replace方法去掉多余的空格及换行符
    list_all.append([name,url,information,rating])
    # 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all
print(list_all)
# 打印

##另一种解法
tag_name = bs_movies.find_all('div', class_='pl2')
# 查找包含电影名和电影详情URL的<a>标签
tag_p = bs_movies.find_all('p',class_='pl')
# 查找包含电影基本信息的<p>标签
tag_div = bs_movies.find_all('div', class_='star clearfix')
# 查找包含电影评分信息的<div>标签
list_all = []
# 创建一个空列表，用于存储信息
for x in range(len(tag_name)):
# 启动一个循环，次数等于电影名的数量
    list_movie = [tag_name[x].find('a').text.replace(' ', '').replace('\n', ''),tag_name[x].find('a')['href'],tag_p[x].text.replace(' ', '').replace('\n', ''),tag_div[x].text.replace(' ', '').replace('\n', '')]
    # 提取信息，封装为列表。
    list_all.append(list_movie)
    # 将信息添加进list_all
print(list_all)
# 打印