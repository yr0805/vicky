import wave as we
import numpy as np
import matplotlib.pyplot as plt
import os
import math

def calVolumeDB(datawave, frameSize, overLap):
    wlen = len(datawave)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = datawave[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.mean(curFrame) # zero-justified
        volume[i] = 10*np.log10(np.sum(curFrame*curFrame))
    return volume


filepath = "C:/Users/top/Music/" #�s���ɪ����|
filename= os.listdir(filepath) #��Ƨ��U���Ҧ��ɮ� 
num=0
for file in range(len(filename)):
    print(num+1, end=" ")
    num+=1
    print(filename[file])
name = input('�п�J�ɦW�G')
wavefile=we.open(filepath+filename[int(name)-1],"rb")

#Ū���o��wave����T
params=wavefile.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)

#��G�i�� 
datawav=wavefile.readframes(nframes)
wavefile.close()

#�r����}�C
datause=np.frombuffer(datawav,dtype=np.int16)

print("datause����",end="")
print(len(datause))
print(datause)

frameSize = 256
overLap = 128
volume12 =calVolumeDB(datause,frameSize,overLap)

datause.shape=-1,2
datause=datause.T
time=np.arange(0,nframes)*(1/framerate)
##�e��
plt.title(filename[int(name)-1])
#plt.subplot(211)
plt.plot(time,volume12,'r--')
# plt.subplot(212)
# plt.plot(time, datause[1])
plt.show()