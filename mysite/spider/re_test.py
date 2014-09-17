# -*- coding: utf-8 -*-
# user for collect the information of taihao and cheap things

import re
from search_haitao import get_html, get_time, get_title
from datetime import datetime, date, time

str2 = '''
<a href="http://haitao.smzdm.com/youhui/295361" target="_blank" onclick="ga('send', 'event','海淘专区','列表_优惠_文章标题','295361_Clarks 其乐 Denner Motion 男款真皮休闲鞋');"> Clarks 其乐 Denner Motion 男款真皮休闲鞋<span class="red">$44（约￥360）有晒单</span></a>'''

str1 = '''
<a href="http://haitao.smzdm.com/youhui/293755" target="_blank" onclick="ga('send', 'event','海淘专区','列表_优惠_文章标题','293755_Panasonic 松下 EW-DE42-S 电动声波牙刷');">Panasonic 松下 EW-DE42-S 电动声波牙刷<span class="red">8990日元（约￥660）有晒单</span></a>'''

url = 'http://haitao.smzdm.com/p1'

def get_title(html):
	r = r';">(.*?)</a>'
	r2 = r';">(.*?)</sp'
	titler = re.compile(r2)
	title_list = titler.findall(html)
	return title_list

print get_title(str1)
print get_title(str2)

# title_list = get_title(get_html(url))
# print title_list
# for i in title_list:
# 	print i
# dt = datetime.strptime("09-04 16:30", "%m-%d %H:%M")
# print dt

time_list = get_time(get_html(url))
# print time_list

# def trs_time(time_list):
# 	datetime_list = []
# 	if (time_list):
# 		for time_item in time_list:
# 			if len(time_item) == 5:
# 				time_item = date.today().isoformat() + ' ' + time_item
# 				datetime2 = datetime.strptime(time_item, "%Y-%m-%d %H:%M")
# 				datetime_list.append(datetime2)
# 			elif len(time_item) == 11:
# 				time_item = '2014-'+ time_item
# 				datetime2 = datetime.strptime(time_item, "%Y-%m-%d %H:%M")
# 				datetime_list.append(datetime2)
# 			else:
# 				print 'error date'
# 		return datetime_list
#
#
#
# n = trs_time(time_list)
# for i in n:
# 	print i