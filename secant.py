#!/usr/bin/env python3

# secant method
def secant(f,x00,x0,n):
	i=0
	x_old=0
	for i in range(n+1):
		x_new=x0-(f(x0)*(x00-x0))/(f(x00)-f(x0))
		ea=(x_new-x_old)/x_new*100
		print("step\tX(i+1)\tX(i)\tX(i-1)\tea")
		print("{}\t{:.5}\t{:.5}\t{:.5}\t{:.5}".format(i, x_new,x0,x00,ea))
		i+=1
		x00=x0
		x0=x_new
		x_old=x_new
		
f=lambda x:x**3-6*x**2+11*x-6.1
secant(f, 2.5, 3.5, 3)