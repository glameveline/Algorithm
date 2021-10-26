#!/usr/bin/env python3

# false position
def false_position(f,xl,xu,es):
	xr_old=0
	ea=100
	xr=xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
	step=0
	while abs(ea)>es:
		xr=xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
		if f(xr)*f(xu)>0:
			xu=xr
		elif f(xr)*f(xu)<0:
			xl=xr
		elif abs(ea)<=es:
			active=False
		else:
			print("Root is {} and the error is {}".format(xr,ea))
			break
		ea=(xr-xr_old)/xr*100
		xr_old=xr
		step+=1
		print("step\txl\txu\txr\tea")
		print("{} {} {} {} {}\n".format(step,xl, xu,xr,ea))
		
		
f=lambda x:-12-21*x+18*x**2-2.75*x**3
false_position(f, -1, 0, 1)
