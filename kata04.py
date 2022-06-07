t = ( 0, 4, 132.42222, 10000, 12345.67)

join = str(t[0]) + str(t[1])
var = '{:.2e}'.format(t[3])
var2 = '{:.2e}'.format(t[4])

print ("module_00, ex_%s : %.2f, %s, %s" % (join , t[2],var,var2))
