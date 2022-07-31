import tkinter
import tkinter.messagebox
import random
import re
import time

start = 0
Time = 0
Challenge = 0


def Count():
    global Challenge
    Challenge = Challenge + 1


# --------------------------------StartPage---------------------------------
def StartPage():
    def Change_Page1():
        root.destroy()
        MainPage()

    def Change_Page2():
        root.destroy()
        RulePage()

    root = tkinter.Tk()
    root.title("Start Page")
    root.geometry("800x500")
    root.resizable(False, False)
    label = tkinter.Label(root, text="数字当てゲーム", font=("Times New Roman", 60))
    label.place(x=210, y=100)
    button = tkinter.Button(root, text="は じ め る", font=(
        "Times New Roman", 30), command=Change_Page1)
    button.place(x=320, y=300)
    button = tkinter.Button(root, text="や り か た", font=(
        "Times New Roman", 30), command=Change_Page2)
    button.place(x=320, y=370)
    root.mainloop()
# --------------------------------RulePage----------------------------------


def RulePage():
    def Change_Page():
        root.destroy()
        StartPage()

    root = tkinter.Tk()
    root.title("RulePage")
    root.geometry("800x500")
    root.resizable(False, False)
    label = tkinter.Label(
        root, text="ランダムに決められた4桁の数字を当てるゲームです", font=("Times New Roman", 23))
    label.place(x=120, y=50)
    label = tkinter.Label(root, text="例題：ランダムな数字が００９７のとき",
                          font=("Times New Roman", 20))
    label.place(x=200, y=150)
    label = tkinter.Label(root, text="　解答　　　　　数字正解数　　場所正解数",
                          font=("Times New Roman", 17))
    label.place(x=250, y=220)
    label = tkinter.Label(root, text="１２３４　　　　　　０　　　　　　０　　",
                          font=("Times New Roman", 17))
    label.place(x=250, y=260)
    label = tkinter.Label(root, text="０１２３　　　　　　１　　　　　　１　　",
                          font=("Times New Roman", 17))
    label.place(x=250, y=290)
    label = tkinter.Label(root, text="６７８９　　　　　　２　　　　　　０　　",
                          font=("Times New Roman", 17))
    label.place(x=250, y=320)
    label = tkinter.Label(root, text="８７９０　　　　　　３　　　　　　１　　",
                          font=("Times New Roman", 17))
    label.place(x=250, y=350)
    label = tkinter.Label(root, text="００９７　　　　　　　　　・・・正解！　",
                          font=("Times New Roman", 17))
    label.place(x=250, y=380)
    button = tkinter.Button(root, text="戻る", font=(
        "Times New Roman", 12), command=Change_Page)
    button.place(x=650, y=450)
    root.mainloop()
# --------------------------------MainPage----------------------------------


