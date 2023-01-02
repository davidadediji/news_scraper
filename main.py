from bs4 import BeautifulSoup
# import pandas as pd
import requests
import sys
import csv


def get_url(url) -> str:
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


def convert_csv():  # convert response data into csv
    soup = parse()

    headline = soup.find(attrs={"data-qa": "headline-text"}).get_text()
    author = soup.find(attrs={"data-qa": "author-name"}).get_text()
    timestamp = soup.find(
        attrs={"data-testid" or "data-qa": "timestamp"}).get_text()
    content_tag = soup.find_all(attrs={"data-el": "text"})

    content = ""
    for part in content_tag:
        content += "\n\n" + part.get_text()
    data = [headline, author, timestamp, content]

    with open('scrape.csv', 'a',  encoding='UTF8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['headline', 'author', 'timestamp', 'content'])
        writer.writerow(data)


convert_csv()
