# Python program to capture a single image
# using pygame library

# importing the pygame library
# import pygame
# import pygame.camera

# # initializing the camera
# pygame.camera.init()

# # make the list of all available cameras
# camlist = pygame.camera.list_cameras()

# # if camera is detected or not
# if camlist:

# 	# initializing the cam variable with default camera
# 	cam = pygame.camera.Camera(camlist[0], (640, 480))

# 	# opening the camera
# 	cam.start()

# 	# capturing the single image
# 	image = cam.get_image()

# 	# saving the image
# 	pygame.image.save(image, "filename.jpg")

# # if camera is not detected the moving to else part
# else:
# 	print("No camera on current device")



import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("dashaDoor.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
