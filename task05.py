import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task05: max_depth を変えて過学習を確認しよう
# =========================================

# TODO 1: 健康診断データを準備する
# - health_check.csv を読み込む
# - 年齢、BMI、血圧、血糖値、運動日数を特徴量にする
# - risk を正解ラベルにする
# - 訓練データとテストデータに分ける

# TODO 2: max_depth を変えて何度か学習する
# - 深さ 1, 2, 3, 制限なしを試す
# - それぞれのモデルで訓練データとテストデータの正解率を出す

# TODO 3: 過学習していないか確認する
# - 訓練データだけ高く、テストデータが低い場合は過学習の可能性がある
# - 結果を print() で表示する

# TODO 4: 正解率の変化をグラフにする
# - 深さごとの訓練スコアとテストスコアを折れ線グラフで表示する
# - タイトル、軸ラベル、凡例をつける
