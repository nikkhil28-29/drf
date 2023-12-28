import requests 

# endpoints="https://httpbin.org/"
endpoints="http://127.0.0.1:8000/api/products/1/" 
get_response=requests.get(endpoints,json={'title':'hello titlyy','content':'abc123'}) # HTttp request
print(get_response.headers)

# print(get_response.text)
               
print(get_response.json())  


try:
    response_data = get_response.json()
    print(response_data)
except requests.exceptions.JSONDecodeError:
    print 