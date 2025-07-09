import random

def check_hit_and_blow(secret, guess):
    """ユーザーの推測値と正解を比較、ヒットとブローの数値を返す"""

    # ヒットとブロー変数初期化
    hit = 0
    blow = 0

    # ヒットのカウント（ヒット　　= 数値と位置が一致）
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            hit += 1

    # 重複数のカウント
    hit_and_blow = 0
    for num in secret:
        if num in guess:
            hit_and_blow += 1

    # ブロー = 重複数からヒット数を引く
    blow = hit_and_blow - hit

    return hit, blow

# ゲーム開始の説明
print('数を当てようゲーム!')
print('1~9までの数値を使用しランダムな数値を作成します。')
print('あなたは1ケタから9ケタのケタ数を指定してください。')

# ケタ数入力
while True:
    n = int(input('何ケタの数字にしますか？(1~9):'))

    # 1~9の入力がされた際、ループから抜ける
    if 1 <= n <= 9:
        break
    print('1~9の数字を入れてください。')

# 正解の数値
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
secret_numbers = random.sample(numbers, n)

# 試行回数を初期化
trial_count = 0

# ユーザーから推測した数字を受け取り正解するまでループ
while True:
    guess_number = input(f'{n}ケタの数字を入れてください: ')

    # 入力を整数リストに変換
    guess_list = []
    for char in guess_number:
        guess_list.append(int(char))
    print(guess_list)

    # 試行回数をカウントアップ
    trial_count += 1
    print(f'{trial_count}回目の回答です。')

    # ユーザーの推測値と正解を比較、ヒットとブローの数値を返す
    hit, blow = check_hit_and_blow(secret_numbers, guess_list)
    
    # 結果表示
    if hit == n:
        print(f'正解!GameClear!正解={secret_numbers}')
        print(f'{trial_count}回で正解でした。')
        break
    else:
        print(f'ヒット = {hit}, ブロー = {blow}')