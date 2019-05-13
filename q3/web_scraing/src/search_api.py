import requests
from bs4 import BeautifulSoup
from googlesearch import search


def get_most_relevent_search(link):
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src)
    searched_links = soup.find_all('a')
    final_result = []
    for link in searched_links:
        if '#1' in link.text:
            final_result.append(link)
    return final_result

def get_top_5_result(query):
    links = []
    for j in search(query, tld="com", num=5, stop=5, pause=2):
        links.append(j)
    return links
