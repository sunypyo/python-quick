while True:
    value = input("나이를 입력하세요. 종료를 원하시면 exit 를 입력하세요 : ")
    if value == 'exit':
        break
    try:
        age = int(value)
        print("당신의 나이는 %s 입니다" % age)

        if age > 0 and age < 10:
            group = "10대 미만"
        elif age >= 10 and age <20:
            group = '10대'
        elif age >= 20 and age <30:
            group = '20대'
        elif age >= 30 and age <40:
            group = '30대'
        elif age >= 40 and age <50:
            group = '40대'
        elif age >= 50 and age <60:
            group = '50대'
        else :
            group = '60대 이상'

        print ("나이대는 {0} 입니다".format(group))

    except Exception as e:
        print("예외 처리 구문 실행")
        print("{0} 입력, 숫자를 입력해 주세요~~".format(value))
        # 발생한 예외 사항이 어떠한 것인지 출력
        print(e)
    finally:
        print("finally 코드는 언제나 수행 됩니다")

    print("계속해서 사용자의 입력값을 받습니다")
