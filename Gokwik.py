import requests
import json
import jsonpath

#Test_case1
def test_register1():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test1.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 200,"test pass"
    print(response.text)

#Test_Case2
def test_register2():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test2.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 400,"test pass"
    print(response.text)

#Test_Case3
def test_register3():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test3.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 400,"test fail"                #Bad_request
    print(response.text)

#Test_Case4
def test_register4():
    URL = ("https://api.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test3.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 403,"test fail"
    print(response.text)

#Test_Case5
def test_register5():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test5.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 200,"test fail" 
    print(response.text)

#Test_Case6
def test_register6():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test6.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 200,"test fail internal server error"       
    print(response.text)


#Test_Case7
def test_register7():
    URL = ("https://api.gokwik.co/v1/enquiry")
    f = open('/home/shivam/Documents/Gokwik/test7.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 405,"test fail"                 
    print(response.text)