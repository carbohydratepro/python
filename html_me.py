import requests
from bs4 import BeautifulSoup
import urllib
import os
import time
from selenium import webdriver


def pro1():  # urlのhtmlファイルを取得する
    url = "https://api.aoikujira.com/time/get.php"
    result = requests.get(url)

    print(result.text)


def pro2():  # urlから単一の画像を取り出す
    url = "https://uta.pw/shodou/img/3/3.png"
    res = requests.get(url)
    if not res.ok:
        print("失敗：", res.status_code)
        quit()

    with open("gyudon.png", "wb") as fp:
        fp.write(res.content)
    print("ok.")


def pro3():  # htmlファイルからタグ内の文字を読み取る
    with open("html_chapter10.html", encoding="utf-8") as fp:
        html_str = fp.read()

    soup = BeautifulSoup(html_str, "html5lib")

    title = soup.find("title")
    print(title)
    print(title.text)


def pro4():
    save_dir = "./pydoc_tutorial"
    top_page = "https://docs.python.org/ja/3/tutorial/index.html"
    check_url = "https://docs.python.org/ja/3/tutorial/"
    visited = {}

    def get_page(url):
        if check_url not in url:
            return
        if url in visited:
            return
        visited[url] = True
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        html = res.text
        fname = save_dir + "/" + os.path.basename(url)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        with open(fname, "wt", encoding="utf-8") as f:
            f.write(html)
            print("save:", fname)
        time.sleep(1)
        soup = BeautifulSoup(html, "html5lib")
        for a in soup.find_all("a"):
            a_url = urllib.parse.urljoin(url, a["href"])
            a_url = urllib.parse.urldefrag(a_url)[0]
            get_page(a_url)

    get_page(top_page)


def pro5():  # webbrowser
    driver = webdriver.Chrome()
    driver.get("https://python.org")
    time.sleep(10)
    driver.quit()


def pro6():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    el = driver.find_element_by_name("q")
    el.send_keys("google翻訳")
    el.submit()

    time.sleep(10)
    driver.close()


def pro7():
    driver = webdriver.Chrome()
    text = "りんご"
    url_text = "https://translate.google.co.jp/#ja/en/{0}".format(text)
    url = urllib.parse.quote_plus(url_text, "/:?=&#")
    driver.get(url)
    ja = driver.find_element_by_css_selector("span[jsname='W297wb']")
    print(ja.text)

    driver.close()
    driver.quit()

if __name__ == '__main__':
    pro1()
