import matplotlib.pyplot as plt
import numpy as np
import atomap.dummy_data as dummy_data

if __name__ == "__main__":
    s = dummy_data.get_simple_cubic_signal(image_noise=True)
    # for k in s.__dict__:
    #     print(k)
    pixels = np.array(s.data)
    print(pixels.shape)
    plt.imshow(pixels)
    plt.show()
