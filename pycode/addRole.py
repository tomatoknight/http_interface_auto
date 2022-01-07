import requests
import json

url = "http://192.168.3.169:30001/api/admin-api/sysRole/add"


payload = "{\r\n    \"id\": null,\r\n    \"roleName\": \"test6\",\r\n    \"roleCode\": \"test6\",\r\n    \"description\": \"test5\",\r\n    \"dataScopeType\": \"\",\r\n    \"status\": 0,\r\n    \"level\": 1,\r\n    \"grantOrgIdList\": []\r\n}"
payload = json.loads(payload)

headers = {
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/plain, */*',
  'DNT': '1',
  'Authorization': '$2a$10$mAYf83B9TxP5YXpnx9tjwuVttmIQODY06JOO0FyoY.3cWtd8G6rDK',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'http://192.168.3.169:30001',
  'Referer': 'http://192.168.3.169:30001/',
  'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8',
  'Cookie': 'sentinel_dashboard_cookie=043EDFFF4867ACF0C86C663DAC412A5B; sidebar_status=opened; Authorization=$2a$10$1c4Tb1OyH2HayPcUoecPDuc0F4AVtXfjtK.0pshPWWDihWq4A1wLy; SECKEY_ABVK=xgnwmCxr+Toi0wxSgwCiqg9fpytLUbM2qhyt38ZC4b0%3D; BMAP_SECKEY=cde6ebb241c3d75c675c8688828640edba33c570fc006f6ccdee864f2e95d88033fc19e794fee19c2417a6953ba260f3e91efa7e82cbc9c45b5854aec79ce92429eac55d3668eeebfcb98be231842513c66d8c38ec0148bc8f807c889c4789832e4e3f6651029aa4eadbf58acd2f540235448c4038efec21a767bdde33a531220462d3b6391963aa61e4d0253284f591c4f1817963a41a03ee0aaf1dac998372e5f18ae50a13c73f59e70d1126938cccfd52ba667eeb0164e63302e7e792ff12707e36f3b78181516b886d8e1e17ebd5e0c75a7b4d56518d247adbc8e15d47e95d263ce2550aace47be14866dc7f4316; JSESSIONID=25E271A66E2B6084623D43CD2FE2BC0D'
}

#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
for i in range(10,20):
    payload["roleName"] = f'test{i}'
    payload["roleCode"] = f'test{i}'
    print(payload)
