import cv2
import time
import numpy as np

from AlgorithmVisualizers.LinearSortVisualizer import LinearSortVisualizer
from AlgorithmVisualizers.MergeSortVisualizer import MergeSortVisualizer

array_width = 1000
array_height = 500

random_array = np.random.randint(1, array_height + 1, array_width)

# linear_sort = LinearSortVisualizer()
# linear_sort.linear_sort_visualize(random_array)

n = len(random_array)
merge_sort = MergeSortVisualizer()
merge_sort.merge_sort_visualize(random_array, 0, n - 1)

cv2.waitKey(0)
cv2.destroyAllWindows()