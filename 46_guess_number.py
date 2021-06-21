# 46. 猜數字遊戲 & 47
# 產生一個隨機整數 1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小
# 延伸 : 印出猜幾次
# 延伸 : 讓使用者決定隨機數範圍

import random  #亂數

# 產生亂數結束值小於開始值會有 ValueError: empty range for randrange()
while True:
    int_start = int(input('請決定隨機數字範圍開始值: '))
    int_end = int(input('請決定隨機數字範圍結束值: '))
    if int_end < int_start:
        print('結束值不可小於開始值, 請重新輸入')
    else:
        break

#r = random.randint(1, 100)  # 產生亂數
r = random.randint(int_start, int_end)  # 產生亂數
int_count = 0
while True:
    ans = int(input('猜猜數字是多少: '))
    int_count += 1  # count = count +1
    if ans > r:
        print('比答案大')
    elif ans < r:
        print('比答案小')
    else:
        print('終於猜對了')
        break
    print('這是猜第 ', int_count, ' 次')