import numpy as np
import cv2

#Test the model by feeding an Road bike image randomly
img = cv2.imread("./bikes/examplesbike/road.jpeg")
img = img.copy()
img = cv2.resize(img, (150,150))
img = img.reshape(1,150,150,3)

j = model.predict(img)


img = cv2.imread("./bikes/examplesbike/road.jpeg")
if j == 0 :
        cv2.putText(img, 'Mountain Bike', (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
					0.7, (0, 255, 0), 2)
        cv2.imshow("output",img)
else:
        cv2.putText(img, 'Road Bike', (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
					0.7, (0, 255, 0), 2)
        cv2.imshow("Output",img)
        
cv2.waitKey(0)
cv2.destroyAllWindows()
