import cv2
import numpy as np

resiim = cv2.imread("pyt.png")

#Boyut(Size), Veri Tipi(dtype), Şekil(Shape) 
#resmin boyutunu verir.
print(resiim.size)
#resmin tipini verir.
print(resiim.dtype)
#remin yükseklik, genişlik, kanal sayısını verir.
print(resiim.shape)

#resmi ekranda gösterir.
cv2.imshow("resim", resiim)

cv2.waitKey(0)
cv2.destroyAllWindows()