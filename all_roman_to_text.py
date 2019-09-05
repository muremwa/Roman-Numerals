from int_roman import IntRoman


with open('roman_integers.txt', 'w') as f:
    line = "{number} - {roman}\n"
    # new instance of IntRoman
    ir = IntRoman()

    # loop
    for i in range(1, 4000):
        f.write(line.format(number=i, roman=ir.to_roman(i)))
