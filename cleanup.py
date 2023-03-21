import os
import matplotlib.pyplot as plt

# ディレクトリの容量を再帰的に計算する関数
def get_size(start_path='.'):
    total_size = 0
    with os.scandir(start_path) as it:
        for entry in it:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_size(entry.path)
    return total_size

# ディレクトリを指定して容量を取得する
path = './'
total_size = get_size(path)

# グラフ表示用のデータを作成する
sizes = []
labels = []
for root, dirs, files in os.walk(path):
    size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
    sizes.append(size)
    labels.append(root.replace(path, '') + '\n(' + str(size / 1024 / 1024) + ' MB)')

# グラフを作成して表示する
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Directory size of ' + path + '\nTotal size: ' + str(total_size / 1024 / 1024) + ' MB')
plt.show()