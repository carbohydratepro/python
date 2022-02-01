import requests


def pro1():#urlのhtmlファイルを取得する
  url = "https://api.aoikujira.com/time/get.php"
  result = requests.get(url)

  print(result.text)

if __name__ == '__main__':
  pro1()