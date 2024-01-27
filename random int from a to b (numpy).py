import numpy as np 
# استفاده از کتابخانه numpy

# دریافت دو عدد از کاربر به عنوان بازه تولید عدد رندوم
a, b = map(int, input().split())

# تولید یک عدد رندوم با توزیع یکنواخت در بازه [a، b)
random_number = int(np.random.uniform(a, b))

# چاپ عدد رندوم تولید شده
print("عدد تصادفی:", random_number)
