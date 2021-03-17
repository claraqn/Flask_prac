# # 네이버 지도 데이터 수집하기
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time


# ftitle=[]

# def near_theater():
#     #driver = webdriver.Chrome("./chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument('window-size=1920x1080')
#     options.add_argument("disable-gpu")
#     driver = webdriver.Chrome('chromedriver', chrome_options=options)

#     # 구버전 네이버지도 접속
#     driver.get("https://v4.map.naver.com")

#     driver.find_elements_by_css_selector("button.btn_close")[1].click()

#     # 검색창에 검색어 입력하기 // 검색창: input#search-input
#     search_box = driver.find_element_by_css_selector("input#search-input")
#     search_box.send_keys("영화관")
#     # 검색버튼 누르기 // 검색버튼: button.spm
#     search_button = driver.find_element_by_css_selector("button.spm")
#     search_button.click()

#     time.sleep(5)

#     #select=배열, select_one=하나의 값만가져올때

#     html=driver.page_source
#     bs=BeautifulSoup(html,'html.parser')
#     cs=bs.select('ul.lst_site > li')
#     ftitle=[]


#     for i in range(0,3):
#         title=cs[i].select_one('div.lsnx > dl.lsnx_det > dt > a').text
#         ftitle.append(title)

#     return ftitle

# ftitle=near_theater()

# print(ftitle)
