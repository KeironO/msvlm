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
        if self.empty():
            raise Exception("ActiveSequence::advanceLowerBound(): ActiveSequence must be non empty")

        old_size = len(self._the_list)
        t = self._the_list[0]

        if t[0] >= self.num_spectra:
            raise Exception("ActiveSequence::advanceLowerBound(): get<0>(t] >= nbOfSpectra")

        if t[0] == False:
            raise Exception("ActiveSequence::advanceLowerBound(): that spectrum should be present")

        self._the_list = self._the_list[1:]

        self._spectra_present[t[0]] = False

        mz_lb = t[2]

        new_size = len(self._the_list)

        print(self._the_list)

        if new_size == 0:
            self.mz_avg = 0
        else:
            self.mz_avg = (float(old_size) * mz_lb) / float(new_size)


    def insert(self, heap, peak):
        if heap.empty():
            return False

        if self.empty():
            t = heap.pop_and_feed(peak)

            if t[0] >= self.num_spectra:
                raise Exception("ActiveSequence::insert(): get<0>(t] >= nbOfSpectra")

            if self._spectra_present[t[0]]:
                raise Exception("ActiveSequence::insert(): this spectra should be absent")

            self._spectra_present[t[0]] = True
            self._the_list.append(t)

            self.mz_avg = t[2]
            return True

        else:

            t = heap.top()
            if t[0] >= self.num_spectra:
                raise Exception("ActiveSequence::insert(): get<0>(t] >= nbOfSpectra")

            spectra_indx = t[0]

            mz = t[2]

            if self._spectra_present[spectra_indx]:
                return False

            old_size = len(self._the_list)

            new_mz_avg = (float(old_size) + mz) / float(old_size) +1

            if mz <= new_mz_avg * (  1 * self.window_size ):
                if self._the_list[0][2] >= new_mz_avg * (1 - self.window_size):
                    self._spectra_present[spectra_indx] = True
                    self.mz_avg = new_mz_avg
                    self._the_list.append(heap.pop_and_feed(peak))
                    return True

            return False