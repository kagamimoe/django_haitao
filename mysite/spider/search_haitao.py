# -*- coding: utf-8 -*-
# user for collect the information of taihao and cheap things

import re
import urllib
import urllib2
import string
import time
import os
import sys
import sqlite3
from datetime import datetime, date, time

def get_html(url):
	headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
	req = urllib2.Request(url, headers=headers)
	my_response = urllib2.urlopen(req)
	html = my_response.read()
	return html

def get_title(html):
	r = r';">(.*?)</sp'
	titler = re.compile(r)
	title_list = titler.findall(html)
	return title_list

def get_link(html):
	# r = r'y">\s*?<a href="(http://www\.smzdm\.com/URL/.{18})'
	r = r'y">\s*?<a href="(htt.*?)"'
	linkr = re.compile(r)
	link_list = linkr.findall(html)
	return link_list

def get_time(html):
	r = '"lrTime">(.*?)</span>'
	timer = re.compile(r)
	time_list = timer.findall(html)
	return time_list

def trs_list(title_list):
	true_list = []
	for item in title_list:
		if '<img' not in item and '<em>' not in item:
			item = string.replace(item, '<span class="red">',' ')
			true_list.append(item)
	return true_list

def trs_time(time_list):
	datetime_list = []
	if (time_list):
		for time_item in time_list:
			if len(time_item) == 5:
				time_item = date.today().isoformat() + ' ' + time_item
				datetime2 = datetime.strptime(time_item, "%Y-%m-%d %H:%M")
				datetime_list.append(datetime2)
			elif len(time_item) == 11:
				time_item = '2014-'+ time_item
				datetime2 = datetime.strptime(time_item, "%Y-%m-%d %H:%M")
				datetime_list.append(datetime2)
			else:
				print 'error date'
		return datetime_list

class Recorder:
	def __init__(self):
		self.conn = sqlite3.connect('/Users/kagami/Desktop/django_haitao/mysite/db.sqlite3', check_same_thread = False)
		self.cur = self.conn.cursor()

	def save_item(self, title, url, datetime):
		if self.is_existed_finger(title):
			return False

		sql = "insert into smzdm_goodspost values(NULL, '%s', '%s', '%s')" % (title.replace('\'', ''), url, datetime)
		try:
			self.cur.execute(sql)
		except:
			print 'Save data error.[%s]' % sql
			return False
		try:
			self.conn.commit()
		except sqlite3.OperationalError, e:
			print "Error when commit:[%s]." % e.message
		return True

	def is_existed_finger(self, title):
		sql = "select count(*) from smzdm_goodspost where title = '%s'" % title.replace('\'', '')
		self.cur.execute(sql)
		rows = self.cur.fetchall()
		cnt = int(rows[0][0])
		return True if cnt > 0 else False

# def save_item(trs_list, total_link_list):
# 	item_list = []
# 	item = dict {
# 		title
# 	}





if __name__ == '__main__':
	total_list = []
	total_link_list = []
	total_time_list = []
	page = 1
	while page < 4:
		url = 'http://haitao.smzdm.com/p'
		url = url + str(page)
		# print get_html(url)
		# print get_title(get_html(url))
		# time.sleep(5)
		html = get_html(url)
		title_list = get_title(html)
		time_list = get_time(html)
		total_list =  total_list + title_list
		total_link_list = total_link_list + get_link(html)
		total_time_list = total_time_list + time_list
		print '第%d页抓取完毕' % page
		page = page + 1
	f = open('1.txt','w')
	recorder = Recorder()
	t_list = trs_list(total_list)
	trs_time_list = trs_time(total_time_list)
	del t_list[0]
	for i in range(len(t_list)):
		# print total_link_list[i]
		f.write(t_list[i] + '\n')
		f.write(total_link_list[i] + '\n')
		f.write(total_time_list[i] + '\n')
	f.close()

	print 'It has ' + str(len(t_list)) + ' titles'
	print 'It has ' + str(len(total_link_list)) + ' urls'
	print 'It has ' + str(len(total_time_list)) + ' times'

	# for i in range(len(t_list)):
		# recorder.save_item(t_list[i], total_link_list[i], trs_time_list[i])

	# print "已存入数据库"
	sys.exit(1)