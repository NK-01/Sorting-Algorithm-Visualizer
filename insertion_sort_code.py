import time
def insertion_sort(array, draw_rectangular_elements, delay):
    for i in range(len(array) - 1):
        j = i + 1
        while j > 0:
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                draw_rectangular_elements(array,['blue' if x == j or x == j + 1 else '#FF5003' for x in range(len(array))])
                time.sleep(delay)
            else:
                break
            j -= 1
    draw_rectangular_elements(array, ['#00AB08' for x in range(len(array))])