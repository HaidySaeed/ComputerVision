1- What ’re the methods that you used ?

1_erosion and dilation
2_threshold
cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.
cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.
3_adaptive threshold
4_Otsu thresholding 



2- Explain each method ..
1_erosion:used to remove white noise or break two connected component 
          used to diminish the features of an image 
2_dilation:used to connect component and increase the object area 
3_threshold:used on grayscale image if pixels of image less than threshold it set to zero other set to 1
            and this useful for segmentation to extract specific object
4_ used to threshold images that has illumination 
5_otsu thresholding:the value of threshold detremined automatically


3- What’s new for you ?



4- Resources ? 
1- https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/?ref=lbp

2- https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/?ref=lbp

3- https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-2-adaptive-thresholding/?ref=lbp

4- https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-3-otsu-thresholding/?ref=lbp
