import math
def N(k,r):
	return (1+math.sqrt(1+12*(6*k**2+3*r**2+6*k*r-2*k-r)))/6

def M(k,r):
	return (1+math.sqrt(1+12*(3*r**2+6*k*r-r)))/6

k=1
while k<10000:
	r=1
	while r<10000:
		n=N(k,r)
		m=M(k,r)
		if (abs(round(n)-n)<10**(-12) and abs(round(m)-m)<10**(-12)):
			print(k,r,n,m)
		r=r+1
	k=k+1
	if (round(k/10)==k/10):
		print(k/10)

#solution
# 1020 1147 2395.0 1912.0
#N(1020,1147) = 2395.0
#M(1020,1147) = 1912.0
#m = 1912
#m*(3*m-1)/2= 5482660.0

