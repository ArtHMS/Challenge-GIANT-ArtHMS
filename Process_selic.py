import requests

def test_api():
    
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Success!")
        try:
            data = response.json()
            print(data)
        except ValueError:
            print("Error decoding JSON")
            print(response.text)
    else:
        print("Failed to fetch data")
        print("Status code:", response.status_code)
        print("Response:", response.text)

if __name__ == '__main__':
    test_api()