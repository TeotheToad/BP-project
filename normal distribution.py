import math
# استفاده از کتابخانه math

# دریافت تعداد نمونه‌ها از کاربر
n = int(input())

# تعریف ژنراتور (LCG)
class LCG:
    def __init__(self, seed, x=16467, y=201467, z=2**10):
        self.x = x
        self.y = y
        self.z = z
        self.state = seed

    def random_number(self):
        self.state = (self.x * self.state + self.y) % self.z
        return self.state / float(self.z)

# محاسبه مقدار توزیع نرمال برای یک مقدار x
def normal_distribution_function(x):
    y = ((2 * math.pi)**(-1/2)) * (math.e**((-1/2) * (x**2)))
    return y

# تعریف تابع برای محاسبه میانگین، انحراف معیار و نمونه‌های توزیع نرمال
def normal(n):
    y = []
    i = n
    while i > 0:
        value = abs(hash(str(i)))
        random_number = LCG(seed=value)
        x = random_number.random_number()
        y.append(normal_distribution_function(x))
        i = i - 1

    # محاسبه میانگین
    sum = 0
    j = 0
    while j < len(y):
        sum += y[j]
        j = j + 1
    mean = sum / n

    # محاسبه انحراف معیار
    s = 0
    k = 0
    while k < len(y):
        s = s + ((((y[k] - mean)**2) / n)**(1/2))
        k = k + 1

    return mean, s, y

# چاپ میانگین، انحراف معیار و نمونه‌های توزیع نرمال
print(normal(n))
