import requests
import json
import xlrd

workbook = xlrd.open_workbook(r'C:\Users\Jack\Desktop\api_hub.xls')

sheet1_name = workbook.sheet_names()[0]

print(sheet1_name)

sheet1 = workbook.sheet_by_name(sheet1_name)

print(sheet1.name, sheet1.nrows, sheet1.ncols)

rows =  sheet1.row_values(0)
print(rows[0])

cols = sheet1.col_values(0)
print(cols)


host = "http://192.168.3.169:30001"
method = sheet1.row_values(1)[2]
route = sheet1.row_values(1)[1]
url = host + "/api/admin-api" + route

print(url)



url = "http://192.168.3.169:30001/api/admin-api/login/login"

payload = json.dumps({
  "account": "superAdmin",
  "captcha": "",
  "password": "123456"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request(method, url, headers=headers, data=payload)

print(response.text)
print(type(response))

