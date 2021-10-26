#!/usr/bin/env python3

#bisection

def bisection(f,xl,xu,es):
	xr_old=xu
	xr=(xl+xu)/2
	ea=1
	i=0
	while ea >= es or ea <= es:
		if f(xr)*f(xu)>0:
			xu=xr
		elif f(xr)*f(xu)<0:
			xl=xr
		else:
			print("Root is {} and the error is {}".format(xr,ea))
			break
		ea=(xr-xr_old)/xr
		xr_old=xr
		xr=(xl+xu)/2
		i+=1
		print("step\txl\txu\txr\tea")
		print("{} {} {} {} {}\n".format(i,xl, xu,xr,ea))
		
f=lambda x:-12-21*x+18*x**2-2.75*x**3
bisection(f, -1, 0, 0.1)

