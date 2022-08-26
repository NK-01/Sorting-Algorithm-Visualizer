import time

def bubble_sort(array, draw_rectangular_elements, delay):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_rectangular_elements(array, ['blue' if x == j or x == j + 1 else '#FF5003' for x in range(len(array))])
                time.sleep(delay)
    draw_rectangular_elements(array, ['#00AB08' for x in range(len(array))])