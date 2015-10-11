import pymouse
import time

m = pymouse.PyMouse()
print m.position()
x = min(m.screen_size())

i = 0
j = 1
k = i + j

while i < x and j < x:
	m.click(i, j)
	time.sleep(0.5)
	i = j
	j = k
	k = i + j


