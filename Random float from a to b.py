class LCG:
    def __init__(self, seed, x=16467, y=201467, z=2**10):
        # مقداردهی اولیه به مولفه‌ها
        self.x = x  # ضرب‌کننده
        self.y = y  # افزایش‌دهنده
        self.z = z  # ماژولوس
        self.state = seed  # مقدار اولیه

    def random_number(self):
        # تولید یک عدد تصادفی با استفاده از فرمول
        self.state = ((self.y + self.x * self.state) % self.z)
        return (self.state / int(self.z))  # نرمال‌سازی نتیجه به منظور قرار گرفتن در بازه 0 تا 1

def random_number_a_to_b(a:int, b:int):
    # تولید یک مقدار ابتدایی بر اساس جمع a و b
    value = abs(hash(str(a + b)))
    # ایجاد یک نمونه با استفاده از مقدار ابتدایی تولید شده
    lcg = LCG(seed=value)
    # تولید یک عدد رندوم در بازه [a، b)
    return (lcg.random_number() * (b - a) + a)  # تولید عدد رندوم در بازه (a تا b)
