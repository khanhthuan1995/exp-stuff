from bs4 import BeautifulSoup
import requests
import lxml
list_url = open('output_live.txt','r')
for url in list_url.readlines():
    try:
        request1 = requests.get(url , timeout=5,verify=True,allow_redirects=True)
        soup = BeautifulSoup(request1.text, 'lxml')
        input_r = soup.select("input.name")
        print(input_r)
        print(soup)
        input_f = soup.input
        print(input_f)
        inputs = soup.find_all("input")
        print(inputs)
        for input_ in inputs:
            print(url)
            print(input_.get("name"))

        
    except Timeout as e:
    # Handle timeout exception here
        print(url +"Timeout Occured: ", e)
    except requests.exceptions.RequestException as e:
        print(url +"nothing")