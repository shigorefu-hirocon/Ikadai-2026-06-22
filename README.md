# 分類 課題

Classification（分類）の練習問題です。
`task01.py` から `task10.py` まで、Pandas で CSV/JSON を読み込み、matplotlib で結果を見ながら分類モデルを作ります。

## インストール

```bash
pip install -r requirements.txt
```

## 課題

1. `task01.py`: CSVを読み、合格/不合格を学習して新しい学生を予測する
2. `task02.py`: `train_test_split` で訓練データとテストデータに分け、正解率を出す
3. `task03.py`: Logistic Regression で合格確率を確認する
4. `task04.py`: JSONを読み、お客様が購入するか分類する
5. `task05.py`: JSONのメール特徴量から迷惑メールを分類する
6. `task06.py`: `max_depth` を変えて過学習を確認する
7. `task07.py`: 問い合わせを3つのカテゴリに分類する
8. `task08.py`: 決定木の特徴量重要度をグラフにする
9. `task09.py`: 汚いCSVを整理してから分類し、予測結果CSVを保存する
10. `task10.py`: 訓練CSVで学習し、テストCSVで評価して予測結果CSVを保存する

## データ

- `students_pass.csv`: 学生の勉強時間、出席率、宿題提出率、合格ラベル
- `new_students.csv`: 予測したい新しい学生
- `customer_purchase.json`: お客様の行動データ
- `emails.json`: メールの特徴量データ
- `health_check.csv`: 健康診断の数値データ
- `support_tickets.json`: 問い合わせカテゴリのデータ
- `app_users.csv`: アプリ利用者の継続/解約データ
- `students_dirty.csv`: 表記ゆれや欠損を含む学生データ
- `exam_train.csv`: 学習用の試験データ
- `exam_test.csv`: テスト用の試験データ

