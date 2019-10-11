max_predicate = lambda a, b: a[2] <= b[2]

class Heap:
    def __init__(self):
        self.heap = []

    def heap_swap(self, a, b):
        t = self.heap[a]
        self.heap[a] = self.heap[b]


        self.heap[b] = t

    def _heapify(self, heap_size, x, predicate):
        left = 2 *  (x + 1) - 1
        right = 2 * (x + 1)

        largest = x

        if left < heap_size and predicate(self.heap[left], self.heap[x]):
            largest = left
        if right < heap_size and predicate(self.heap[right], self.heap[largest]):
            largest = right

        if largest != x:
            self.heap_swap(x, largest)
            self._heapify(heap_size, largest, predicate)

    def make_heap(self, h, comp=max_predicate):

        for i in range(len(h)):
            spectra_peak = h[i]
            self.heap.append([i, 0, spectra_peak])

        heap_size = len(self.heap)

        for i in reversed(range(0, heap_size //2)):
            self._heapify(heap_size, i, comp)

    def top(self):
        return self.heap[0]

    def empty(self):
        return self.heap == []

    def size(self):
        return len(self.heap)

    # Todo
    def pop_back(self):
        self.heap = self.heap[:-1]

    def pop_heap(self, predicate):

        pop_value = self.heap[0]
        self.heap_swap(0, len(self.heap)-1)
        self._heapify(len(self.heap) -1, 0, predicate)
        return pop_value

    def push_heap(self, value, predicate=max_predicate):
        self.heap.append(value)

        current = len(self.heap) - 1

        while current > 0:
            parent = (current - 1) // 2
            if predicate(self.heap[current], self.heap[parent]):
                self.heap_swap(parent, current)
                current = parent
            else:
                break

    def pop_and_feed(self, peak, comp=max_predicate):


        if self.empty():
            raise Exception("Heap::popAndFeed(): theVector must be non empty")

        returned_peak = self.heap[0]

        spectra_indx = returned_peak[0]
        peak_indx = returned_peak[1] + 1

        self.pop_heap(comp)

        spectra = peak[spectra_indx]

        if peak_indx < len(spectra):
            self.heap[self.size() - 1] = [spectra_indx, peak_indx, spectra[peak_indx]]
            self.push_heap(comp)
        else:
            self.pop_back()

        return returned_peak