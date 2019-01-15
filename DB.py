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


filepath = "C:/Users/top/Music/" #存放音檔的路徑
filename= os.listdir(filepath) #資料夾下的所有檔案 
num=0
for file in range(len(filename)):
    print(num+1, end=" ")
    num+=1
    print(filename[file])
name = input('請輸入檔名：')
wavefile=we.open(filepath+filename[int(name)-1],"rb")

#讀取這首wave的資訊
params=wavefile.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)

#轉二進位 
datawav=wavefile.readframes(nframes)
wavefile.close()

#字串轉陣列
datause=np.frombuffer(datawav,dtype=np.int16)

print("datause長度",end="")
print(len(datause))
print(datause)

frameSize = 256
overLap = 128
volume12 =calVolumeDB(datause,frameSize,overLap)

datause.shape=-1,2
datause=datause.T
time=np.arange(0,nframes)*(1/framerate)
##畫圖
plt.title(filename[int(name)-1])
#plt.subplot(211)
plt.plot(time,volume12,'r--')
# plt.subplot(212)
# plt.plot(time, datause[1])
plt.show()