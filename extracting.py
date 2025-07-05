import os
import tarfile
from pathlib import Path

src_dir = Path.home() / "Documents" / "datasets" / "Gaze"
dst_dir = Path("./gazecapture")
# dst_dir.mkdir(parents=True, exist_ok=True)

# for tar_path in src_dir.glob("*.tar.gz"):
# 	with tarfile.open(tar_path, "r:gz") as tar:
# 		tar.extractall(path=dst_dir)
archives = src_dir.glob("*.tar.gz")
for i in archives:
    print(i)
    with tarfile.open(i, "r:gz") as tar_reader:
        tar_reader.extractall(dst_dir)
