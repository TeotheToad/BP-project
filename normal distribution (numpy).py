import numpy as np
# استفاده از کتابخانه numpy
import math
# استفاده از کتابخانه math

# دریافت تعداد نمونه‌ها از کاربر
n = int(input())

# تعریف تابع توزیع نرمال
def normal_distribution_function(x):
    # فرمول توزیع نرمال
    y = ((2 * math.pi)**(-1/2)) * (math.e**((-1/2) * (x**2)))
    return y

# تعریف تابع برای محاسبه میانگین، انحراف معیار و نمونه‌های توزیع نرمال
def normal(n):
    y = []
    i = n
    while i > 0:
        # تولید یک عدد تصادفی در بازه [0, 1) با استفاده از numpy
        x = np.random.rand()
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
