import sys
import cv2
#import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread(sys.argv[1])

#kernel = np.ones((5,5),np.float32)/25

#blur = cv2.GaussianBlur(img,(3,3),0)
blur = cv2.bilateralFilter(img,9,75,75)
median = cv2.medianBlur(blur,3)

cv2.imwrite(sys.argv[2],median)
cv2.destroyAllWindows()

##plt.subplot(121),plt.imshow(img),plt.title('Original')
##plt.xticks([]), plt.yticks([])
##plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
##plt.xticks([]), plt.yticks([])
##
##plt.subplot(122),plt.imshow(median),plt.title('median')
##plt.xticks([]), plt.yticks([])
##plt.show()
