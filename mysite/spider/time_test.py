# -*- coding: utf-8 -*-
from datetime import datetime, date, time

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", tiem.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())

# currenttime = 1377075601.54
# print time.time()
# print time.ctime()
# print time.ctime(currenttime)
# print time.localtime()
# print type(time.localtime())
# print time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print time.strftime('%Y-%m-%d %H:%I:%S',time.localtime(time.time()))
# currentstr = '2013-08-21 17:05:01'
# print time.strptime(currentstr,'%Y-%m-%d %H:%I:%S')
# dt = datetime.strptime("09-04 16:30", "%m-%d %H:%M")
# print dt
url = '22:54'
url = date.today().isoformat() + ' ' + url
date1 = datetime.strptime(url, "%Y-%m-%d %H:%M")
print url
print type(date1)

url2 = '09-04 22:54'
url2 = '2014-'+ url2
date2 = datetime.strptime(url, "%Y-%m-%d %H:%M")
print date2
print type(date2)

# time1 = datetime.combine(date.today(),time(datetime.strptime(url,"%H:%M")))
# print time1
# print string_toTimestamp('09-04 22:54')
