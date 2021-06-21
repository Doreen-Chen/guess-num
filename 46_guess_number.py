# 46. 猜數字遊戲 & 47
# 產生一個隨機整數 1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小
# 延伸 : 印出猜幾次

import random  #亂數

r = random.randint(1, 100)  # 產生亂數
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