# 46. 猜數字遊戲
# 產生一個隨機整數 1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random  #亂數

r = random.randint(1, 100)  # 產生亂數
ans = int(input('猜猜數字是多少: '))
while True:
    if ans > r:
        print('比答案大')
        ans = int(input('猜猜數字是多少: '))
    elif ans < r:
        print('比答案小')
        ans = int(input('猜猜數字是多少: '))
    else:
        print('終於猜對了')
        break
