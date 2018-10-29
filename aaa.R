m=0.5
c=-log(0.01)*m
height=c(2.13,1.59,1.31)
#c(0.9,0.7,0.53,0.4)
p1=c()
a=0
for(i in height){
  a=a+1
  u=m*log(i) + c
  p1[a]=u
}

p2 = p1 + rnorm(3,mean=0, sd=0.07)

dat=data.frame(
  z=log(height),
  u=p2
)
rip=lm(u ~ z, data = dat)
int=as.numeric(rip$coefficients[1])
grad=as.numeric(rip$coefficients[2])
print(p2)
print(grad)
print(int)
plot(log(height),p2)
lines(c(-1,5), c((-grad*1 + int), (grad*5 + int)), type="l")

print(exp(-int/grad))
#plot(height,p2, type='l')


####temp######

m1=-0.7
c1=15.9
height=c(2.13,1.59,1.31)
#c(2.22,1.52,1,0.78)
t1=c()
a=0
for(i in height){
  a=a+1
  Tmp=m1*i + c1
  t1[a]=Tmp
}
t2=t1 + rnorm(3,mean=0, sd=0.04)
t2=t2+273.15
temperature=data.frame(
  t = t2,
  z = height
)
rip3=lm(t ~ z, data=temperature)
gradt=as.numeric(rip3$coefficients[2])
intt=as.numeric(rip3$coefficients[1])
plot(height,t2)
lines(c(0,4), c(intt, (gradt*4 + intt)), type='l')
print(gradt)
print(t2)

dat2=data.frame(
  z=height,
  u=p2
)
rip2= lm(u ~ z, data=dat2)
du = as.numeric(rip2$coefficients[2])
dT=-0.8
Temp=273.15+15
Ri = (9.81/Temp)*(gradt)*(1/(du**2))
print(Ri)
