import json

# json 파일을 읽어서 출력
data_json = open('bitcoin_sample.json').read()
data = json.loads(data_json)
# data = json.loads(open('bitcoin_sample.json').read())
print(data)

# 읽어온 데이터를 json 파일로 출력
f = open('json_result.json' , 'w')
# json.dump(data, f)
# json 파일이 한줄로 쭉 출력되지 않고, 들여쓰기를 원할때 아래 코드로 실행
json.dump(data, f, indent="\t")
f.close()
print("=" * 30)

data = json.load(open('bitcoin_sample.json'))
print(data)

print("=" * 30)
# 리스트 컴프리 헨션
values = [item.values() for item in data]
print(values)