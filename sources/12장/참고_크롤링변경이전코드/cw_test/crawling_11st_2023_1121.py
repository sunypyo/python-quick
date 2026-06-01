# 코드를 실행했는데, 한번에 안 될때는 여러번 실행해 본다
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 드라이버 객체를 생성한다
driver = webdriver.Chrome()

# 크롤링한 결과를 저장할 엑셀 파일 생성한다
# Workbook 객체를 생성한다
result_xlsx = Workbook()
# Workbook으로부터 worksheet 를 가져온다
# 현재 활성화된(active) 워크시트를 가져온다
worksheet = result_xlsx.active
# 워크시트에 컬럼명 추가
worksheet.append(['상품명','가격','링크'])

url = 'http://11st.co.kr'

try:
    # 11번가 페이지에 접속하여, 웹 클롤링 한다
    driver.get(url)

    # 검색창 요소가 발견될 때 까지 명시적으로 기다리고,
    # 검색창 요소가 발견되면 해당 요소를 리턴한다
    # 최대 기다리는 시간은 10초이다
    elem = WebDriverWait(driver,10).until(
        EC.presence_of_element_located( (By.CLASS_NAME , "search_text") )
    )
    print('=== 첫 페이지 로딩 성공 ===')

    # 검색창에 검색어를 입력한다
    elem.send_keys('마스크')
    # 엔터를 입력한다. 엔터의 키 값은 Keys.RETURN 혹은 Keys.ENTER
    elem.send_keys(Keys.RETURN)

    # 검색페이지의 전체 페이지가 로딩 될때까지 기다린다
    # 검색된 페이지의 전체 상품을 가지는 div 요소
    content = WebDriverWait(driver,10).until(
        EC.presence_of_element_located( (By.ID , "layBodyWrap") )
    )
    print('=== 검색된 페이지 로딩 성공 ===')
    time.sleep(3)

    # 상위 메뉴 목록을 찾는다
    div = content.find_element(By.CLASS_NAME, "b_search_tab")
    print('=== 상위 메뉴 목록 로딩 성공 ===')
    time.sleep(3)

    # ul > li 태그들을 모두 가져온다
    li_menu = div.find_elements(By.TAG_NAME, "li")
    time.sleep(3)

    # li 태그들을 반복하면서 하나의 li 를 꺼낸다
    for li in li_menu:
        # text 가 쇼킹딜인 것을 선택
        if li.text == '쇼킹딜':
            # 쇼킹딜 페이지로 이동할 a 요소를 찾는다
            a = li.find_element(By.TAG_NAME,'a')
            # 이동할 링크를 클릭한다
            # 참고로 href 주소가 URL 형식이라면,
            # href 의 값을 가져와서 driver.get(url) 을 사용할 수도 있다
            # 현재 코드는 <a href="#"...> 로 되어 있어 주소를 얻을 수 없어서 요소를 클릭하여 이동한다
            a.click()
            print("이동할 페이지 URL: ", driver.current_url)
    print('=== 쇼킹딜 페이지 이동 중... ===')


    # 쇼킹딜 페이지로 이동, 기다린다
    # 쇼킹딜 페이지의 전체 상품을 가지는 div 요소를 기다린다
    content = WebDriverWait(driver,10).until(
        EC.presence_of_element_located( (By.ID , "layBodyWrap") )
    )
    print('=== 쇼킹딜 페이지 이동 성공 ===')

    # <section class="search_section "...> 의 CSS_SELECTOR 문법은 아래와 같다
    # section.search_section 혹은 .search_section 으로 사용할 수 있다
    search = content.find_element(By.CSS_SELECTOR, ".search_section")
    print('=== 쇼킹딜 페이지 전체 상품 목록 로딩 성공 ===')

    time.sleep(5)

    # 상품 목록을 가져온다
    elems = search.find_elements(By.TAG_NAME, "li")
    # 상품 목록에서 상품을 하나씩 꺼낸다
    for el in elems:
        # 하나의 상품 정보에서
        # 상품이름, 가격, 상세페이지로 이동할 링크 주소를 가져온다

        # 상품이름
        div = el.find_element(By.CLASS_NAME, "c-card-item__name")
        name = div.find_element(By.TAG_NAME, 'dd').text

        # 상품 가격
        dl = el.find_element(By.CLASS_NAME, "c-card-item__price")
        price = dl.find_element(By.TAG_NAME, "span").text
        # TAG_NAME 이나 CLASS_NAME 이름으로 가져올 수 도 있다
        # price = dl.find_element(By.CLASS_NAME, "value").text

        # 상품 상세 페이지로 이동할 링크 주소
        a = el.find_element(By.CSS_SELECTOR,"a")
        link = a.get_attribute('href')

        # 화면에 출력
        print(name, ":", price, ":", link)
        # 엑셀 파일에 출력
        worksheet.append([name, price,link])

except Exception as e:
    print('***** 광고 제외 *****')
    # 에러가 발생하거나 파일에 내용이 기록되지 않을 때는 아래 구문을 주석 해지
    # 에러 메시지를 보고 에러를 수정하고 실행
    print(e)
    # 성공 이후 다시 위 구문은 다시 주석으로 처리 할것
    # 광고 때문에 에러가 발생할 수도 있다
finally:
    file_name = "11st_result.xlsx"
    # 엑셀 파일 저장
    result_xlsx.save(file_name)
    print("크롤링된 결과는 %s 파일로 저장됩니다." % file_name)
    # 웹 드라이버 종료
    driver.quit()
