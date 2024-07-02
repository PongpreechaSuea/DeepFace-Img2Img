from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
# from src.main import FaceSwapper
from src.config import SOURCE_PATH, TARGET_PATH, HOST, PORT

app = FastAPI(
    title="DeepFace img to img",
    description="An advanced DeepFace system using AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# สร้างโฟลเดอร์ชื่อ 'templates' และวาง HTML file ของคุณไว้ที่นั่น
templates = Jinja2Templates(directory="templates")

# สร้างโฟลเดอร์ชื่อ 'static' สำหรับไฟล์ CSS และ JavaScript (ถ้ามี)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# face_swapper = FaceSwapper()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/swap-face/")
# async def swap_face(
#     source: UploadFile = File(...),
#     target: UploadFile = File(...),
#     full_generate: bool = False
# ):
#     try:
#         # อ่านไฟล์รูปภาพ
#         source_image = Image.open(io.BytesIO(await source.read()))
#         target_image = Image.open(io.BytesIO(await target.read()))

#         source_image.save(SOURCE_PATH)
#         target_image.save(TARGET_PATH)

#         # เรียกใช้ฟังก์ชัน swap_face
#         result_image = face_swapper.swap_face(SOURCE_PATH, TARGET_PATH, full_generate)

#         # แปลงรูปภาพผลลัพธ์เป็น bytes
#         img_byte_arr = io.BytesIO()
#         result_image.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         # ส่งคืนรูปภาพ
#         return StreamingResponse(io.BytesIO(img_byte_arr), media_type="image/jpeg")

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
