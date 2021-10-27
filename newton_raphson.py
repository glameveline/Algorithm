#!/usr/bin/env python3

def newton_raphson(f,f_diff,x0,n=10):
	x=x0
	i=0
	ea=1
	for i in range(n):
		x_new=x-f(x)/f_diff(x)
		i+=1
		ea=(x_new-x)/x_new*100
		x=x_new
		print("step\tXi\terror")
		print("{}\t{}\t{}".format(i, x_new,ea))
		
f=lambda x:x**3-6*x**2+11*x-6.1
f_diff=lambda x:3*x**2-12*x+11
newton_raphson(f, f_diff, 3.5, 3)
