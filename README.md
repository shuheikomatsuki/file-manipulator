# File Manipulator

ファイルへの操作をCLI上で実行できます。

## コマンド操作

```bash
python3 file_manipulator.py <command name> arg1 ... argn
```

### reverse

指定したファイルの内容を逆にしたファイルを生成する

```bash
python3 file_manipulator.py reverse <inputpath> <outputpath>
```

### copy

指定したファイルの内容を別ファイルにコピーする

```bash
python3 file_manipulator.py copy <inputpath> <outputpath>
```

### duplicate-contents

指定したファイルの内容を、任意の回数だけ複製する

```bash
python3 file_manipulator.py duplicate-contents <inputpath> <Repetition Count>
```

### replace-string

指定したファイル内にある"needle""という文字列を"newstring"に置き換える

```bash
python3 file_manipulator.py replace-string <inputpath> needle newstring
```

---

# File Converter

markdown形式のファイルをHTMLファイルに変換する。

```bash
python3 file-converter.py markdown <md_inputpath> <html_outputpath>
```
実行例
```bash
python3 file-converter.py markdown README.md index.html
```

---

# Guess the number game

ランダムに生成される数値を当てる非常に簡単なゲームです。

## 遊び方
1. 任意の整数n, mを入力し実行する。ただし、n < m とする。
2. n 以上 m 以下の整数を入力する。
3. 正解の場合は"Collect!"と表示される。不正解なら"Wrong"と表示され、再入力する。これを正解するまで繰り返す。

```bash
python3 guess_number.py <n> <m>
```
実行例
```bash
python3 guess_number.py 3 8
```