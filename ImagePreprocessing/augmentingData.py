import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","del","nothing","space"]
#letters = ["A"]
# Parameters here are chosen to ensure images still retain its fundamental integrity
# tolerences for shear and zoom does not affect the ability to comprehend the image.
# augmenting is done to ensure various orientations and lighting conditions are
#represented in the training dataset
datapath=input('Enter training set data path: ')
batchSize=input('Enter batch size for random img generation: ')
#sampleSize=input('Number of images to sample: ')
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.07,
        brightness_range=[0.2,2.5],
        height_shift_range=0.07,
        shear_range=0.1,
        zoom_range=0.2,
        fill_mode='nearest')

for letter in letters:
    path=os.path.join(datapath,letter)
    i=0
    #j=0
    for images in os.listdir(path):
        #j=j+1
        #if j > int(sampleSize):
            #break
        x=str('/')
        filepath=path+x+images
        img = load_img(filepath)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the path specified above and it concatinates the
        # letter value to the path. Prefix new is added for ease of filtering incase
        # futher tuning is required
        i = 0
        for batch in datagen.flow(x, batch_size=int(batchSize), save_to_dir=path, save_prefix='new', save_format='jpg'):
            i += 1
            if i >= 10:
                break
