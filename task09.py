import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# =========================================
# task09: 訓練CSVで学習し、テストCSVで評価しよう
# =========================================

# TODO 1: 学習用CSVとテスト用CSVを読み込む
# - exam_train.csv はモデルを学習するために使う
# - exam_test.csv は最後の確認だけに使う
# - 両方で同じ特徴量を使う

# TODO 2: 2種類の分類モデルを作る
# - DecisionTreeClassifier を学習する
# - LogisticRegression も学習する
# - どちらも学習用CSVだけで fit() する

# TODO 3: テスト用CSVで2つのモデルを比べる
# - それぞれのモデルで予測する
# - それぞれの正解率を計算する
# - Decision Tree の混同行列も確認する

# TODO 4: 予測結果をCSVに保存する
# - テスト用データに2つのモデルの予測結果を追加する
# - task09_predictions.csv として保存する

# TODO 5: 比較結果をグラフで表示する
# - 2つのモデルの正解率を棒グラフにする
# - 正解率と混同行列も print() で表示する
