import random

# 1. 生成一个 1-100 的秘密数字
secret = random.randint(1, 100)

print("我想了一个 1 到 100 之间的数字，你猜猜看？")

# 2. 循环猜，直到猜对
while True:
    guess = int(input("请输入你猜的数字: "))
    if guess < secret:
        print("太小了，再大一点！")
    elif guess > secret:
        print("太大了，再小一点！")
    else:
        print(f"🎉 答对了！秘密数字就是 {secret}")
        break