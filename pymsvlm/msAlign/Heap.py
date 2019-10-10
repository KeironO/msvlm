class Heap:
    def __init__(self, peaks: list):
        self.peaks = peaks

        self._heap = []

        for i, peak in enumerate(self.peaks):
            self._heap.append([i, 0, peak])


    def empty(self):
        return self._heap == []

    def size(self) -> int:
        return len(self._heap)

    def top(self) -> float:
        return self.heap[0]

    def pop_and_feed(self, peak):

        def _pop_heap():
            front, back = self._heap[0], self._heap[1]

            if front[2] >= back[2]:
                self._heap[0] = back
                self._heap[-1] = front

        if self.empty():
            raise AttributeError("Heap::popAndFeed(): theVector must be non empty")

        returned_peak = self._heap[0]

        spectra_indx = returned_peak[0]
        peak_indx = returned_peak[1] + 1

        spectra = peak[spectra_indx]

        if peak_indx < len(spectra):
            self._heap[len(self._heap) - 1] = [spectra_indx, peak_indx, spectra[peak_indx]]

            #pop heap?
            _pop_heap()
        else:
            # pop back
            self._heap = self._heap[:-1]

        return returned_peak

    def _comp(self, a, b):
        return a[2] >= b[2]

    def __repr__(self):
        return self._heap