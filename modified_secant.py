#!/usr/bin/env python3

#modified secant
def modified_secant(f,x0,delta,n):
	i=0
	d=delta
	for i in range(n+1):
		x=x0-d*x0*f(x0)/(f(x0+d*x0)-f(x0))
		ea=(x-x0)/x*100
		print("step\tX[i+1]\tX[i]\tea")
		print("{}\t{:.5}\t{:.5}\t{:.5}".format(i, x,x0,ea))
		i+=1
		x0=x
		
f=lambda x:x**3-6*x**2+11*x-6.1
modified_secant(f, 3.5, 0.01, 3)