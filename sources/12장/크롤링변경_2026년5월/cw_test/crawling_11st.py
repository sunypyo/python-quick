# 코드를 실행했는데, 한번에 안 될때는 여러번 실행해 본다
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time

# 웹 드라이버 객체 생성
driver = webdriver.Chrome()

# 크롤링한 결과를 저장할 엑셀 파일 생성
# Workbook 객체 생성
result_xlsx = Workbook()
# Workbook 으로부터 worksheet 를 가져온다
# 현재 활성화된 worksheet 를 가져온다
worksheet = result_xlsx.active
# 워크시트에 컬럼명 추가
worksheet.append(['상품명','가격','링크'])

# 접속할 웹 페이지 주소
url = 'http://11st.co.kr'
# 검색어
search_keyword = '덴탈마스크'

try:
    # 11번가 페이지에 접속, 웹 크롤링
    driver.get(url)

    # 1) 11번가 페이지에 접속 --> 검색창을 찾는다
    # <input type="text" class="search_text" title="통합검색" ...>
    #     # 검색창 요소가 발견될때 까지 명시적으로 기다리고,
    #     # 검색창 요소가 발견되면 해당 요소를 리턴한다
    #     # 최대 기다리는 시간은 10초로 설정
    elem = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search_text"))
    )
    print('=== 첫 페이지 로딩 성공 ===')

    # 검색창에 검색어를 입력
    elem.send_keys(search_keyword)
    # 엔터를 입력. 엔터 키 값은 Keys.RETURN 혹은 Keys.ENTER
    elem.send_keys(Keys.RETURN)
    print('=== 검색어 입력 성공 ===')

    # 2) 검색어를 입력하고 --> 검색 페이지로 이동
    # 검색페이지의 전체 페이지가 로딩 될때까지 기다린다
    # 검색된 페이지의 전체 상품을 가지는 div 요소
    # <div id="layBodyWrap" tabindex="-1">
    # 	<div class="l_content">
    # 		<div class="s_search s_search_main">
    content = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "layBodyWrap"))
    )
    print('=== 검색된 페이지 로딩 성공 ===')
    # 페이지 로딩이 지연될때는 아래 코드 실행
    # 지연되는 코드 사이에 넣는다 --> 묵시적 기다림
    # 지연이 없다면 time.sleep(2) 은 주석 처리해도 된다
    time.sleep(2)

    # 좌측 메뉴를 찾는다
    # <div class="search_filter_sort productType active" ....>
    # class 이름에 공백이 포함되는 경우에는 공백 앞까지만 입력한다
    div = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search_filter_sort"))
    )
    print('=== 메뉴 로딩 성공 ===')
    time.sleep(2)

    # 메뉴의 모든 리스트들을 가져온다
    # <li class="item">
    li_menu = div.find_elements(By.CLASS_NAME, "item")
    print('=== 메뉴의 모든 리스트 로딩 성공 ===')
    time.sleep(2)

    # li 요소들을 반복하면서 li 를 하나씩 꺼낸다
    # <li class="item">
    # 	<span class="radio_style_1">
    # 		<input type="radio" id="s_jzRbG2QmaXqj9hiPkuU" name="productType" ...>
    # 			<label for="s_jzRbG2QmaXqj9hiPkuU">쇼킹딜</label>
    # 	</span>
    # </li>
    for li in li_menu:
        # 하나의 li 요소에서 text 가 쇼킹딜 인 것을 선택
        if li.text == '쇼킹딜':
            # 쇼킹딜의 input 요소를 찾는다
            radio = li.find_element(By.TAG_NAME, "input")
            # input 요소 즉, 라디오 버튼을 클릭한다
            radio.click()
    print("=== 쇼킹딜 페이지로 이동중... ===")

    # 4) 쇼킹딜 페이지로 이동, 기다린다
    # 쇼킹딜 페이지의 전체 상품을 가지는 div 요소
    # <div id="layBodyWrap" tabindex="-1">
    content = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "layBodyWrap"))
    )
    print('=== 쇼킹딜 페이지 이동 성공 ===')
    time.sleep(2)

    # 상품 정보들   <section class="search_section "...> 태그들을 모두 가져온다
    # <section class="search_section" id="section_topAdArea">
    # 	...
    # 	<div class="c-search-list">
    # 		<ul class="c-search-list__container">
    # 			<li class="c-search-list__item">
    # 				.....
    # 위 태그를 가져오는 css selector 의 문법
    # section.search_section 혹은 .search_section
    # search = content.find_element(By.CSS_SELECTOR, "section.search_section")
    searchs = content.find_elements(By.CSS_SELECTOR, ".search_section")
    time.sleep(2)
    print('=== 쇼킹딜 페이지 - 전체 상품들의 목록 로딩 성공 ===')
    time.sleep(2)

    # <section class="search_section" id="section_topAdArea"> 태그들을
    # 반복하면서 하나의 section 을 가져온다
    for search in searchs:
        # 하나의 section 안에 있는 모든 목록들을 가져온다
        # 모든 상품의 리스트들을 가져온다
        # <li class="c-search-list__item">
        elems = search.find_elements(By.CLASS_NAME , "c-search-list__item")
        time.sleep(2)
        print('=== 쇼킹딜 페이지 - 모든 상품 리스트들 가져오기 성공 ===')

        # 모든 상품의 리스트들에서 상품을 하나씩 꺼낸다
        # <li class="c-search-list__item">
        for el in elems:
            # 하나의 상품 정보에서
            # 상품명, 가격, 상세페이지로 이동할 주소를 가져온다

            # 상품명
            # <div class="c-card-item__name">
            # 	<dt>상품명</dt>
            # 	<dd>[25매추가증정]CLA 클라 라이트 마스크 KF94 새부리형 컬러마스크 50매</dd>
            # </div>
            div = el.find_element(By.CLASS_NAME, "c-card-item__name")
            name = div.find_element(By.TAG_NAME, "dd").text

            # 가격
            # <dd class="c-card-item__price">
            # 	<span class="value">12,210</span>원~
            # </dd>
            dl = el.find_element(By.CLASS_NAME, "c-card-item__price")
            # <span class="value">12,210</span> 에서 태그명으로 가져오기
            price = dl.find_element(By.TAG_NAME, "span").text
            # <span class="value">12,210</span> 에서 CLASS_NAME 으로 가져오기
            # price = dl.find_element(By.CLASS_NAME, "value").text

            # 상세페이지로 이동할 주소
            # <a href="..." class="c-card-item__anchor" ...>
            a = el.find_element(By.TAG_NAME, "a")
            link = a.get_attribute("href")

            # 화면에 출력
            print(name, ":", price, ":", link)
            # 엑셀파일에 기록
            worksheet.append([name, price, link])

except Exception as e:
    print('***** 광고 제외 *****')
    # 에러가 발생하거나 파일에 내용이 기록되지 않을 때는 아래 구문을 주석 해지
    # 에러 메시지를 보고 에러를 수정하고 실행
    print(e)
    # 성공 이후 다시 위 구문은 다시 주석으로 처리 할것
    # 광고 때문에 에러가 발생
finally:
    # 저장할 엑셀 파일의 이름
    file_name = '11st_result.xlsx'
    # 엑셀파일 저장
    result_xlsx.save(file_name)
    print('크롤링된 결과는 %s 파일로 저장됩니다.' % file_name)
    # 웹 드라이버 종료(웹 브라우저 종료)
    driver.quit()
