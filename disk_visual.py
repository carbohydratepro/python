import os
import matplotlib.pyplot as plt

# 対象のディレクトリを指定
directory = "C:/"

# 各サブディレクトリのサイズを取得
dirs = [os.path.join(directory, d) for d in os.listdir(directory)]
sizes = []

for d in dirs:
    if os.path.isdir(d):
        total_size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, filenames in os.walk(d) for f in filenames)
        sizes.append(total_size / (1024 * 1024))  # MB単位に変換

# ディレクトリ名を短くする
dir_names = [os.path.basename(d) for d in dirs]

# グラフを描画
plt.bar(dir_names, sizes)
plt.xlabel('Directories')
plt.ylabel('Size (MB)')
plt.title('Directory Size Usage')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
