import json
from pathlib import Path

import tqdm
import tqdm.auto

gazecapture = Path().cwd() / "gazecapture"

for dir in tqdm.auto.tqdm(gazecapture.iterdir()):
	print(dir)







# os.makedirs("dataset/0", exist_ok=True)
# os.makedirs("dataset/1", exist_ok=True)

# cnt = 0
# for data_id in sorted(os.listdir(root_dir)):

#     data_dir = os.path.join(root_dir, data_id)
#     if not os.path.isdir(data_dir):
#         continue

#     dotinfo_path = os.path.join(data_dir, "dotInfo.json")
#     if not os.path.exists(dotinfo_path):
#         continue

#     with open(dotinfo_path, "r") as f:
#         try:
#             dot_info = json.load(f)
#         except json.JSONDecodeError as e:
#             continue

#     x_cams = np.array(dot_info.get("XCam"))
#     y_cams = np.array(dot_info.get("YCam"))

#     distances = np.sqrt(x_cams**2 + y_cams**2)

#     distances_max = distances.max()

#     counts = sum(distances > distances_max * 0.9)

#     frames_dir = os.path.join(data_dir, "frames")
#     if not os.path.exists(frames_dir) or not os.path.isdir(frames_dir):
#         continue

#     for distance, frame_name in zip(distances, sorted(os.listdir(frames_dir))):
#         if not frame_name.endswith(".jpg"):
#             continue
#         cnt += 1
#         if distance > distances_max * 0.9:
#             src_path = os.path.join(frames_dir, frame_name)
#             dst_path = os.path.join("dataset", "0", f"{cnt:08d}.jpg")
#             os.system(f"cp {src_path} {dst_path}")
#         else:
#             src_path = os.path.join(frames_dir, frame_name)
#             dst_path = os.path.join("dataset", "1", f"{cnt:08d}.jpg")
#             os.system(f"cp {src_path} {dst_path}")
