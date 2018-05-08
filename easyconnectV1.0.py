import os  
import time
from selenium import webdriver
#测试网络连通性
ping_value=os.system('ping www.baidu.com')
#如果网络不通畅自动连接
if ping_value == 1:
	browser = webdriver.Chrome()
	browser.get('http://10.81.2.6/a70.htm')
	#用户名
	username="xxxxxxxx"
	#密码
	passwd="xxxxxxxx"
	#自动登陆
	browser.implicitly_wait(10)
	#填写用户名
	elem=browser.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[1]')
	elem.send_keys(username)
	#填写密码
	elem=browser.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[2]')
	elem.send_keys(passwd)
	#点击‘签到’
	elem=browser.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[3]')
	elem.click()
	browser.implicitly_wait(10)
	browser.quit()

