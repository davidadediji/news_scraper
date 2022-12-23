from bs4 import BeautifulSoup
import pandas as pd
import requests
import sys


def get_url(url)->str:
    try:
        response = requests.get(url)
        return response
    except:
        print('Invalid url, please try again')
        sys.exit()


def main():
    res = get_url(sys.argv[1])
    if (res.status_code != 200):
        print(f"Error getting news. status code is {res.status_code}")
        if (res.status_code == 404):
            print("Page does not exist")
        else:
            print(
                "Check if the URL is valid, if you have an internet connection or try later!'")

def parse():
    main()
    print(sys.argv[1])
    res = get_url(sys.argv[1])
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup



def convert_csv():
    soup = parse()
    
    headline = soup.find(attrs={"data-qa":"headline-text"}).get_text()
    author = soup.find(attrs={"data-qa":"author-name"}).get_text()
    timestamp = soup.find(attrs={"data-qa":"timestamp"}).get_text()

    content_tag = soup.find_all(attrs={"data-el":"text"})

    content = ""
    for part in content_tag:
        content += "\n\n" + part.get_text()
        return 1



# move to heaven
# tale of the nine-tailed
# 18  again
# crash landing on you
