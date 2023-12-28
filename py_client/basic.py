import requests 

# endpoints="https://httpbin.org/"
endpoints="http://127.0.0.1:8000/api" 
get_response=requests.get(endpoints,params={'abc':123},json={'query':'hello'}) # HTttp request
print(get_response.headers)

print(get_response.text)
              
print(get_response.json())              
