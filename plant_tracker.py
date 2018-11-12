# set pin defaults
pin_a = FALSE
pin_b = FALSE
pin_c = FALSE

# loop through the range of available inputs
for num in range(0,8):
    bin = '{0:0b3}'.format(num)
    pin_a = int(bin[0])
    pin_b = int(bin[1])
    pin_c = int(bin[2])

    print "input {}: {} {} {}".format(num, pin_a, pin_b, pin_c)