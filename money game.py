class LCG:
    def __init__(self, seed, x=16467, y=201467, z=2**10):
        # مقداردهی اولیه به مولفه‌ها
        self.x = x  # ضرب‌کننده
        self.y = y  # افزایش‌دهنده
        self.z = z  # ماژولوس
        self.state = seed  # مقدار اولیه

    def random_number(self):
        # تولید یک عدد رندوم با استفاده از فرمول
        self.state = ((self.y + self.x * self.state) % self.z)
        return (self.state / int(self.z))

def money_game(rounds):
    # مقدار اولیه پول هر بازیکن
    player_amount_of_money = 20 * [25]

    i = 0
    while i <= rounds:
        j = 0
        while j < len(player_amount_of_money):
            # تولید یک مقدار رندوم برای انتخاب بازیکن
            value = abs(hash(str(i + 1000)))
            lcg = LCG(seed=value)
            player = int(lcg.random_number() * (len(player_amount_of_money) - 1))

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















