import os  
import time
from selenium import webdriver
#测试网络连通性
ping_value=os.system('ping 8.8.8.8')
#如果网络通畅自动连接海大vpn
if ping_value == 0:
	browser = webdriver.Chrome()
	browser.get('https://vpn.ouc.edu.cn')
	#用户名
	username="xxxxxxxx"
	#密码
	passwd="xxxxxxxx"
	#自动连接
	browser.implicitly_wait(10)
	elem=browser.find_element_by_id("svpn_name")
	elem.send_keys(username)
	elem=browser.find_element_by_id("svpn_password")
	elem.send_keys(passwd)
	elem=browser.find_element_by_id("logButton")
	elem.click()
