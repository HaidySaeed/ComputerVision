1- The methods used:

a-Optical Flow with Lucas-Kanade method
b-Dense optical flow
c-Visualizing image in different color spaces
d-Find Co-ordinates of Contours using OpenCV 
e-Find and Draw Contours using OpenCV
f-Draw a rectangular shape and extract objects
g-cv2.rectangle() method
h- cv2.putText() method


2- Explain each method 
a-Optical Flow with Lucas-Kanade method:track some points on a video. To track the points, first, we need to find the points to be tracked. For finding the points, we’ll use cv2.goodFeaturesToTrack()

b-Dense optical flow:Optical flow is the motion of objects between the consecutive frames of the sequence, caused by the relative motion between the camera and the object. It can be of two types-Sparse Optical flow and Dense Optical flow

c-Visualizing image in different color spaces:represent images in different formats like grayscale, RGB scale, Hot_map, edge map, Spectral map, etc

d-Find Co-ordinates of Contours using OpenCV :
The Co-ordinates of each vertices of a contour is hidden in the contour itself. In this approach, we will be using numpy library to convert all the co-ordinates of a contour into a linear array. This linear array would contain the x and y co-ordinates of each contour. The key point here is that the first co-ordinate in the array would always be the co-ordinate of the topmost vertex and hence could help in detection of orientation of an image

e-Find and Draw Contours using OpenCV:Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity. Contours come handy in shape analysis, finding the size of the object of interest, and object detection.

f-Draw a rectangular shape and extract objects:select desired portion in an image and extract that selected portion as well,draw shape on any image,re-select the extract portion for in case bad selection,extract particular object from the image
g-cv2.rectangle() method:is used to draw a rectangle on any image
h- cv2.putText() method:is used to draw a text string on any image



3-Optical Flow with Lucas-Kanade method,-Dense optical flow,-Visualizing image in different color spaces,-Find Co-ordinates of Contours using OpenCV,-Find and Draw Contours using OpenCV


4- Resources:

a- https://www.geeksforgeeks.org/python-opencv-optical-flow-with-lucas-kanade-method/?ref=lbp

b- https://www.geeksforgeeks.org/python-opencv-dense-optical-flow/?ref=lbp

c- https://www.geeksforgeeks.org/python-visualizing-image-in-different-color-spaces/?ref=lbp

d- https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/?ref=lbp

e- https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/?ref=lbp

f- https://www.geeksforgeeks.org/python-draw-rectangular-shape-and-extract-objects-using-opencv/?ref=lbp

g- https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/?ref=lbp

h- https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/?ref=lbp

