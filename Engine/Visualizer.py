import cv2
import numpy as np

class Visualizer:
    def __init__(self):
        self.canvas = cv2.namedWindow('Canvas', cv2.WINDOW_AUTOSIZE)

    def visualize(self, random_array, highlight_index = None):
        canvas_width = random_array.shape[0]
        canvas_height = random_array.max()

        canvas = []

        for (index, integer) in enumerate(random_array):
            filled_bar = [1.0] * integer
            if highlight_index is not None and index == highlight_index:
                filled_bar = [0.5] * integer

            empty_bar = [0] * (canvas_height - integer)
            bar = filled_bar + empty_bar
            canvas.append(bar)

        return np.rot90(np.array(canvas))
    
    def render_frame(self, frame):
        cv2.imshow("Canvas", frame)
        
        # If ESC is pressed, exit
        key_pressed = cv2.waitKey(1)
        if key_pressed == 27: 
            cv2.destroyAllWindows()