import os

import matplotlib
import matplotlib.pyplot as plt
import hyperspy.api as hs
import atomap.api as am
import numpy as np

import atomap.dummy_data as dummy_data
import cv2
# from PIL import Image

matplotlib.rcParams['backend'] = 'nbagg'

if __name__ == "__main__":
    # dum = dummy_data.get_simple_cubic_signal(image_noise=True)
    filename = 'image/1716_DPC_12.0_Mx_DF4_crop.tif'

    # img = Image.open(filename).convert("LA")
    sp = filename.split('.')
    new_filename = ".".join(sp[:-1]) + "_GS." + sp[-1]
    if not os.path.isfile(new_filename):
        img = cv2.imread(filename)
        cv2.imwrite(new_filename, img[:, :, 1])
    filename = new_filename
    img = hs.load(filename, convert_units=True)

    img.axes_manager['width'].units = 'nm'
    img.axes_manager['width'].scale = 0.004
    img.axes_manager['height'].units = 'nm'
    img.axes_manager['height'].scale = 0.004
    # print(img.axes_manager.as_dictionary())
    # 0. Draw Plot
    img.plot()
    plt.show()
    # for idx, val in np.ndenumerate(img.data):
    #     i, j = idx
    #     assert val[0] == val[1] == val[2] and val[3] == 255
    #     img.data[i][j] = val[0]
    print(img.data)

    # 1. Finding the feature separation
    # Error, we need to reduce the dimension (Gray scale)
    s_peaks = am.get_feature_separation(img, separation_range=(5, 30), show_progressbar=True)
    s_peaks.plot()
    plt.show()
