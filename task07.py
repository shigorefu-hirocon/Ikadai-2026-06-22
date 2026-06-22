import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task07: 特徴量重要度を見よう
# =========================================

# TODO 1: アプリ利用データを準備する
# - app_users.csv を読み込む
# - ログイン日数、学習時間、完了レッスン数、質問数を特徴量にする
# - 継続したかどうかを正解ラベルにする

# TODO 2: Decision Tree を学習する
# - 訓練データとテストデータに分ける
# - 木の深さを制限して学習する
# - テストデータも予測してみる

# TODO 3: どの特徴量が大事だったかを見る
# - 学習したモデルから feature_importances_ を取り出す
# - 特徴量名と重要度を print() で表示する

# TODO 4: 特徴量重要度をグラフにする
# - 棒グラフで表示する
# - タイトル、軸ラベルをつける
