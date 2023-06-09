def main(x):
    x = int(x)
    bits_16 = x >> 16
    bits_15_9 = (x >> 9) & 0b1111111
    bits_8_5 = (x >> 5) & 0b1111
    bits_4_0 = x & 0b11111
    new_num = (bits_16 << 16) | (bits_4_0 << 11) | (bits_15_9 << 4) | bits_8_5

    return new_num



print(main('106518'))
print(main('75711'))
print(main('40672'))
print(main('44044'))
