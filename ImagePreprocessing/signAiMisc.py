def getImgCount(path,imgType):
    #arguments of directory path and image type (jpg png etc)
    import pathlib
    import IPython.display as display
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt

    path=r'{}'.format(path) #convert to raw string
    data_dir=pathlib.Path(path)
    image_count = len(list(data_dir.glob('*/*.{}'.format(imgType))))
    return image_count

def printImgCount(arg,type):
    print(getImgCount(arg,type))
