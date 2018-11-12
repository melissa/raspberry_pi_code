# loop through the range of available inputs
for num in range(0,8):
    bin_num = '{0:03b}'.format(num)
    pin_a = int(bin_num[0])
    pin_b = int(bin_num[1])
    pin_c = int(bin_num[2])

    # print sensor number as well as selectors a, b, and c
    # this is to ensure we're getting input from the sensor we expect to receive
    # input from.
    print "input from sensor #{} ({} {} {}):".format(num, pin_a, pin_b, pin_c)