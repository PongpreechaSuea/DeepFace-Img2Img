import os

MODEL = "./checkpoints/model_swap_face.onnx"
MODEL_CODEFORMER = os.path.abspath("./src/CodeFormer/CodeFormer/weights/CodeFormer/codeformer.pth")
MODEL_REALESRGANER = os.path.abspath("./src/CodeFormer/CodeFormer/weights/realesrgan/RealESRGAN_x2plus.pth")
MODEL_PATH = os.path.join(os.path.abspath("./"), MODEL.replace("./", ""))

FULL_GENERATE = True

DIM_EMBD=512
CODEBOOK_SIZE=1024
N_HEAD=8
N_LAYERS=9
CONNECT_LIST=["32", "64", "128", "256"]

RRDBNET_IN_CHANNELS=3
RRDBNET_OUT_CHANNELS=3
RRDBNET_GROW_CHANNELS=32
RRDBNET_FEAT_NUM=64
RRDBNET_BLOCK_NUM=23
SCALE=2

SOURCE_INDEXES="-1"
TARGET_INDEXES="-1"
FACE_RESTORE="store_true"
BACKGROUND_ENHANCE="store_true"
FACE_UPSAMPLE="store_true"
UPSCALE=1
CODEFORMER=0.5

SOURCE_PATH = "temp_source.jpg"
TARGET_PATH = "temp_target.jpg"

HOST = "0.0.0.0"
PORT = 8000
BASE_URL = f"http://{HOST}:{PORT}/"