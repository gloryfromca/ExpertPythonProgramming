from test import pystone
benchtime, pystones = pystone.pystones()
print("%.1f" % (pystones/1000), "k stones per second")
