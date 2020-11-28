# selenium 라이브러리

# 브라우저를 직접 제어할 수 이는 라이브러리
# 크롬 브라우저를 제어 해보겠습니다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 웹 드라이버가 필요합니다. 
# https://sites.google.com/a/chromium.org/chromedriver/downloads

browser = webdriver.Chrome('D:\\IJH\\chromedriver.exe')

# 크롬 부라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 크기 조절
# browser.maximize_window()
# browser.minimize_window()
browser.set_window_size(800, 500) # 해상도( width x height )

browser.get('http://www.naver.com')

# 웹 페이지 소스 출력
print(browser.page_source)

# 쿠키 확인
print(browser.get_cookies())

# 현재 URL 확인
print(browser.current_url)

# search = browser.find_element_by_id('query')
search = browser.find_element_by_css_selector('div.green_window > input#query')
search.send_keys("검색어")
# search.submit()
search.send_keys(Keys.RETURN)



# 브라우저 종료
# browser.quit()
