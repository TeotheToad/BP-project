import numpy as np
# استفاده از کتابخانه numpy

def money_game(rounds):
    # مقدار اولیه پول هر بازیکن
    player_amount_of_money = 20 * [25]

    i = 0
    while i <= rounds:
        j = 0
        while j < len(player_amount_of_money):
            # انتخاب بازیکن به صورت رندوم با استفاده از توزیع یکنواخت
            player = int(np.random.uniform(0, len(player_amount_of_money) - 1))

            # انجام بازی و به‌روزرسانی مقدار پول بازیکنان
            if player < j:
                player_amount_of_money[j] -= 1
                player_amount_of_money[player] += 1
            else:
                player_amount_of_money[j] -= 1
                player_amount_of_money[player + 1] += 1
            j = j + 1

        # حذف بازیکنانی که پولشان تمام شده است
        while 0 in player_amount_of_money:
            player_amount_of_money.remove(0)

        i = i + 1

    return player_amount_of_money

# تعداد دورهای بازی
rounds = 10000

# اجرای بازی و چاپ نتیجه
final_amount_of_money = money_game(rounds)
print("مقدار نهایی پول بازیکنان:", final_amount_of_money)
