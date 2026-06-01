# 코드를 실행했는데, 한번에 안 될때는 여러번 실행해 본다
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time

# TODO
# 웹 드라이버 객체 생성
driver = webdriver.Chrome()

# 크롤링한 결과를 저장할 엑셀 파일 생성
# Workbook 객체 생성
# TODO
result_xlsx = Workbook()
# Workbook 으로부터 worksheet 를 가져온다
# 현재 활성화된 worksheet 를 가져온다
# TODO
worksheet = result_xlsx.active
# 워크시트에 컬럼명 추가
# TODO
worksheet.append(['상품명','가격','링크'])

url = 'http://11st.co.kr'
search_keyword = '덴탈마스크'

try:
    # TODO
    # 11번가 페이지에 접속, 웹 크롤링
    # TODO
    driver.get(url)

    # 11번가 페이지에 접속 --> 검색창을 찾는다
    # 검색창 요소가 발견될때 까지 명시적으로 기다리고,
    # 검색창 요소가 발견되면 해당 요소를 리턴한다
    # 최대 기다리는 시간은 10초로 설정
    # TODO
    # 1) 11번가 페이지에 접속 --> 검색창을 찾는다
    # <input type="text" class="search_text" title="통합검색" ...>
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search_text"))
    )
    print('=== 첫 페이지 로딩 성공 ===')

    # TODO
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
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "layBodyWrap"))
    )
    print('=== 검색된 페이지 로딩 성공 ===')
    # 페이지 로딩이 지연될때는 아래 코드 실행
    # 지연되는 코드 사이에 넣는다 --> 묵시적 기다림
    # 지연이 없다면 time.sleep(2) 은 주석 처리해도 된다
    time.sleep(2)

    # 쇼킹딜 라디오 버튼의 html 태그 분석
    # <span class="radio_style_1">
    #     <input type="radio" id="s_jzRbG2QmaXqj9hiPkuU" ...>
    #     <label for="s_jzRbG2QmaXqj9hiPkuU">쇼킹딜</label>
    # </span>
    # radio_style_1이라는 클래스명이 보이는데, CSS 디자인을 위해 진짜 input 버튼은 화면에서 숨겨두고,
    # 그 옆의 <label> 태그를 예쁘게 꾸며서 사용자가 클릭하도록 디자인된 구조
    # 이 경우 셀레니움으로 input을 클릭하면 브라우저가 무시함
    # 동적 ID (id="s_jzRb...")
    # id 값이 s_jzRbG2QmaXqj9hiPkuU처럼 무작위 문자로 되어 있음
    # 이런 ID는 페이지를 새로고침하거나 검색어를 바꿀 때마다 계속 변하는 동적 ID일 확률이 99%임
    # 따라서 ID로 접근하면 안 됨.
    # 결론적으로, label 태그를 타겟팅하여 클릭하기
    # 사용자가 화면에서 진짜로 클릭하는 대상은 쇼킹딜이라는 글자가 적힌 <label> 태그임
    # 이 요소를 정확히 짚어서 클릭해 주어야 함

    # 방법1) XPATH 사용
    # XPATH는 HTML 태그 안에 들어있는 '텍스트(글자)'를 직접 인식해서 요소를 찾을 수 있음
    # 따라서 클래스명이나 구조가 바뀌어도 "쇼킹딜"이라는 글자만 있으면 무조건 찾아낸다는 강력한 장점이 있음
    # #'쇼킹딜' 텍스트를 가진 label 태그를 찾는다
    # shocking_deal_label = driver.find_element(By.XPATH, "//label[contains(text(), '쇼킹딜')]")
    #
    # 방법2) CSS Selector 사용
    # CSS Selector는 원칙적으로 텍스트 내용을 직접 매칭하는 기능(:contains() 같은 문법은 표준 CSS에서 제외됨)이 없고, 대신 태그 이름, 클래스명, 아이디, 속성값 등을 조합해서 구조적으로 찾아야 함.
    # 브라우저가 요소를 해석하는 속도는 XPATH보다 CSS Selector가 미세하게 더 빠르고 직관적임

    # 상품 유형 리스트 안의 모든 라벨들을 다 가져옴
    labels = driver.find_elements(By.CSS_SELECTOR, ".sort_cont_list .item label")

    # 반복문을 돌며 텍스트가 '쇼킹딜'인 것을 찾아 클릭
    for label in labels:
        if "쇼킹딜" in label.text:
            driver.execute_script("arguments[0].click();", label)
            print("쇼킹딜 클릭 성공!")
            break
    # 클릭 후 페이지 내용이 바뀔 때까지 반드시 대기!
    time.sleep(3)


    print("=== 쇼킹딜 페이지로 이동중... ===")

    # 4) 쇼킹딜 페이지로 이동, 기다린다
    # 쇼킹딜 페이지의 전체 상품을 가지는 div 요소
    # <div id="layBodyWrap" tabindex="-1">
    # TODO
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "layBodyWrap"))
    )
    print('=== 쇼킹딜 페이지 이동 성공 ===')
    time.sleep(2)

    # 5) 상품 정보들 <section class="search_section "...> 태그를 모두 가져온다
    # 각 상품들은 하나하나의 <li class="c-search-list__item"> 태그에 포함되어 있다
    # <section class="search_section" id="section_topAdArea">
    # 	...
    # 	<div class="c-search-list">
    # 		<ul class="c-search-list__container">
    # 			<li class="c-search-list__item">
    # 				.....
    # 위 태그를 가져오는 css selector 의 문법
    # section.search_section 혹은 .search_section
    # TODO
    # searchs = content.find_element(By.CSS_SELECTOR, "section.search_section")
    searchs = content.find_elements(By.CSS_SELECTOR, ".search_section")
    time.sleep(2)
    print('=== 쇼킹딜 페이지 - 전체 상품들의 목록 로딩 성공 ===')
    time.sleep(2)

    # <section class="search_section" id="section_topAdArea"> 태그들을
    # 반복하면서 하나의 section 을 가져온다
    # TODO
    for search in searchs:
        # TODO
        # 하나의 section 안에 있는 모든 목록들을 가져온다

        # 섹션의 ID를 가져온다
        section_id = search.get_attribute("id")

        # 11번가 구조상 'topAd'(상단광고), 'relation'(연관추천), 'recommend'(추천) 등이 포함된 섹션은 건너뛴다
        # (주의: 11번가 HTML 구조에 따라 이 ID 키워드는 바뀔 수 있음)
        if section_id and any(
                ad_keyword in section_id for ad_keyword in ['topAd', 'recommend', 'relation', 'powerPrd']):
            print(f"--- 광고/추천 섹션 제외함 (ID: {section_id}) ---")
            continue

        # 실제 상품 목록만 크롤링 진행. 모든 상품의 리스트들을 가져온다
        # <li class="c-search-list__item">
        elems = search.find_elements(By.CLASS_NAME, "c-search-list__item")
        if not elems:
            continue
        time.sleep(2)
        print('=== 쇼킹딜 페이지 - 실제 모든 상품 리스트들 가져오기 성공 ===')

        # 모든 상품의 리스트들에서 상품을 하나씩 꺼낸다
        # <li class="c-search-list__item">
        # TODO
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
            dl = el.find_element(By.CLASS_NAME,"c-card-item__price")
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
    # TODO
    # 저장할 엑셀 파일의 이름
    file_name = 'result_11번가_추천제외.xlsx'
    # 엑셀파일 저장
    result_xlsx.save(file_name)
    print(f'크롤링된 결과는 {file_name} 파일로 저장됩니다.')
    # 웹 드라이버 종료(웹 브라우저 종료)
    driver.quit()
