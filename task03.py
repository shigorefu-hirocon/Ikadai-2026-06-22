import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# =========================================
# task03: Logistic Regression で確率を見よう
# =========================================

# TODO 1: データを準備する
# - students_pass.csv を読み込む
# - 勉強時間、出席率、宿題提出率を特徴量にする
# - 合格/不合格を正解ラベルにする
# - 訓練データとテストデータに分ける

# TODO 2: Logistic Regression で分類する
# - LogisticRegression を使って学習する
# - テストデータを予測する

# TODO 3: 予測の「確率」を確認する
# - predict_proba() を使う
# - 合格する確率だけを取り出してみる
# - 予測クラスと確率を print() で表示する

# TODO 4: 確率をグラフで見る
# - テストデータごとの合格確率を棒グラフにする
# - タイトル、軸ラベルをつける
