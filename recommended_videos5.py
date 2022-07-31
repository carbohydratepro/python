import tkinter
import random
import tkinter.font
import webbrowser
from functools import partial

width = 1000
height = 700
cx = 500
cy = 350

title_non_s = [     "ノンスタイル＿エレベーター",
                    "ノンスタイル＿デート",
                    "ノンスタイル＿夢",
                    "ノンスタイル＿時代劇",
                    "ノンスタイル＿Bar",
                    "ノンスタイル＿寝坊",
                    "ノンスタイル＿自己紹介",
                    "ノンスタイル＿取り調べ",
                    "ノンスタイル＿決め台詞",
                    "ノンスタイル＿熱血教師",
                    "ノンスタイル_ヤンキー",
                    "ノンスタイル＿一人旅",
                    "ノンスタイル＿男の友情",
                    "ノンスタイル＿インタビュー",
                    "ノンスタイル＿モテル男は...",
                    "ノンスタイル＿不倫報道"
                ]
                 
title_non_t = [     "ノンスタイル＿張り込み",
                    "ノンスタイル＿MBGM",
                    "ノンスタイル＿謝罪会見",
                    "ノンスタイル＿好感度が欲しい",
                    "ノンスタイル＿運命の出会い",
                    "ノンスタイル＿ポジティブ＝アホ"
                ]

title_non_j = [     "ノンスタイル＿指",
                    "ノンスタイル＿復帰漫才"
                ]

title_jyaru_s = [   "ジャルジャル＿ドア間違える奴",
                    "ジャルジャル＿嘘つき通す奴",
                    "ジャルジャル＿逆ー！！",
                    "ジャルジャル＿ふざける奴",
                    "ジャルジャル＿くしゃみと...",
                    "ジャルジャル＿国名分けっこ",
                    "ジャルジャル＿南っていう奴",
                    "ジャルジャル＿フィリピン数学",
                    "ジャルジャル＿言語覚える天才",
                    "ジャルジャル＿すごい展開",
                    "ジャルジャル＿葬式",
                    "ジャルジャル＿同い年家庭教師",
                    "ジャルジャル＿言葉漫才",
                    "ジャルジャル＿はずれの先生",
                    "ジャルジャル＿野球部",
                    "ジャルジャル＿空き巣"
                ]

title_jyaru_t = [   "ジャルジャル＿性別わからん奴",
                    "ジャルジャル＿知らん奴",
                    "ジャルジャル＿男なのに...",
                    "ジャルジャル＿部屋入ってくる奴",
                    "ジャルジャル＿ノリツッコミ",
                    "ジャルジャル＿スタンガン",
                    "ジャルジャル＿変装",
                    "ジャルジャル＿屁の足音",
                    "ジャルジャル＿変なキャラ練習",
                    "ジャルジャル＿お尻怪我した奴",
                    "ジャルジャル＿最高ランク先生",
                    "ジャルジャル＿予約電話する南",
                    "ジャルジャル＿選挙補佐する南",
                    "ジャルジャル＿実習生じゃない奴",
                    "ジャルジャル＿変態追い出す奴",
                    "ジャルジャル＿変わってる奴",
                    "ジャルジャル＿万引きしそうな奴",
                    "ジャルジャル＿停電時の南"
                ]

title_jyaru_j = [   "ジャルジャル＿変な奴",
                    "ジャルジャル＿腹殴る奴",
                    "ジャルジャル＿理解不能者",
                    "ジャルジャル＿頭おかしい奴",
                    "ジャルジャル＿熱烈kiss",
                    "ジャルジャル＿オバハン",
                    "ジャルジャル＿ハンドイートマン",
                    "ジャルジャル＿kumo",
                    "ジャルジャル＿人間シュレッダー",
                    "ジャルジャル＿柔道"
                    ]

