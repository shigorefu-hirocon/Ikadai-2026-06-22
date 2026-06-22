# 分類 課題

Classification（分類）の練習問題です。
`task01.py` から `task09.py` まで、Pandas で CSV/JSON を読み込み、matplotlib で結果を見ながら分類モデルを作ります。

各データファイルには 50 件のデータがあります。
列名・JSON のキー名は日本語です。
また、分類に直接使わない余分な列も入っています。
学生はすべての列をそのまま使うのではなく、目的に合う特徴量だけを選んでモデルを作ってください。

## インストール

```bash
pip install -r requirements.txt
```

## 課題

1. `task01.py`: CSVを読み、合格/不合格を学習して新しい学生を予測する
2. `task02.py`: `train_test_split` で訓練データとテストデータに分け、正解率を出す
3. `task03.py`: Logistic Regression で合格確率を確認する
4. `task04.py`: JSONのメール特徴量から迷惑メールを分類する
5. `task05.py`: 健康診断データで `max_depth` を変えて過学習を確認する
6. `task06.py`: 問い合わせを3つのカテゴリに分類する
7. `task07.py`: アプリ利用データで決定木の特徴量重要度をグラフにする
8. `task08.py`: 汚いCSVを整理してから分類し、予測結果CSVを保存する
9. `task09.py`: 訓練CSVで学習し、テストCSVで評価して予測結果CSVを保存する