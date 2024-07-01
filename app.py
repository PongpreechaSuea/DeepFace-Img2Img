from fastapi import FastAPI, File, UploadFile, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from src.config import *
from PIL import Image
import cv2
import io
import asyncio


app = FastAPI(
    title="DeepFace img to img",
    description="An advanced DeepFace system using AI",
    version="1.0.0"
)

# developing


if __name__ == "__main__":
    print(f"BASE_URL: {BASE_URL}/docs")
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)