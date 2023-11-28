class Manager:
    name = "이름"
    position = '직책'

    def __init__(self, name, position):
        print("두 개 인자값을 받는 생성자 함수 호출")
        print("=== 기본 적인 변수 ===")
        print("{0} 님의 직책은 {1} 입니다.".format(self.name, self.position))
        self.name = name
        self.position = position
        print("=== 초기화 이후 변경된 변수 ===")
        print("{0} 님의 직책은 {1} 입니다.".format(self.name, self.position))

    # 코드 추가. 소멸자 함수
    def __del__(self):
        print("=== 소멸자 함수 호출 ===")
        print("객체가 메모리에서 제거됩니다.")

mgr = Manager("써니", "차장")
# 코드 추가
mgr2 = mgr
mgr = None
mgr2 = Manager("루나","과장")
print("{0} 님의 직책은 {1} 입니다.".format(mgr2.name, mgr2.position))


