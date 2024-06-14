import cv2
vidcap = cv2.VideoCapture('DATA/animacion_sandy/VID_20231020_151124.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(f"DATA/animacion_sandy/frame{count}.jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1