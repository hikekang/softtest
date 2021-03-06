# -*- coding: utf-8 -*-
# @Time    : 2020-02-05 17:51
# @Author  : Arrow and Bullet
# @FileName: baidu.py
# @Software: PyCharm
import random
import datetime
import win32con
from pymouse import *
from pykeyboard import *
import win32gui
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW, SW_SHOWMAXIMIZED, MOUSEEVENTF_LEFTDOWN
from selenium import webdriver
import time
from fake_useragent import UserAgent
import pymongo


option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

user = []
def mongo():
    myclient = pymongo.MongoClient(host="127.0.0.1", port=27017)
    mydb = myclient.jubao
    ipcol = mydb['ip']
    usercol = mydb['user']
    data = ipcol.find().skip(13).limit(12)
    user = usercol.find().skip(53)  # 62-74开始
    return data, user


def proxy():
    ua = UserAgent()
    ua = ua.chrome
    option.add_argument('user-agent=' + ua)
    # option.add_argument("--user-data-dir=" + r"C:/Users/hike/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(options=option)
    # driver.set_window_size(740, 735)
    return driver,ua

def open_driver(driver):
    print("打开页面")

    driver.implicitly_wait(10)
    driver.get('http://i.baidu.com/')
    time.sleep(1)
    print("等待网页响应")

def add_cookie(driver,bduss):
    cookielist=[{
        'domain': '.baidu.com',
        'expiry': 1841140385.316289,
        'httpOnly': True,
        'name': 'BDUSS',
        'path': '/',
        'secure': False,
        'value': bduss
    }]
    for cookie in cookielist:  # 遍历添加cookie
        if 'expiry' in cookie:
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
    driver.refresh()

def add_coookie_login(bduss):
    window_name = u'百度个人中心——您在百度的家 - Google Chrome'
    handow = win32gui.FindWindow(None, window_name)

    win32gui.SetWindowPos(handow, HWND_TOPMOST, 0, 0, 750, 723, SWP_SHOWWINDOW)
    # win32gui.ShowWindow(handow, SW_SHOWMAXIMIZED)
    m = PyMouse()
    m.click(652, 61, 1, 1)
    time.sleep(1)
    m.click(301, 87, 1, 1)
    time.sleep(1)
    m.click(273, 168, 1, 1)
    time.sleep(1)
    k = PyKeyboard()
    k.type_string('BDUSS')
    m.click(315, 236, 1, 1)
    time.sleep(1)
    k.type_string(bduss)
    time.sleep(1)
    m.click(369, 446, 1, 1)
    time.sleep(1)
    m.click(436, 141, 1, 3)
    time.sleep(1)
    m.click(297, 541, 1, 1)
    time.sleep(1)
    m.click(367, 656, 1, 1)
    time.sleep(1)
    m.click(70, 656, 1, 1)
def write_log(user_name,title):
    today=datetime.date.today()
    filename=str(today)+"-log.txt"
    with open(filename,'a') as file_object:
        file_object.write(user_name+"\t:"+title+"\n")


def login(driver, user):
    driver.refresh()
    print("点击登录")
    # driver.implicitly_wait(15)
    driver.find_element_by_link_text('登录').click()
    # time.sleep(5)
    print("5s倒计时")

    print("用户名登录")
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
    name = user.get('name')
    pwd = user.get('pwd')
    print("3s倒计时")

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

def isElementExist(driver, element):
    flag = True
    browser = driver
    try:
        browser.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag
def jubao(driver, data, user):
    print("正在跳转举报链接")
    driver.implicitly_wait(30)
    url_jubao = data.get('url_jubao')
    driver.get(url_jubao)
    title=data.get('title')
    name=user.get('name')

    time.sleep(2)
    print("等待网页显示")
    d1 = random.randint(2, 3)
    if(d1==2):
        print("个人")
    elif(d1==3):
        print("企业")
    driver.find_element_by_xpath('//*[@id="jubao-type-level1"]/a['+str(d1)+']').click()

    print("正在填写内容")
    reason="reason"+str(random.randint(1,3))
    driver.find_element_by_xpath('//*[@id="form-description"]').send_keys(data.get(reason))
    driver.find_element_by_xpath('//*[@id="form-pic2"]').send_keys(data.get('url'))
    driver.find_element_by_xpath('//*[@id="form-phone"]').send_keys(user.get('phone'))
    print("内容填写完毕，请填写验证码")
    # 写日志
    write_log(name, title)


def quitChrome(driver):
    print("清理缓存")
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    print("关闭浏览器")
    # driver.close()
    # driver.quit()
    print("切换ip")
def close_ip_web():
    win_name="IP地址查询--手机号码查询归属地 | 邮政编码查询 | 长途电话区号 | 身份证号码验证在线查询网 - Internet Explorer"
    handow=win32gui.FindWindow(None,win_name)
    win32gui.PostMessage(handow,win32con.WM_CLOSE,0,0)

def main():
    data, users = mongo()
    dd = []
    for d in data:
        dd.append(d)

    driver, ua_img = proxy()
    open_driver(driver)
    for u in users:
        add_cookie(driver,u.get('BDUSS'))
        for d in dd:
            jubao(driver, d, u)
        quitChrome(driver)

if __name__ == '__main__':
    main()
