import os
import cv2
import mediapipe as mp
from matplotlib import pyplot as plt

image = cv2.imread("/home/parvez/reps/project/dataset/1/00185502.jpg")
h, w, _ = image.shape

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
	static_image_mode=True, max_num_faces=1, refine_landmarks=True
)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = face_mesh.process(image_rgb)

LEFT = [33, 133, 159, 145, 153, 154, 155]
RIGHT = [362, 263, 386, 374, 380, 381, 382]

if results.multi_face_landmarks:
	lms = results.multi_face_landmarks[0].landmark

	lx = [int(lms[i].x * w) for i in LEFT]
	ly = [int(lms[i].y * h) for i in LEFT]
	left_eye = image[
		max(min(ly) - 10, 0) : min(max(ly) + 10, h),
		max(min(lx) - 10, 0) : min(max(lx) + 10, w),
	]

	rx = [int(lms[i].x * w) for i in RIGHT]
	ry = [int(lms[i].y * h) for i in RIGHT]
	right_eye = image[
		max(min(ry) - 10, 0) : min(max(ry) + 10, h),
		max(min(rx) - 10, 0) : min(max(rx) + 10, w),
	]

	plt.subplot(1, 2, 1)
	plt.imshow(cv2.cvtColor(left_eye, cv2.COLOR_BGR2RGB))
	plt.subplot(1, 2, 2)
	plt.imshow(cv2.cvtColor(right_eye, cv2.COLOR_BGR2RGB))
	plt.tight_layout()
else:
	print("No face detected.")




