import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task08: 汚いCSVを整理してから分類しよう
# =========================================

# TODO 1: 汚いCSVを読み、使える形に直す
# - students_dirty.csv を読み込む
# - 「時間」や「%」などの文字を取り除いて数値に変換する
# - 合格/不合格、pass/fail などの表記を 1/0 にそろえる
# - 欠損値がある行をどうするか決める

# TODO 2: 整理したデータで分類モデルを作る
# - 勉強時間、出席率、宿題提出率を特徴量にする
# - 合格/不合格を正解ラベルにする
# - 訓練データとテストデータに分けて学習する

# TODO 3: テスト結果を確認して保存する
# - テストデータを予測する
# - 正解率を計算して表示する
# - テストデータ、正解、予測をまとめて task09_predictions.csv に保存する

# TODO 4: 整理後のデータをグラフで見る
# - 合格/不合格で色分けした散布図を作る
# - タイトル、軸ラベルをつける
