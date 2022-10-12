import requests
import pandas as pd

offset_ = 1
limit_ = 150
url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset={offset_}&limit={limit_}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
res = requests.get(url)
objects_data = res.json()
objects_data.get('data').get('list')[0]

objects_list = objects_data.get('data').get('list')
objids = [x.get('objId') for x in objects_list]
# print(len(objids), objids, sep='\n')

url = []
for i in range (len(objids)):
    idd = objids[i]
    url.append(f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{idd}')

res = requests.get(url[0])
ress = res.json()
print(*url, sep='\n')
print(ress)
# print(len(url), url, sep='\n')

df = pd.DataFrame(ress)
df.to_csv("panda.csv", index=True, header=False)
print(df)