# Coursera Neural Networks Course
# Week 11 Quiz Problem 5: 
# Figure out lowest possible energy and configuration for the lowest energy of a given Boltzman Machine
# (lazy man approach..)
import itertools
nodes=5;
#w_e=[1,1,-3,3,-2];
#w_i = [2,2];
ens = []
configs=[]

for s in list(itertools.product([0, 1], repeat=nodes)): # 0-a, 1-b, .., 4-e
	en = s[0]*s[2]*(1.0) + s[1]*s[2]*(1.0)+s[1]*s[4]*(-3.0) + s[3]*s[4]*3.0+s[0]*s[3]*(-2.0) + s[4]*s[2]*(2.0)+ s[2]*s[3]*(2.0);
	ens.append(-en);
	configs.append(s);