import sys
sys.path.append('./CodeFormer/CodeFormer')

import onnxruntime
import torch
import cv2
import numpy as np
from PIL import Image
from src.swapper import *
from src.restoration import *
from src.config import *

class FaceSwapper:
    def __init__(self):
        self.check_ckpts()
        self.providers = onnxruntime.get_available_providers()
        self.face_analyser = self.getFaceAnalyser()
        self.face_swapper = self.getFaceSwapModel()
        self.upsampler = self.set_realesrgan()
        self.device = self.set_device()

    def check_ckpts(self):
        check_ckpts()

    def getFaceAnalyser(self):
        return getFaceAnalyser(MODEL, self.providers)

    def getFaceSwapModel(self):
        return getFaceSwapModel(MODEL_PATH)

    def set_realesrgan(self):
        return set_realesrgan()

    def set_device(self):
        return torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")

    def swap_face(self, input_source, target_source, full_generate=False):
        source_img = [Image.open(input_source)]
        target_img = Image.open(target_source)

        if full_generate:
            result_image = process(source_img, target_img, SOURCE_INDEXES, TARGET_INDEXES, MODEL)
            codeformer_net = self.setup_codeformer()

            result_image = cv2.cvtColor(np.array(result_image), cv2.COLOR_RGB2BGR)
            result_image = face_restoration(
                result_image, 
                BACKGROUND_ENHANCE, 
                FACE_UPSAMPLE, 
                UPSCALE, 
                CODEFORMER,
                self.upsampler,
                codeformer_net,
                self.device
            )
            result_image = Image.fromarray(result_image)
        else:
            result_image = process(source_img, target_img, SOURCE_INDEXES, TARGET_INDEXES)

        return result_image

    def setup_codeformer(self):
        codeformer_net = ARCH_REGISTRY.get("CodeFormer")(
            dim_embd=DIM_EMBD,
            codebook_size=CODEBOOK_SIZE,
            n_head=N_HEAD,
            n_layers=N_LAYERS,
            connect_list=CONNECT_LIST,
        ).to(self.device)
        ckpt_path = MODEL_CODEFORMER
        checkpoint = torch.load(ckpt_path)["params_ema"]
        codeformer_net.load_state_dict(checkpoint)
        codeformer_net.eval()
        return codeformer_net

# ตัวอย่างการใช้งาน:
swapper = FaceSwapper()
result = swapper.swap_face("./30868.jpg", "./LINE_ALBUM_news_240702_1.jpg", full_generate=True)
result.save("./output.jpg")

