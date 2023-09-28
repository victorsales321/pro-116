import cv2

img = cv2.imread("solar-system.jpg")





cv2.putText(img,
            
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255))

cv2.putText(img,
            
            "Mercurio",
            (120,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.25,
            (0,0,255))

cv2.imshow("resultado",img)

gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("Escala de Cinza", gray_img)

cv2.waitKey(0)