 
#program: dft.py
#author: Maulik Rajpara
#course: CS 827
#date: 2018/10/29 
#assignment #2
#description: 
#--------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100
N = 1024
data = pd.read_csv('my.dat',header=None, delimiter=r"\s+") #read input file from given location

data_list = data[1]


new_data_list = []
#coverting all values into float
for i in range(0,N):

   new_data_list.append(float(data_list.iloc[i]))

pi2 = np.pi * 2.0

#----------------------------------------------------------------
# DFT
# purpose: calculates fourier tranformation 
# parameter(s): <1> list (frequency list)
# return: The output of the DFT is a sequence of complex numbers. 
#         Each complex number is a pair consisting of a real-part and an imaginary-part.
def DFT(freq_list):
    N = len(freq_list)
    temp_list = []
    for k in range(N):
        exp_value = 0.0
        for n in range(N):
            exp_value += freq_list[n] * np.exp(- 1j * pi2 * k * n / N)
        temp_list.append(exp_value / N)
    return temp_list


X = DFT(new_data_list) # calling dft function 
X=X[:64]  #reducing size of list to show graph more accurate 
powers_all = np.abs(np.divide(X, N//2))
powers = powers_all[0:N//2]
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N/2)), N)
frequencies=frequencies[:64]
powers=powers[:64]



# creating output file which contains frequencies and powers
f = open("result.text", "w")
f.write( " Frequencies = " + str(frequencies) +"\n")
f.write( " Power = " + str(powers)+"\n")
f.close()



p=data[0] # input file data for ploting graph
q=data[1] # input file data  for ploting graph
_, plots = plt.subplots(2)
plots[0].plot(p[:512],q[:512])  # ploting graph of input data
plt.ylabel('Power')
plt.xlabel('Frequency')
plots[1].plot(frequencies,powers)  #ploting plot spectrum grpah
plt.show()


