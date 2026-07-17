import requests
import json

url = "https://comic.naver.com/api/webtoon/titlelist/weekday?week=sun&order=user"
headers = {'User-Agent': 'Mozilla/5.0 ...'}

response = requests.get(url, headers=headers)
data = response.json()

print(f"{len(data['titleList'])}개의 웹툰 발견!")
with open('webtoon-items.jsonl', 'a', encoding='utf-8') as f:
    for item in data['titleList']:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

import sqlite_utils

db = sqlite_utils.Database("webtoon_data.db")
table = db["webtoons"]

for item in data['titleList']:
    table.upsert(item, pk="titleId")
    print(f"'{item['titleName']}' DB 저장 / 업데이트 완료!")