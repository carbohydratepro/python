import requests


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

if __name__ == '__main__':
    pro1()
