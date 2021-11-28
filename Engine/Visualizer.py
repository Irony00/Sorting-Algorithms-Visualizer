import cv2
import numpy as np

class Visualizer:
    def __init__(self):
        pass

    def visualize(self, random_array, highlight_index = None):
        canvas_width = random_array.shape[0]
        canvas_height = random_array.max()

        canvas = []

        for (index, integer) in enumerate(random_array):
            filled_bar = [(255.0, 255.0, 255.0)] * integer
            if highlight_index is not None and index == highlight_index:
                filled_bar = [(0.0, 0.0, 255.0)] * integer

            empty_bar = [(0.0, 0.0, 0.0)] * (canvas_height - integer)
            bar = filled_bar + empty_bar
            canvas.append(bar)

        return np.rot90(np.array(canvas))