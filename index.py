import cv2
import time
import numpy as np
from Engine.Visualizer import Visualizer

random_array = np.random.randint(1, 501, 500)
visualizer = Visualizer()

canvas = cv2.namedWindow('Canvas', cv2.WINDOW_AUTOSIZE)

# Traverse through 1 to len(arr)
for i in range(1, len(random_array)):

    # Sorting Logic
    key = random_array[i]
    j = i - 1
    while j >=0 and key < random_array[j] :
            random_array[j + 1] = random_array[j]
            j -= 1
    random_array[j + 1] = key

    # Visualizing each frame
    visualize = visualizer.visualize(
        random_array = random_array,
        highlight_index = j + 1
    )
    cv2.imshow("Canvas", visualize)
    
    # If ESC is pressed, exit loop
    key_pressed = cv2.waitKey(1)
    if key_pressed == 27: 
        cv2.destroyAllWindows()
        break

cv2.waitKey(0)
cv2.destroyAllWindows()