def MainPage():
    global start
    start = time.time()

    def Change_Page1():
        root.destroy()
        ClearPage()

    def Change_Page2():
        root.destroy()
        StartPage()

    V = re.compile('[0123456789]+')
    om = random.randint(0, 9)

    ones_com = random.randint(0, 9)
    tens_com = random.randint(0, 9)
    hundreds_com = random.randint(0, 9)
    thousands_com = random.randint(0, 9)

    key = ""

    def func(enter):
        Count()
        txt = entry.get()
        if V.fullmatch(txt):
            answer = int(txt)
            if 3 < len(txt) < 5:
                ones_pl = answer % 10
                tens_pl = (answer % 100 - answer % 10) // 10
                hundreds_pl = (answer % 1000 - answer % 100) // 100
                thousands_pl = (answer - answer % 1000) // 1000

                n = 0
                p = 0
                n_1 = 0
                n_2 = 0
                n_3 = 0
                n_4 = 0

                if ones_com == ones_pl:
                    p = p + 1
                if tens_com == tens_pl:
                    p = p + 1
                if hundreds_com == hundreds_pl:
                    p = p + 1
                if thousands_com == thousands_pl:
                    p = p + 1

                check_1 = [ones_pl, tens_pl, hundreds_pl, thousands_pl]
                check_2 = [ones_com, tens_com, hundreds_com, thousands_com]

                if str(ones_com) in str(check_1):
                    n_1 = n_1 + 1
                if str(tens_com) in str(check_1):
                    n_2 = n_2 + 1
                if str(hundreds_com) in str(check_1):
                    n_3 = n_3 + 1
                if str(thousands_com) in str(check_1):
                    n_4 = n_4 + 1

                n = n_1 + n_2 + n_3 + n_4
                n_5 = 0

                if str(check_2).count(str(ones_com)) == 2 and str(check_1).count(str(ones_com)) == 1:
                    n_5 = n_5 + 1
                else:
                    if str(check_2).count(str(tens_com)) == 2 and str(check_1).count(str(tens_com)) == 1:
                        n_5 = n_5 + 1
                    else:
                        if str(check_2).count(str(hundreds_com)) == 2 and str(check_1).count(str(hundreds_com)) == 1:
                            n_5 = n_5 + 1

                if str(check_2).count(str(ones_com)) == 2 and str(check_2).count(str(tens_com)) == 2 and ones_com != tens_com and str(check_1).count(str(ones_com)) == 1 and str(check_1).count(str(tens_com)) == 1:
                    n_5 = n_5 + 1
                else:
                    if str(check_2).count(str(ones_com)) == 2 and str(check_2).count(str(hundreds_com)) == 2 and ones_com != hundreds_com and str(check_1).count(str(ones_com)) == 1 and str(check_1).count(str(hundreds_com)) == 1:
                        n_5 = n_5 + 1
                    else:
                        if str(check_2).count(str(ones_com)) == 2 and str(check_2).count(str(thousands_com)) == 2 and ones_com != thousands_com and str(check_1).count(str(ones_com)) == 1 and str(check_1).count(str(thousands_com)) == 1:
                            n_5 = n_5 + 1

                if str(check_2).count(str(ones_com)) == 3 and str(check_1).count(str(ones_com)) == 2:
                    n_5 = n_5 + 1
                else:
                    if str(check_2).count(str(tens_com)) == 3 and str(check_1).count(str(tens_com)) == 2:
                        n_5 = n_5 + 1

                if str(check_2).count(str(ones_com)) == 4 and str(check_1).count(str(ones_com)) == 3:
                    n_5 = n_5 + 1

                if str(check_2).count(str(ones_com)) == 3 and str(check_1).count(str(ones_com)) == 1:
                    n_5 = n_5 + 2
                else:
                    if str(check_2).count(str(tens_com)) == 3 and str(check_1).count(str(tens_com)) == 1:
                        n_5 = n_5 + 2

                if str(check_2).count(str(ones_com)) == 4 and str(check_1).count(str(ones_com)) == 2:
                    n_5 = n_5 + 2

                if str(check_2).count(str(ones_com)) == 4 and str(check_1).count(str(ones_com)) == 1:
                    n_5 = n_5 + 3

                n = n - n_5

                if p == 4:
                    Change_Page1()
                else:

                    text.insert("1.0", " 　" + (txt) + "　　　　　　" +
                                str(n) + "　　　　　　　" + str(p) + "\n")
                    entry.delete(0, tkinter.END)
            else:
                tkinter.messagebox.showerror("error", "4桁の半角数字で解答を入力してください")

        else:
            tkinter.messagebox.showerror("error", "4桁の半角数字で解答を入力してください")

    root = tkinter.Tk()
    root.title("Main Page")
    root.geometry("800x500")
    root.resizable(False, False)
    label = tkinter.Label(root, text="解答を入力してenterキーを押してください",
                          font=("Times New Roman", 16))
    label.place(x=50, y=100)
    entry = tkinter.Entry(width=15,)
    entry.place(x=120, y=170)
    button = tkinter.Button(text="リタイア", font=(
        "Times New Roman", 15), command=Change_Page2)
    button.place(x=155, y=300)
    label = tkinter.Label(root, text="解答　　　　数字正解数　　場所正解数",
                          font=("Times New Roman", 13))
    label.place(x=450, y=50)
    text = tkinter.Text(width=35, height=23, font=(
        "Times New Roman", 13), relief="ridge")
    text.place(x=437, y=70)
    root.bind("<Return>", func)
    root.mainloop()
# --------------------------------ClearPage---------------------------------


def ClearPage():
    global Challenge
    global start

    def Change_Page():
        root.destroy()
        StartPage()

    if Challenge > 10000:
        Challenge = 9999

    Time = time.time() - start
    Hour = 0
    Minute = 0
    Second = Time
    if Second >= 60:
        Minute = Time // 60
        Second = Second - Minute * 60
    if Minute >= 60:
        Hour = Minute // 60
        Minute = Minute - Hour * 60
    if Hour >= 100:
        Hour = 99
        Minute = 59
        Second = 59
    Second = round(Second, 2)
    Minute = round(Minute)
    Hour = round(Hour)

    root = tkinter.Tk()
    root.title("Clear Page")
    root.geometry("800x500")
    root.resizable(False, False)
    label = tkinter.Label(root, text="正解しました！", font=("Times New Roman", 45))
    label.place(x=238, y=150)
    label = tkinter.Label(root, text="試行回数：" + str(Challenge) + "回　　　経過時間：" + str(
        Hour) + "時間" + str(Minute) + "分" + str(Second) + "秒", font=("Times New Roman", 15))
    label.place(x=220, y=235)
    Challenge = 0
    button = tkinter.Button(text="ホームに戻る", font=(
        "Times New Roman", 13), command=Change_Page)
    button.place(x=600, y=400)
    root.mainloop()
# --------------------------------------------------------------------------


if __name__ == '__main__':
    StartPage()
