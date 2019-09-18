import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

def findintersectionpts(m,bint):
	a = 4+m**2
	b = 2*m*bint
	c = bint**2 - 100
	x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
	y1 = m*x1+bint
	y2 = m*x2+bint
	return [[x1,y1],[x2,y2]]


# el = Ellipse(xy=[0,0], width=10, height=20)
# fig = plt.figure()
# ax = fig.add_subplot(111,aspect='equal')
# ax.add_artist(el)
# ax.set_xlim(-10,10)
# ax.set_ylim(-15,15)

# xrange = np.linspace(0,1.4,10)
m = (-9.6 - 10.1)/(1.4 - 0)
bint = 10.1
# intpt = findintersectionpts(m,bint)
newx = 1.4
newy = -9.6
# if abs(newx-intpt[0][0]) > abs(newx-intpt[1][0]):
	# newx = intpt[0][0]
	# newy = intpt[0][1]
# else:
	# newx = intpt[1][0]
	# newy = intpt[1][1]
# tm = -4.*newx / newy
# normalm = -1./tm
# theta=(m-normalm)/(1+m*normalm)
# phi = np.arctan(theta)
# m = (normalm-np.tan(phi))/(1+np.tan(phi)*normalm)
# bint = newy-m*newx
# m2 = -4.*intpt[0][0] / intpt[0][1]
# normalm = -1/m2


# # theta = np.arctan(abs((m1-m2)/(1+m1*m2)))

# t=(m1-normalm)/(1+m1*normalm)
# phi = np.arctan(t)
# m3 = (normalm-np.tan(phi))/(1+np.tan(phi)*normalm)
# xrange3 = np.linspace(-3.9905976,1.4,10)

# y3 = m3*xrange3 + (-9.6-m3*1.4)
# xrange2 = np.linspace(-5,5,10)
# y1 = xrange*m1 +b1
# y2 = xrange2*normalm + (-9.6-normalm*1.4)

# intpt2 = findintersectionpts(m3,(-9.6-m3*1.4))

# newtm = -4.*intpt2[1][0] / intpt2[1][1]
# xrange4 = np.linspace(-6,0,10)
# y4 = xrange4*newtm + intpt2[1][1]-newtm*intpt2[1][0]
# newnormalm = -1/newtm
# y5 = xrange2*newnormalm + intpt2[1][1]-newnormalm*intpt2[1][0]

# t2=(m3-newnormalm)/(1+m3*newnormalm)
# phi2 = np.arctan(t2)
# m4 = (newnormalm-np.tan(phi2))/(1+np.tan(phi2)*newnormalm)
# y6 = m4*xrange2 + intpt2[1][1]-m4*intpt2[1][0]

# intpt3 = findintersectionpts(m4,intpt2[1][1]-m4*intpt2[1][0])
# # newx = max(abs(intpt2[1][0]-intpt3[0][0]),abs(intpt2[1][0]-intpt3[1][0]))
# if abs(intpt2[1][0]-intpt3[0][0]) > abs(intpt2[1][0]-intpt3[1][0]):
	# newx = intpt3[0][0]
	# newy = intpt3[0][1]
# else:
	# newx = intpt3[1][0]
	# newy = intpt3[1][1]
# # newy = max(abs(intpt2[1][1]-intpt3[0][1]),abs(intpt2[1][1]-intpt3[1][1]))
# newt2m = -4.*newx / newy
# newnormalm2 = -1./newt2m
# t3=(m4-newnormalm2)/(1+m4*newnormalm2)
# phi3 = np.arctan(t3)
# m5 = (newnormalm2-np.tan(phi3))/(1+np.tan(phi3)*newnormalm2)
# y7 = xrange2*m5 + newy-m5*newx

# plt.plot(xrange,y1,'r')
# plt.plot(xrange2,y2,'r--')
# plt.plot(xrange3,y3,'r')
# plt.plot(xrange4,y4,'g')
# plt.plot(xrange2,y5,'r--')
# plt.plot(xrange2,y6,'r')
# plt.plot(xrange2,y7,'r')
# plt.show()
count = 0
while True:
	if newx >-0.01 and newx <0.01 and newy>0.:
		break
	
	
	
	tm = -4.*newx / newy
	normalm = -1./tm
	theta=(m-normalm)/(1+m*normalm)
	phi = np.arctan(theta)
	m = (normalm-np.tan(phi))/(1+np.tan(phi)*normalm)
	bint = newy-m*newx
	intpt = findintersectionpts(m,bint)
	if abs(newx-intpt[0][0]) > abs(newx-intpt[1][0]):
		newx = intpt[0][0]
		newy = intpt[0][1]
	else:
		newx = intpt[1][0]
		newy = intpt[1][1]
	count+=1