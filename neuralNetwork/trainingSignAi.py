import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

#use pip install if you are missing these libraries on your local machine
#matplot for displaying images and os for iterating the directories
#cv2 for imagine operations
#numpy for array operations

dataDir=r"C:\Users\rathn\github\signAi\signAiData\asl_alphabet_train\asl_alphabet_train"
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","del","nothing","space"]
# l=0
trainData=[]
def trainSetGenerator():
    for letter in letters:
        letterPath=os.path.join(dataDir,letter)#accessing each subfolder inside main asl_alphabet_train
        letterLabelNum=letters.index(letter)#assign array index as numerical category identifier
        for trainExample in os.listdir(letterPath):
            greyLetterArray=cv2.imread(os.path.join(letterPath,trainExample),cv2.IMREAD_GRAYSCALE)
            trainData.append([greyLetterArray,letterLabelNum])
            # plt.imshow(greyLetterArray,cmap="gray")#to ensure images are being selected from dir properly
            # plt.show()
            # l=l+1
            # if l>3:
            #     break
        #     break
        # break
    # print(greyLetterArray)
    # print(greyLetterArray.shape)
    # images were not rescaled since dataset was fixed at 200x200 including our augmented data
trainSetGenerator()
print(len(trainData))
