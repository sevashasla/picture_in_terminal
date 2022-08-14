import numpy as np
from copy import copy

class ImageToBrailer():
    def __init__(self, image):
        self.BRAILLE_START = 10240
        self.BRAILLE_END = 10495
        self.WIDTH_STEP = 2
        self.HEIGHT_STEP = 4
        self.map4x2 = {
            (0, 0): 0,
            (1, 0): 1,
            (2, 0): 2,
            (0, 1): 3,
            (1, 1): 4,
            (2, 1): 5,
            (3, 0): 6,
            (3, 1): 7
        }
        self.pow2map4x2 = {el: 2**self.map4x2[el] for el in self.map4x2}

        self.image = copy(image)
        if self.image.shape[0] % self.HEIGHT_STEP != 0:
            need_add = self.HEIGHT_STEP - self.image.shape[0] % self.HEIGHT_STEP
            self.image = np.vstack((self.image, np.zeros((need_add, self.image.shape[1]), dtype=np.int)))

        if self.image.shape[1] % self.WIDTH_STEP != 0:
            need_add = self.WIDTH_STEP - self.image.shape[1] % self.WIDTH_STEP
            self.image = np.hstack((self.image, np.zeros((self.image.shape[0], need_add), dtype=np.int)))

    def array4x2ToSymbol(self, arr):
        result_idx = self.BRAILLE_START
        for el, power in self.pow2map4x2.items():
            result_idx += arr[el] * power
        return chr(result_idx)

    def array8x1ToSymbol(self, arr):
        result_idx = self.BRAILLE_START
        for el in arr:
            result_idx += 2 ** el
        return chr(result_idx)

    def show(self):
        for i in range(0, self.image.shape[0], self.HEIGHT_STEP):
            for j in range(0, self.image.shape[1], self.WIDTH_STEP):
                curr_arr = self.image[i:(i + self.HEIGHT_STEP), j:(j + self.WIDTH_STEP)]
                print(self.array4x2ToSymbol(curr_arr), end="")
            print()
