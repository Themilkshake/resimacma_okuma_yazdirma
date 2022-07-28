#opencv'yi ve numpy kütüphanesini import ettim.
import cv2
import numpy as np

#resmi arraya dönüştürür (0 --> RGB'yi kaldırır, tek kanallı yapar).
resim = cv2.imread("kus.jpg",0)

#resmi gösterir.
cv2.imshow("KUŞ",resim)

#yeni resmi kaydeder.
cv2.imwrite("yeniresim.png", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()