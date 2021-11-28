import cv2
import time
import numpy as np
import multiprocessing

from AlgorithmVisualizers.LinearSortVisualizer import LinearSortVisualizer
from AlgorithmVisualizers.MergeSortVisualizer import MergeSortVisualizer

array_width = 800
array_height = 300

random_array = np.random.randint(1, array_height + 1, array_width)

def process_one():
    linear_sort = LinearSortVisualizer()
    linear_sort.linear_sort_visualize(random_array)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_two():
    n = len(random_array)
    merge_sort = MergeSortVisualizer()
    merge_sort.merge_sort_visualize(random_array, 0, n - 1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

p1 = multiprocessing.Process(target = process_one)
p2 = multiprocessing.Process(target = process_two)

p1.start()
p2.start()

p1.join()
p2.join()