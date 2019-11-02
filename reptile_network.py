import requests
from bs4 import BeautifulSoup
import openpyxl

url = ('https://c.y.qq.com/soso/fcgi-bin/client_search_cp')
singers = ['周杰伦', '张杰', '谭维维']
all_song = {}
page = 3


def reptile_songs(name):
	song_list = []
	for x in range(1, page + 1):
		header = {
			'Origin': 'https://y.qq.com',
			'Referer': 'https://y.qq.com/portal/search.html',
			'Sec-Fetch-Mode': 'cors',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
		}
		param = {
			'ct': '24',
			'qqmusic_ver': '1298',
			'new_json': '1',
			'remoteplace': 'txt.yqq.song',
			'searchid': '57932146736576159',
			't': '0',
			'aggr': '1',
			'cr': '1',
			'catZhida': '1',
			'lossless': '0',
			'flag_qc': '0',
			'p': x,
			'n': '10',
			'w': name,
			'g_tk': '5381',
			'loginUin': '0',
			'hostUin': '0',
			'format': 'json',
			'inCharset': 'utf8',
			'outCharset': 'utf-8',
			'notice': '0',
			'platform': 'yqq.json',
			'needNewCode': '0'
		}
		res = requests.get(url, params=param, headers=header)
		res_json = res.json()
		songs = res_json['data']['song']['list']

		for song in songs:
			song_url = 'https://y.qq.com/n/yqq/song/' + str(song['mid']) + '.html'
			li = [song['name'], song['album']['name'], song_url, song['interval']]
			song_list.append(li)
	return song_list


def reptile_singer(names):
	for name in names:
		li = reptile_songs(name)
		all_song[name] = li
	return all_song


def save_songs():
	column_name = ['歌名', '所属专辑', '歌曲地址', '播放时长(秒)']
	wb = openpyxl.Workbook()
	print('----------getting songs------------')
	result = reptile_singer(singers)
	for singer, songs in result.items():
		sheet = wb.create_sheet(singer)
		sheet.append(column_name)
		# sheet.title = singer
		for song in songs:
			sheet.append(song)
	print('----------saving songs------------')
	wb.save('songs.xlsx')
	wb.close()
	print('----------It is OK------------')


if __name__ == '__main__':
	save_songs()
