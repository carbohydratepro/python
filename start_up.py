import pyautogui
import time

"""
info: https://pyautogui.readthedocs.io/en/latest/quickstart.html
info: https://pypi.org/project/PyAutoGUI/0.9.50/
"""


def get_status():
    # マウスの位置を取得する
    print(pyautogui.position())
    # 画面のサイズを取得する
    print(pyautogui.size())


def move_cursor():
    # カーソルを動かす(絶対座標へ移動, duration=移動にかける秒数)
    pyautogui.moveTo(500, 500, duration=1)
    # 上へ移動する(絶対座標へ移動)
    pyautogui.mouseUp(x=300, y=300, button="left")
    # 下へ移動する(絶対座標へ移動)
    pyautogui.mouseDown(x=700, y=700, button="left")


def crick():
    # 左クリック
    pyautogui.click(x=700, y=700, clicks=1, interval=1, button="left")
    # 右クリック
    pyautogui.rightClick(x=700, y=700)
    # ダブルクリック
    pyautogui.doubleClick()


def send_key():
    # 文字列の書き込み
    pyautogui.write("Hello world!", interval=0.25)
    # ホットキー入力
    pyautogui.hotkey("ctrl", "a")


def main():
    print("開発環境起動中")
    pyautogui.hotkey("win", "1")
    time.sleep(2)
    pyautogui.write("cd C:\\Users\\admin\\Desktop\\workspace\\rails\\limit_diary")
    pyautogui.press("enter")
    pyautogui.write("if (!(Get-Process 'C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe' -ErrorAction SilentlyContinue)) { Start-Process 'C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe'}")
    pyautogui.press("enter")
    pyautogui.write("code .")
    pyautogui.press("enter")

if __name__ == "__main__":
    main()
    # print(pyautogui.position())
    # print(pyautogui.size())
    # pyautogui.rightClick(x=10, y=10)
    # time.sleep(1)
    # pyautogui.hotkey("win")