link_non_s = [      "https://youtu.be/uQfBi9EdqAQ",
                    "https://youtu.be/3uWSH7iQAg0",
                    "https://youtu.be/Jih4bcwDBA8",
                    "https://youtu.be/eQld5YUSBTc",
                    "https://youtu.be/dmSJv8suvE0",
                    "https://youtu.be/GIu3PZJpB7k",
                    "https://youtu.be/AUudsReoKTo",
                    "https://youtu.be/Pvk9_N-hMPE",
                    "https://youtu.be/ywc3Sp08F98", 
                    "https://youtu.be/I1E2Tcv7gQo",
                    "https://youtu.be/PpG0mEAAI-w",
                    "https://youtu.be/myZXb7DkIK8",
                    "https://youtu.be/ZV05_5Lp4Ls",
                    "https://youtu.be/O4BDHW4HJso",
                    "https://youtu.be/QvmfHUHOhsE",
                    "https://youtu.be/ZNBkbw8bT5I"
             ]

link_non_t = [      "https://youtu.be/yXHdpggKefs",
                    "https://youtu.be/nr2_iKVCeEU",
                    "https://youtu.be/DaaV5xQhF8c",
                    "https://youtu.be/iNOAzB5q_Ug",
                    "https://youtu.be/vh4B7uU_bkk",
                    "https://youtu.be/Zi52d51FoFI"
             ]

link_non_j = [      "https://youtu.be/FNg-uztQutA",
                    "https://youtu.be/SxmwBeD-N-A"
             ]

link_jyaru_s = [    "https://youtu.be/DaCmjtB-5To",
                    "https://youtu.be/0px-xNc5sZ0",
                    "https://youtu.be/PJboiuRpQhc",
                    "https://youtu.be/Vmgq8cnzBvQ",
                    "https://youtu.be/XqIHqB1ywtY",
                    "https://youtu.be/b1J39WQFvSs",
                    "https://youtu.be/lXOeDJR5LJc",
                    "https://youtu.be/XC40Vw4quJw",
                    "https://youtu.be/krFc0_M4XWY",
                    "https://youtu.be/ucKw1CDNI3E",
                    "https://youtu.be/RcJByXnF2kY",
                    "https://youtu.be/pCE7xwxiph0",
                    "https://youtu.be/KVFAXIWSu4E",
                    "https://youtu.be/AOtvUnalVYc",
                    "https://youtu.be/oYG6-IpG-vw",
                    "https://youtu.be/EyGMilxXmOA"
                ]

link_jyaru_t = [    "https://youtu.be/MkBYw5Xu460",
                    "https://youtu.be/19KGYFH1hRo",
                    "https://youtu.be/3PSPuIO2Yno",
                    "https://youtu.be/yp9wu86XorI",
                    "https://youtu.be/GW30zOaqQiI",
                    "https://youtu.be/--KcnBOTY6k",
                    "https://youtu.be/Kez68G9wRSE",
                    "https://youtu.be/qF2QnRRC3Uo",
                    "https://youtu.be/tOSDUk-NM64",
                    "https://youtu.be/LG2A51QJhd4",
                    "https://youtu.be/8RjYNCHZR0U",
                    "https://youtu.be/N5kqPXc2l0o",
                    "https://youtu.be/mlMElwFGx4c",
                    "https://youtu.be/_3P9tk6xmlM",
                    "https://youtu.be/xX_eXXWHVDk",
                    "https://youtu.be/-wf94CUDDPg",
                    "https://youtu.be/oRNqGT0Nhig",
                    "https://youtu.be/itEIyoheRlg"
                ]

link_jyaru_j = [    "https://youtu.be/J8ssZzUX2xE",
                    "https://youtu.be/J0VJe9CifX4",
                    "https://youtu.be/D4SSThn4dCo",
                    "https://youtu.be/3gClxCwNUjw",
                    "https://youtu.be/Ly4Wv1wQOng",
                    "https://youtu.be/1Sklpj_dth8",
                    "https://youtu.be/_sHOGo0QJ_s",
                    "https://youtu.be/xcp1CSHrzCg",
                    "https://youtu.be/1N9epOTQmXQ",
                    "https://youtu.be/OeS7W1odflE"
                ]

title_all = []
link_all = []
video_quantity = []
video_random = []

def list_append(container_list, add_list):
    for i in range(len(add_list)):
        container_list.append(add_list[i])

list_append(title_all, title_non_s)
list_append(title_all, title_non_t)
list_append(title_all, title_non_j)
list_append(title_all, title_jyaru_s)
list_append(title_all, title_jyaru_t)
list_append(title_all, title_jyaru_j)

