import time

def selection_sort(array, draw_rectangular_elements, delay):
    for i in range(len(array) - 1):
        min_ind = i
        for j in range(i+1, len(array)):
            if array[min_ind] > array[j]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
        draw_rectangular_elements(array, ['blue' if x == i or x == min_ind else '#FF5003' for x in range(len(array))])
        time.sleep(delay)
    draw_rectangular_elements(array, ['#00AB08' for x in range(len(array))])

