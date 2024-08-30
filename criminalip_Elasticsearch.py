import requests
import json

base_url = 'https://api.criminalip.io/v1/banner/search?query=Elastic+port%3A9200&offset=0'
headers = {
    "x-api-key": "Your API Key"
}

# To retrieve up to 100 results, increment the offset value by 10 with each request
unique_results = {}
for offset in range(0, 100, 10):
    url = base_url + str(offset)
    response = requests.request("GET", url, headers=headers)
    
    json_response = response.json()
    for result in json_response["data"]["result"]:
        ip_address = result["ip_address"]
        open_port_no = result["open_port_no"]
        product = result["product"]
        banner = result['banner']
            
        if ip_address not in unique_results:
            unique_results[ip_address] = {"open_port_no": open_port_no, "product": product, "banner" : banner}
            print(json.dumps({"ip_address": ip_address, "open_port_no": open_port_no, "product": product, "banner" : banner}, indent=4, ensure_ascii=False))

unique_results_list = [{"ip_address": ip, "open_port_no": details["open_port_no"], "product": details["product"], "banner" : banner} for ip, details in unique_results.items()]
print(json.dumps(unique_results_list, indent=4, ensure_ascii=False))

