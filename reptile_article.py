import requests
import csv

url = 'https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
file = open('article.csv', 'a', newline='', encoding='utf-8')
csv_file = csv.writer(file)

offset = 0
while True:
    param = {'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,co'
               'mment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followee'
               's,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': str(offset),
    'limit': '10',
    'sort_by': 'created'}
    
    res = requests.get(url, headers=header, params=param).json()
    articles = res['data']
    
    for art in articles:
        title = art['title']
        artid = art['id']
        excerpt = art['excerpt']
        result = [title, 'https://zhuanlan.zhihu.com/p/{}'.format(artid), excerpt]
        print(result)
        csv_file.writerow(result)
    offset += 20
    if offset >= 60:
        break

