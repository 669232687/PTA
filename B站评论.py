# -*- coding:utf-8 -*-

from selenium import webdriver
import time

browser=webdriver.Chrome()
url='https://www.bilibili.com/bangumi/play/ss26767'
browser.get(url)
num =1
browser.implicitly_wait(10)
def comment(a):

  for d in range(a):
        global num
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        comment=browser.find_elements_by_css_selector('.list-item.reply-wrap')
        for i in comment:
          try:
            name=i.find_element_by_class_name('user').find_element_by_tag_name('a').text
            reply_content=i.find_element_by_class_name('text').text
            reply_time=i.find_element_by_class_name('time').text
            with open('D://私たちは勉強ができない1.txt','a+',encoding='utf-8') as f:
                f.write("ID: "+name+" \ntime: "+str(reply_time)+'\n')
                f.write("评论：\n"+reply_content+'\n\n')
                print("写入成功",num)
                num+=1
          except (Exception) as e:
              print(e)
        try:
            if browser.find_element_by_class_name('next'):
                browser.find_element_by_class_name('next').click()
        except Exception:
            print("爬取结束")
            browser.close()
            exit(0)
        time.sleep(0.5)


comment(1000)


