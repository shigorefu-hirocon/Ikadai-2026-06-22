import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task02: テストデータでモデルを確認しよう
# =========================================

# TODO 1: データを準備する
# - students_pass.csv を読み込む
# - 勉強時間、出席率、宿題提出率を特徴量にする
# - 合格/不合格を正解ラベルにする

# TODO 2: 訓練データとテストデータに分ける
# - train_test_split を使う
# - テストデータは全体の30%にする
# - random_state を指定して、毎回同じ結果になるようにする

# TODO 3: モデルを学習し、テストデータを予測する
# - DecisionTreeClassifier を使う
# - 学習には訓練データだけを使う
# - 予測にはテストデータを使う

# TODO 4: モデルの結果を確認する
# - 正解率を計算する
# - 混同行列を作る
# - 正解と予測を print() で見比べる

# TODO 5: テストデータをグラフで確認する
# - 正解ラベルと予測ラベルの違いが分かるように工夫する
# - タイトル、軸ラベル、凡例をつける
