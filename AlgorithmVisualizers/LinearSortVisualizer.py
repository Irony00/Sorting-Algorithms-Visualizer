from Engine.Visualizer import Visualizer

class LinearSortVisualizer(Visualizer):
    def __init__(self):
        pass
    
    def linear_sort_visualize(self, random_array):
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
            visualized_frame = self.visualize(
                random_array = random_array,
                highlight_index = j + 1
            )
            self.render_frame(visualized_frame)