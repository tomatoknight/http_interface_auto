# coding: utf-8
from Common_Exec import send_HttpRequest
from Common_Excel import getTestData
import requests
import json
if __name__ == "__main__":
    host = "postman-echo.com"
    headers = {
        "Host": "postman-echo.com",
        "User-Agent": "PostmanRuntime/7.28.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip,deflate,br",
        "Cookie": "sails.sid=s%3ATTNjQKKUB0U-BxfiUIVkYEKX_BD9aB4P.QPMFqeuq2i4qKzPsePjMqJIxlRfJbbImAxKeiVD2j%2Fg"
    }
    robotTestCase = "sendPostRequest"
    robotTestSuite = r"E:/llf_58TestSuites/jz_webIntergration/robot_code/rfcode/send_Request.txt"
    testScene = "getSecondCatesByFirstCateId"
    testDataFile = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\testData\\testData.xlsx"
    # testCaseReportPath = "E:\\llf_58TestSuites\\jz_webIntergration\\robot_code\\report\\TestCaseReport"
    method, url, caseNo, testName, dict_params, expectCode, expectContent = getTestData(testDataFile, testScene, host, 1)
    code, content = send_HttpRequest(url, headers, method=method)
    content = json.loads(content)
    print(content["code"])
    print(content["msg"])
    print(content["errorcode"])
    print(content["data"])


