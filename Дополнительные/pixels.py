import matplotlib.pyplot as plt
import matplotlib

pallete=["#000000","#FFFFFF"]

arr=[[1,0,1,0,1],
     [1,0,1,0,1],
     [1,1,1,1,1],
     [1,0,0,0,1],
     [1,0,0,0,1]]

plt.imshow(arr, cmap=matplotlib.colors.ListedColormap(pallete));
plt.show()