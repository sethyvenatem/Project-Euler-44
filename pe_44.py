import math
#This provides acces to sqrt

def N(k,r):
	return (1+math.sqrt(1+12*(6*k**2+3*r**2+6*k*r-2*k-r)))/6
def M(k,r):
	return (1+math.sqrt(1+12*(3*r**2+6*k*r-r)))/6
#These two functions compute n amd m for k and r given

k=1
while k<10000:
#The loop stops either when k=100000 or when a solution is found.
	r=1
	while r<10000:
		#The loop stops either when r=10000 or when a solution is found.
		n=N(k,r)
		m=M(k,r)
		#This makes it a bit faster since n amd m are both needed 3 times below.
		if (abs(round(n)-n)<10**(-12) and abs(round(m)-m)<10**(-12)):
			#print(k,r,n,m)
			k=10000
			break
			#If a solution is found, break set k=10000 (stops the outer loop) and break out of the inner loop.
		r=r+1
	k=k+1
	if (round(k/10)==k/10):
		print(k/10)
		#This displays the progress of the code. It helps to know that the computer is working as intended. Only 1 in 10 outer loops are signalled.

print("The pair of pentagonal numbers associated to k+r and k are ",round(n*(3*n-1)/2)," and ",round(m*(3*m-1)/2))
print("The solution is ",round(m*(3*m-1)/2))

#solution
# 1020 1147 2395.0 1912.0
#N(1020,1147) = 2395.0
#M(1020,1147) = 1912.0
#m = 1912
#m*(3*m-1)/2= 5482660.0
