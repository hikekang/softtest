# -*- coding: utf-8 -*-
# @Time    : 2020-02-05 17:51
# @Author  : Arrow and Bullet
# @FileName: baidu.py
# @Software: PyCharm
import random

from selenium import webdriver
import time
from fake_useragent import UserAgent
import pymongo
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import requests
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

user = []


# data=[]
#
def mongo():
    myclient = pymongo.MongoClient(host="127.0.0.1", port=27017)
    mydb = myclient.jubao
    ipcol = mydb['ip']
    usercol = mydb['user']
    data = ipcol.find()
    user = usercol.find().skip(44)  # 20开始
    return data, user


def proxy():
    '''
    url_ip = "http://dev.kdlapi.com/api/getproxy/?orderid=917598854915999&num=1&protocol=2&method=2&an_an=1&an_ha=1&sp1=1&sp2=1&quality=1&sep=1"
    response = requests.get(url_ip)
    text = response.content.decode('utf-8')  # 解码
    soup = BeautifulSoup(text, 'html5lib')  # 以浏览器的方式解析文档生成HTML5格式的文档
    ip = soup.find('body').string
    获取IP地址
    print(ip)
    option.add_argument('--proxy-server=http://' + ip)
    :return:
    '''
    # 生成一个ua

    ua = UserAgent()
    ua = ua.chrome

    option.add_argument('user-agent=' + ua)

    driver = webdriver.Chrome(options=option)
    driver.set_window_size(838, 735)

    return driver


def open_driver(driver):
    # driver.delete_all_cookies()
    print("打开页面")

    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    # time.sleep(3)
    print("等待网页响应")
def write_log(user_name,title):
    filename="log.txt"
    with open(filename,'a') as file_object:
        file_object.write(user_name+"\t:"+title+"\n")


def login(driver, user):
    print("点击登录")
    # driver.implicitly_wait(15)
    driver.find_element_by_link_text('登录').click()
    # time.sleep(5)
    print("5s倒计时")
    # for x in range(5):
    #     time.sleep(1)
    #     print(5 - x)
    print("用户名登录")
    # driver.implicitly_wait(15)
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
    name = user.get('name')
    pwd = user.get('pwd')
    print("3s倒计时")
    # for x in range(3):
    #     time.sleep(1)  18659566436
    #     print(3-x)
    a = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]')
    a.clear()
    print("填写用户名")
    print(name)
    a.send_keys(name)
    b = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]')
    b.clear()
    print("填写密码")
    b.send_keys(pwd)
    print("登录")
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
    # time.sleep(20)
    print("20s倒计时")
    # for x in range(20):
    #     time.sleep(1)
    #     print(20 - x)
    # 点击下拉列表


def jubao(driver, data, user):
    print("正在跳转举报链接")
    driver.implicitly_wait(30)
    url_jubao = data.get('url_jubao')
    driver.get(url_jubao)
    title=data.get('title')
    name=user.get('name')

    # time.sleep(3)
    # print(url_jubao)
    # for x in range(3):
    #     time.sleep(1)
    #     print(3 - x)
    # driver.implicitly_wait(10)
    time.sleep(0.2)
    print("等待网页显示")
    print("查找企业/组织侵权")
    driver.find_element_by_xpath('//*[@id="jubao-type-level1"]/a[3]').click()
    print("正在填写内容")
    reason="reason"+str(random.randint(1,3))
    driver.find_element_by_xpath('//*[@id="form-description"]').send_keys(data.get(reason))
    driver.find_element_by_xpath('//*[@id="form-pic2"]').send_keys(data.get('url'))
    driver.find_element_by_xpath('//*[@id="form-phone"]').send_keys(user.get('phone'))
    print("内容填写完毕，请填写验证码")
    # 写日志
    write_log(name, title)
    # time.sleep(10)

    # for x in range(20):
    #     time.sleep(1)
    #     print(20 - x)


def quitChrome(driver):
    print("清理缓存")
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    print("关闭浏览器")
    driver.quit()
    print("切换ip")


def main():
    data, users = mongo()
    dd = []
    for d in data:
        dd.append(d)
    # user=mongo()[1]
    for u in users:
        driver = proxy()
        open_driver(driver)
        login(driver, u)
        for d in dd:
            jubao(driver, d, u)
        quitChrome(driver)


if __name__ == '__main__':
    main()
