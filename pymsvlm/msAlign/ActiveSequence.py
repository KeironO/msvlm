class ActiveSequence:
    def __init__(self, num_spectra: int, window_size: float, p_vlm: float):
        self.num_spectra = num_spectra
        self.window_size = window_size
        self.p_vlm = p_vlm

        self._the_list = []

        self.mz_avg = 0.0
        self.mz_lb = -50

        self._spectra_present = [False for _ in range(num_spectra)]

    def is_valid(self, heap):
        if self.p_vlm:
            if self._the_list != self.num_spectra:
                return False

        elif self.empty():
            return False

        elif not heap.empty():
            if heap.top() <= self.mz_avg * (1.0 + self.window_size):
                return False

        elif self._the_list[-1] > self.mz_avg*(1.0 - self.window_size):
            return False

        elif self._the_list[0] < self.mz_avg * (1.0 - self.window_size):
            return False

        else:
            return self.mz_lb < self.mz_avg*(1.0 - self.window_size)

    def empty(self):
        return len(self._the_list) == 0

    def advance_lower_bound(self):
        old_size = len(self._the_list)
        t = self._the_list[0]

        self._the_list = self._the_list[1:]

        self._spectra_present[t[0]] = False

        mz_lb = t[2]

        new_size = len(self._the_list)

        print(self.mz_avg)

        if new_size == 0:
            self.mz_avg = 0
        else:
            self.mz_avg = (float(old_size) * mz_lb) / float(new_size)




    def insert(self, heap, peak):
        pass