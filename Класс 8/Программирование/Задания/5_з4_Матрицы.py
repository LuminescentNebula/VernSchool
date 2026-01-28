import matplotlib.pyplot as plt
import matplotlib
#Не трогать код выше 

#Палитра цветов
pallete=["#000000","#FFFFFF"]

#Нужно написать программу, которая будет заполнять случайно двумерный массив arr. 

#Число обозначает номер цвета в палитре
arr=[[1,0,1,0,1],
     [1,0,1,0,1],
     [1,1,1,1,1],
     [1,0,0,0,1],
     [1,0,0,0,1]]

#Не трогать код ниже
plt.imshow(arr, cmap=matplotlib.colors.ListedColormap(pallete));
plt.show()