import sys
while True:
    print('종료를 원하면 exit 를 입력하세요.')
    key = input()
    if key == 'exit':
        sys.exit()
    print('입력하신 키는 ' + key + ' 입니다')