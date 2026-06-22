import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

from sklearn.tree import DecisionTreeClassifier

# =========================================
# task01: CSVを読んで、合格/不合格を予測しよう
# =========================================

# TODO 1: データを読み、分類に使う列を選ぶ
# - students_pass.csv を読み込む
# - 勉強時間と出席率を特徴量にする
# - 合格/不合格の列を正解ラベルにする

# TODO 2: Decision Tree のモデルを作り、学習させる
# - 授業資料の DecisionTreeClassifier を使う
# - fit() で学習する

# TODO 3: new_students.csv の学生を予測する
# - 学習で使った特徴量と同じ列を使う
# - 予測結果を print() で確認する

# TODO 4: 結果をグラフで見る
# - 学習データを合格/不合格で色分けする
# - 新しい学生も同じグラフに表示する
# - タイトル、軸ラベル、凡例をつける
