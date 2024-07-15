from matplotlib import image
from matplotlib import pyplot
import numpy
import os

#lenna
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

# 'murica 🔫🔫 🦅
USpath = os.path.dirname(os.path.abspath(__file__))
USfilename = USpath + '/' + 'murica.png'
USdata = image.imread(USfilename)

# # show picture
# pyplot.imshow(USdata)
# pyplot.show()

print(USdata.shape)
print(data.shape)

# modified_data = data.copy()

modfied_plot_data = numpy.ndarray([512,512]) #make an empty array 512 x 512 full of zeroes
for width in range(512):
    for length in range(512):
        if width >= 211 and length >= 400:
            pass
            # R = USdata[length-211,width-400,1]
            # print(USdata.shape)
            # print("usa")
            # G = USdata[length-211,width-400,1]
            # B = USdata[length-211,width-400,2]
            # modfied_plot_data[length][211+width] = int(0.3*R + 0.59*G + 0.11*B) #RGB
        else:
            pass
            # print("lenna")
            # R = data[width, length,1]
            # G = data[length,width,1]
            # B = data[length,width,1]
            # modfied_plot_data[length][width] = int(0.3*R + 0.59*G + 0.11*B) #RGB
# pyplot.imshow(data)
# pyplot.show()