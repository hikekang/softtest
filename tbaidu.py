import threading
from tkinter import *

import win32gui
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from selenium import webdriver
import time
import psutil
import os
from fake_useragent import UserAgent
import pymongo
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])


pid=os.getpid()
# p=psutil.Process(pid)

kk=1
def test(content):
    # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
    if content.isdigit() or content == "":
        return True
    else:
        return False


def pauses():
    global kk
    kk = 1

def gogo():
    global kk
    kk = 0

def sleep():
    while(kk==1):
        time.sleep(1)

def mongo():
    print(user_i)
    myclient = pymongo.MongoClient(host="127.0.0.1", port=27017)
    mydb = myclient.jubao
    ipcol = mydb['ip']
    usercol = mydb['user']
    print(data_i.get())
    print(user_i.get())
    data = ipcol.find().skip(data_i.get())
    user = usercol.find().skip(user_i.get())  # 20开始
    return data, user

def proxy():

    # 生成一个ua
    ua = UserAgent()
    ua = ua.chrome
    option.add_argument('user-agent=' + ua)
    option.add_argument("--user-data-dir=" + r"C:/Users/hike/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(options=option)
    return driver
def add_coookie_login(bduss):
    global kk
    l5.insert(END,"请点击GOOG进行添加cookie")
    sleep()
    kk=1
    l5.insert(END,"正在进行添加cookie请不要动鼠标")
    window_name = u'百度一下，你就知道 - Google Chrome'
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
    l5.insert(END,"cookie添加成功")
def open_driver(driver):
    # driver.delete_all_cookies()
    print("打开页面\n")
    # txt.insert()
    # driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    # time.sleep(3)
    l5.insert(END,"等待网页响应\n")

    print("等待网页响应\n")

def login(driver, user):
    global kk
    l5.insert(END,"请点击登录\n")
    # print("点击登录")
    sleep()
    print(kk)
    kk=1
    driver.find_element_by_link_text('登录').click()
    # time.sleep(5)
    # print("5s倒计时")
    # for x in range(5):
    #     time.sleep(1)
    #     print(5 - x)
    l5.insert(END, "用户名登录\n")
    # print("用户名登录")
    # driver.implicitly_wait(15)
    sleep()
    kk = 1
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
    name = user.get('name')
    pwd = user.get('pwd')
    a = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]')
    a.clear()
    l5.insert(END, "填写用户名\n")
    # print("填写用户名")
    print(name)
    a.send_keys(name)
    b = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]')
    b.clear()
    l5.insert(END, "填写密码\n")
    # print("填写密码")
    b.send_keys(pwd)
    # txt.insert(END,"登录")
    # print("登录")
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
    l5.insert(END,"请验证\n")
    sleep()
    kk = 1



def quitChrome(driver):
    global kk
    l5.insert(END,"清理缓存\n")
    # print("清理缓存")
    driver.delete_all_cookies()
    driver.delete_all_cookies()
    l5.insert(END,"关闭浏览器\n")
    # print("关闭浏览器")
    driver.quit()
    l5.insert(END,"切换ip\n")
    # print("切换ip")
    sleep()
    kk = 1

def jubao(driver, data, user):
    global kk
    l5.insert(END,"正在跳转举报链接\n")
    # print("正在跳转举报链接")
    driver.implicitly_wait(30)
    driver.get(data.get('url_jubao'))
    # time.sleep(3)
    # print("3s倒计时")
    # driver.implicitly_wait(10)
    l5.insert(END,"等待网页显示\n")
    # print("等待网页显示")
    # txt.insert(END,"查找企业/组织侵权")
    # print("查找企业/组织侵权")
    sleep()
    kk = 1
    driver.find_element_by_xpath('//*[@id="jubao-type-level1"]/a[3]').click()
    l5.insert(END,"正在填写内容\n")
    # print("正在填写内容")
    driver.find_element_by_xpath('//*[@id="form-description"]').send_keys(data.get('reason3'))
    driver.find_element_by_xpath('//*[@id="form-pic2"]').send_keys(data.get('url'))
    driver.find_element_by_xpath('//*[@id="form-phone"]').send_keys(user.get('phone'))
    l5.insert(END,"内容填写完毕，请填写验证码\n")
    sleep()
    kk = 1
    # print("内容填写完毕，请填写验证码")


root = Tk()
  # 需要将函数包装一下，必要的
root.geometry("500x500")
root.title("自动举报")
test_cmd = root.register(test)
start=Button(root,text='开始',bg="Gold",fg="black",relief="groove",command = lambda: thread_it(mains))
start.place(relx=0.1,rely=0.05,width=60,height=50)
pause=Button(root,text="暂停",bg="greenyellow",fg="black",relief="groove",command = lambda: thread_it(pauses))
pause.place(relx=0.3,rely=0.05,width=60,height=50)
go=Button(root,text="gogo",bg="greenyellow",fg="black",relief="groove",command = lambda: thread_it(gogo))
go.place(relx=0.5,rely=0.05,width=60,height=50)
end=Button(root,text="结束",bg="Gold",fg="black",relief="groove")
end.place(relx=0.7,rely=0.05,width=60,height=50)
l1=Label(root,text='输入开始账号的位置：',fg="green",relief="groove")
l1.place(relx=0.1,rely=0.15,width=150,height=50)

user_i = IntVar(0)
l2=Entry(root,
              textvariable=user_i,
              validate='key',  # 发生任何变动的时候，就会调用validatecommand
              validatecommand=(test_cmd, '%P')  # %P代表输入框的实时内容
              )
    # 需要跳过账号的位置
l2.place(relx=0.1, rely=0.25, relwidth=0.2, height=30)

l3 = Label(root, text='举报链接的位置：', fg="green", relief="groove")
l3.place(relx=0.5, rely=0.15, width=150, height=50)
data_i = IntVar(0)
l4= Entry(root,
              textvariable=data_i,
              validate='key',  # 发生任何变动的时候，就会调用validatecommand
              validatecommand=(test_cmd, '%P')  # %P代表输入框的实时内容
              )
l4.place(relx=0.5, rely=0.25, relwidth=0.2, height=30)

l5 = Text(root)
l5.place(relx=0.1, rely=0.4, relwidth=0.6, height=260)


def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()

def mains():
    l5.insert(END, "请输入数据")
    global kk
    sleep()
    kk=1
    data, users = mongo()
    dd = []
    # print(start.text)
    for d in data:
        dd.append(d)
    # user=mongo()[1]
    for u in users:
        driver = proxy()
        open_driver(driver)
        # login(driver,u)
        add_coookie_login(u.get('BDUSS'))
        for d in dd:
            l5.insert(END,"点击goo进行举报\n")
            jubao(driver, d,u)
        quitChrome(driver)
root.mainloop()


