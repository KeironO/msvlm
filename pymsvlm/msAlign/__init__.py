from .ActiveSequence import ActiveSequence
from .Heap import Heap

def remove_overlaps(tentative_alignment_point: str, window_size: float):
    alignment_point = []

    n = len(tentative_alignment_point)

    is_overlapping = [False for _ in range(n)]

    if n == 0:
        return tentative_alignment_point

    for index, i in enumerate(tentative_alignment_point[:-1]):
        if (1.0 + window_size) * tentative_alignment_point[i] >= (1.0 - window_size) * tentative_alignment_point:
            is_overlapping[index] = True
            is_overlapping[index + 1] = True

    for index, i in enumerate(tentative_alignment_point):
        if not is_overlapping[index]:
            alignment_point.append(i)

    return alignment_point

def alignment_point_detection(peaks: list, window_size: float, for_vlm: bool):
    tentative_alignment_point = []

    num_spectra = len(peaks)

    heap = Heap()

    heap.make_heap(peaks)

    active_sequence = ActiveSequence(num_spectra, window_size, for_vlm)

    found = False

    while not heap.empty():
        if active_sequence.is_valid(heap):
            found = True

        if active_sequence.insert(heap, peaks):
            if found:
                tentative_alignment_point.append(active_sequence.get_average_mz())
                found = False
            active_sequence.advance_lower_bound()
        else:
            if heap.empty():
                while not active_sequence.empty():
                    if active_sequence.is_valid(heap):
                        tentative_alignment_point.append(active_sequence.get_average_mz())
                        break
                    active_sequence.advance_lower_bound()

    return remove_overlaps(tentative_alignment_point, window_size)

def find_vlm(peaks: list, window_size: float):
    return alignment_point_detection(peaks, window_size, True)

def find_alpt(peaks: list, window_size: float):
    return alignment_point_detection(peaks, window_size, False)