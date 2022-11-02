import requests
from bs4 import BeautifulSoup
from typing import List
import sys


def get_github_page_file_name_url_list(url: str) -> List[List[str]]:
    """
    get github file's name and url with github page url.
    :param url:
    :return:
    """
    # get html
    html = requests.get(url).text
    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # retrieve file name and url
    list = soup.find_all(name="a", attrs={"class": "js-navigation-open Link--primary"})
    list = [[item.string, 'https://github.com' + item['href']] for item in list]
    return list


def get_github_md_head(url: str) -> str:
    """
    get a markdown file's first head with this file's github url.
    :param url:
    :return:
    """
    # get html
    html = requests.get(url).text
    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # retrieve file name and url
    head = ""
    try:
        h1 = soup.find_all(name="h1", attrs={"dir": "auto"})[0]
        head = h1.next.next.next.next
    except Exception:
        print("url:{} has no head.".format(url))
    return head


def get_github_page_md_url_head_list(url: str) -> List[List[str]]:
    """
    get all of the github page's markdown file's h1 header and url.
    :param url:
    :return:
    """
    name_url_list = get_github_page_file_name_url_list(url)
    list = []
    for i, item in zip(range(len(name_url_list)), name_url_list):
        url = item[1]
        name = item[0]
        header = get_github_md_head(url)
        print("\rgot: {}/{}".format(i+1, len(name_url_list)))
        list.append([url, header])
    return list


def main():
    if len(sys.argv) < 2:
        print("Too few parameters")
        return 1
    path = sys.argv[1]
    list = get_github_page_md_url_head_list(path)
    for item in list:
        print("* [{}]({})".format(item[1], item[0]))


if __name__ == '__main__':
    main()
