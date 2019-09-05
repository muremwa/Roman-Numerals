from int_roman import IntRoman
from time import time

# see how fast it can produce these roman numerals
digits = [i for i in range(1, 4000)] * 1000
print(len(digits))
ir = IntRoman()

start = time()

# loop over all
for num in digits:
    ir.to_roman(num)

end = time()

print('time used is {}'.format(end-start))

with open('roman_time.txt', 'a') as f:
    print('time used is {}'.format(end-start), file=f)
