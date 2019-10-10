import unittest
import csv
from pymsvlm import msAlign as ms

def read_data() -> list:
    list_of_spectra = []
    with open("./data/alignment.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            list_of_strings = list(row)
            spectrum = []
            for s in list_of_strings:
                spectrum.append(float(s))
            list_of_spectra.append(spectrum)
    return list_of_spectra

class Tests(unittest.TestCase):

    def test_find_vlm(self):
        print(ms.find_vlm(read_data(), 5e-6))

    def test_find_alpt(self):
        #print(ms.find_alpt(read_data(), 5e-6))
        pass

if __name__ == "__main__":
    unittest.main()