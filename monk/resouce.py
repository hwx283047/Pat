#python  用于web开发，云平台支持，后台开发，应用软件开发，科学技术
#学习python小项目：


#httplib方法
import httplib
http = httplib.HTTPConnection('edu.51cto.com',80)
http.request('GET','/course/course_id-1413.html')
print http.getresponse().read()
http.close()
#urllib2
import urllib2
opener = urllib2.build_opener()
f = opener.open("http://edu.51cto.com/lesson/id-26518.html")
print f.read()
f.close()