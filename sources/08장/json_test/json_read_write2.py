# TODO
import json

# json 파일을 로딩(읽기)
data_json = open('bitcoin_sample.json')
data = json.load(data_json)
print(data)

# 데이터들을 json 파일로 출력
f = open('json_result.json', 'w')
json.dump(data, f, indent='\t')
f.close()
##############################
print("=" * 30)

# json 파일을 로딩(읽기)
data_json = open('bitcoin_sample.json').read()
data = json.loads(data_json)
print(data)

# 데이터들을 json 파일로 출력
f = open('json_result2.json', 'w')
retJson = json.dumps(data, indent='\t')
f.write(retJson)
f.close()

##############################
print("=" * 30)

# 리스트 컴프리헨션 사용
# json 은 dict 형태이므로, dict 의 value 값들만 가져와서 리스트로 만들기
values = [item.values() for item in data ]
print(values)