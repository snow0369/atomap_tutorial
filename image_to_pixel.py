import cv2

from convert_tiff_to_grayscale import convert_tiff_to_grayscale

if __name__ == "__main__":
    filename = 'image/1716_DPC_12.0_Mx_DF4_crop.tif'
    filename = convert_tiff_to_grayscale(filename)
    img = cv2.imread(filename)
    print(img.shape)
    print(img)
    norm = 256
    if len(img.shape) == 3:
        img_intensity = img[:, :, 0] / norm
    elif len(img.shape) == 2:
        img_intensity = img / norm
    else:
        raise ValueError
    print(img_intensity)
    out_filename = 'image/1716_DPC_12.0_Mx_DF4_crop_GS_unchanged.tif'
    cv2.imwrite(out_filename, img)