list_append(link_all, link_non_s)
list_append(link_all, link_non_t)
list_append(link_all, link_non_j)
list_append(link_all, link_jyaru_s)
list_append(link_all, link_jyaru_t)
list_append(link_all, link_jyaru_j)

for i in range(len(title_all)):
    video_quantity.append(i)

button = []
for i in range(1,210):
    button.append("button_"+str(i))

def draw_text(txt, x, y, size, tg):
    global canvas
    fnt = ("HG行書体", size)
    canvas.create_text(x, y, text=txt, fill="black", font=fnt, tag=tg)

def draw_button(txt, bx, by, size, num):
    button[num] = tkinter.Button(root, text=txt, font=("HG行書体", size), command=partial(main, num))
    button[num].place(x=bx, y=by)

def main(num):
    global idx, video_random
    idx = num
    if idx == 0:
        draw_text("おすすめの漫才・コント集", cx, 200, 50, "TITLE")
        draw_button("ちょっと見てみる", cx-230, 400, 40, 1)

    elif idx == 1:
        canvas.delete("TITLE")
        button[num].place_forget()
        draw_button("  絞り込む  ", 270, 80, 50, 2)
        draw_button("ランダム検索", 270, 280, 50, 3)
        draw_button("  動画一覧  ", 270, 480, 50, 4)

    elif idx == 2:
        for i in range(2, 5):
            button[i].place_forget()
        draw_button("ジャルジャル", 270, 200, 50, 6)
        draw_button("ノンスタイル", 270, 400, 50, 7)

    elif idx == 3:
        canvas.delete("MOVIE_NAME")
        for i in range(2, 5):
            button[i].place_forget()
        video_random = (random.sample(video_quantity, 3))
        for i in range(3):
            draw_text(title_all[video_random[i]], cx-150, 130+150*i, 30, "MOVIE_NAME")
            draw_button("視聴する", 700, 100+150*i, 30, 50+i)
        draw_button("やり直す", 400, 550, 30, 5)
    
    elif idx == 4:
        for i in range(2, 5):
            button[i].place_forget()
        main(20)

    elif idx == 5:
        for i in range(3):
            button[50+i].place_forget()
        main(3)
    
    elif idx == 6:
        for i in range(6, 8):
            button[i].place_forget()
        draw_button("  初心者  ", 300, 80, 50, 10)
        draw_button("　中級者　", 300, 280, 50, 11)
        draw_button("  上級者  ", 300, 480, 50, 12)
    
    elif idx == 7:
        for i in range(6, 8):
            button[i].place_forget()
        draw_button("  初心者  ", 300, 80, 50, 13)
        draw_button("　中級者　", 300, 280, 50, 14)
        draw_button("  上級者  ", 300, 480, 50, 15)

    elif idx == 10:
        for i in range(10, 13):
            button[i].place_forget()
        for i in range(len(title_jyaru_s)//2):
            draw_text(title_jyaru_s[i], 170, 100+70*i, 15, "MOVIE_NAME")
            draw_text(title_jyaru_s[i+8], 620, 100+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 85+70*i, 15, 55+i)
            draw_button("視聴する", 800, 85+70*i, 15, 61+i)

    elif idx == 11:
        for i in range(10, 13):
            button[i].place_forget()
        for i in range(len(title_jyaru_t)//2):
            draw_text(title_jyaru_t[i], 170, 60+70*i, 15, "MOVIE_NAME")
            draw_text(title_jyaru_t[i+9], 620, 60+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 55+70*i, 15, 70+i)
            draw_button("視聴する", 800, 55+70*i, 15, 79+i)

    elif idx == 12:
        for i in range(10, 13):
            button[i].place_forget()
        for i in range(len(title_jyaru_j)//2):
            draw_text(title_jyaru_j[i], 170, 110+70*i, 15, "MOVIE_NAME")
            draw_text(title_jyaru_j[i+5], 620, 110+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 105+70*i, 15, 90+i)
            draw_button("視聴する", 800, 105+70*i, 15, 95+i)

    elif idx == 13:
        for i in range(13, 16):
            button[i].place_forget()
        for i in range(len(title_non_s)//2):
            draw_text(title_non_s[i], 170, 100+70*i, 15, "MOVIE_NAME")
            draw_text(title_non_s[i+8], 620, 100+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 85+70*i, 15, 102+i)
            draw_button("視聴する", 800, 85+70*i, 15, 110+i)

    elif idx == 14:
        for i in range(13, 16):
            button[i].place_forget()
        for i in range(len(title_non_t)):
            draw_text(title_non_t[i], 380, 110+90*i, 20, "MOVIE_NAME")
            draw_button("視聴する", 650, 90+90*i, 20, 120+i)

    elif idx == 15:
        for i in range(13, 16):
            button[i].place_forget()
        for i in range(len(title_non_j)):
            draw_text(title_non_j[i], 380, 250+90*i, 20, "MOVIE_NAME")
            draw_button("視聴する", 650, 230+90*i, 20, 130+i)

    elif idx == 20:
        for i in range(9):
            draw_text(title_all[i], 170, 50+70*i, 15, "MOVIE_NAME")
            draw_text(title_all[i+9], 620, 50+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 35+70*i, 15, 140+i)
            draw_button("視聴する", 800, 35+70*i, 15, 140+9+i)
        draw_button("次のページ", 700, 650, 18, 21)

    elif idx == 21:
        button[21].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(18):
            button[i+140].place_forget()
        for i in range(9):
            draw_text(title_all[i+18], 170, 50+70*i, 15, "MOVIE_NAME")
            draw_text(title_all[i+27], 620, 50+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 35+70*i, 15, 140+18+i)
            draw_button("視聴する", 800, 35+70*i, 15, 140+27+i)
        draw_button("次のページ", 700, 650, 18, 22)
        draw_button("前のページ",100, 650, 18, 27)
    
    elif idx == 22:
        button[22].place_forget()
        button[27].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(18):
            button[i+140+18].place_forget()
        for i in range(9):
            draw_text(title_all[i+36], 170, 50+70*i, 15, "MOVIE_NAME")
            draw_text(title_all[i+45], 620, 50+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 35+70*i, 15, 140+36+i)
            draw_button("視聴する", 800, 35+70*i, 15, 140+45+i)
        draw_button("次のページ", 700, 650, 18, 23)
        draw_button("前のページ",100, 650, 18, 26)

    elif idx == 23:
        button[23].place_forget()
        button[26].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(18):
            button[i+140+36].place_forget()
        for i in range(7):
            draw_text(title_all[i+54], 170, 50+70*i, 15, "MOVIE_NAME")
            draw_text(title_all[i+61], 620, 50+70*i, 15, "MOVIE_NAME")
            draw_button("視聴する", 350, 35+70*i, 15, 140+54+i)
            draw_button("視聴する", 800, 35+70*i, 15, 140+61+i)
            print("i")
        draw_button("前のページ",100, 650, 18, 25)

    elif idx == 25:
        button[25].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(14):
            button[i+140+54].place_forget()
        main(22)

    elif idx == 26:
        button[26].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(18):
            button[i+140+36].place_forget()
        main(21)

    elif idx == 27:
        button[27].place_forget()
        canvas.delete("MOVIE_NAME")
        for i in range(18):
            button[i+140+18].place_forget()
        main(20)

    elif idx >= 50 and idx < 55:
        webbrowser.open(link_all[video_random[idx-50]])

    elif idx >= 55 and idx < 68:
        webbrowser.open(link_jyaru_s[idx-55])

    elif idx >= 70 and idx < 90:
        webbrowser.open(link_jyaru_t[idx-70])

    elif idx >= 90 and idx <= 100:
        webbrowser.open(link_jyaru_j[idx-90])

    elif idx >= 102 and idx < 120:
        webbrowser.open(link_non_s[idx-102])

    elif idx >= 120 and idx < 130:
        webbrowser.open(link_non_t[idx-120])

    elif idx >= 130 and idx < 135:
        webbrowser.open(link_non_j[idx-130])
    
    elif idx >= 140 and idx < 210:
        print(link_all)
        webbrowser.open(link_all[idx-140])

root = tkinter.Tk()
root.title("動画のすゝめ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=1000, height=700, bg="white")
main(0)
canvas.pack()
root.mainloop()