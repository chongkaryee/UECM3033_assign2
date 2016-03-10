import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

#Read image and generate array
img=mpimg.imread('nana.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]

# Generate U, sigma,and Vh for red, green and blue matrix
Ur,Sr,Vhr = sp.svd(r,False,True,False,True)
Sr = np.diag(Sr)
	
Ug,Sg,Vhg = sp.svd(g,False,True,False,True)
Sg = np.diag(Sg)

Ub,Sb,Vhb = sp.svd(b,False,True,False,True)
Sb = np.diag(Sb)
	
print('There are number of '+ str(len(Sr)) +' nonzero elements in Sigma matrices.')

#lower Resolution Picture
Sr_new = np.zeros_like(Sr)
Sr_new[0:30] = Sr[0:30]
rnew = Ur@Sr_new@Vhr
	
Sg_new = np.zeros_like(Sg)
Sg_new[0:30] = Sg[0:30]
gnew = Ug.dot(Sg_new).dot(Vhg)
	
Sb_new = np.zeros_like(Sb)
Sb_new[0:30] = Sb[0:30]
bnew = Ub.dot(Sb_new).dot(Vhb)
	
img[:,:,0] = rnew
img[:,:,1] = gnew
img[:,:,2] = bnew
	

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(rnew, cmap = 'Reds')
ax3.imshow(gnew, cmap = 'Greens')
ax4.imshow(bnew, cmap = 'Blues')
	
plt.show()

#  Better Resolution Picture	
Sr_new = np.zeros_like(Sr)
Sr_new[0:200] = Sr[0:200]
rnew = Ur@Sr_new@Vhr
	
Sg_new = np.zeros_like(Sg)
Sg_new[0:200] = Sg[0:200]
gnew = Ug.dot(Sg_new).dot(Vhg)
	
Sb_new = np.zeros_like(Sb)
Sb_new[0:200] = Sb[0:200]
bnew = Ub.dot(Sb_new).dot(Vhb)

img[:,:,0] = rnew
img[:,:,1] = gnew
img[:,:,2] = bnew

fig = plt.figure(2)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(rnew, cmap = 'Reds')
ax3.imshow(gnew, cmap = 'Greens')
ax4.imshow(bnew, cmap = 'Blues')
	
plt.show()