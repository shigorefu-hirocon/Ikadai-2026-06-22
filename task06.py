import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task06: 3つのカテゴリに分類しよう
# =========================================

# TODO 1: 問い合わせデータを分類用に準備する
# - support_tickets.json を読み込む
# - 文章の長さ、料金ワード数、技術ワード数、契約ワード数を特徴量にする
# - 問い合わせカテゴリを正解ラベルにする

# TODO 2: 3クラス分類モデルを作る
# - 訓練データとテストデータに分ける
# - DecisionTreeClassifier で学習する
# - テストデータのカテゴリを予測する

# TODO 3: 結果を確認する
# - 正解率を計算する
# - 混同行列で、どのカテゴリを間違えたかを見る
# - 予測結果、正解率、混同行列を print() で表示する

# TODO 4: 混同行列を画像として表示する
# - plt.imshow() を使う
# - タイトルとカラーバーをつける
# - 余裕があれば、軸にカテゴリ名を表示する
