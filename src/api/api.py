import hashlib
import io
import json
import sys
from typing import List

import uvicorn
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image

sys.path.append("..")
from modules.analyze_text import analyze_text  # type:ignore
from modules.perform_ocr import perform_ocr  # type:ignore
from my_redis.redis_config import redis_client  # type:ignore

app = FastAPI()
templates = Jinja2Templates(directory="../../templates")
app.mount("/static", StaticFiles(directory="../../static"), name="static")

supported_image_mimes = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/svg+xml",
    "image/webp",
    "image/apng",
    "image/avif",
]


@app.get("/", response_class=HTMLResponse)
async def read_search_form(request: Request):
    """
    Serves the HTML form to upload images.

    Args:
        request (Request): The HTTP request object.

    Returns:
        TemplateResponse: HTML form template response.
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "status": "Success"}
    )


@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Handles uploaded image files, performs OCR on content, and analyzes the text.

    Args:
        files (List[UploadFile]): List of uploaded image files.

    Returns:
        JSONResponse: Analysis results in JSON format.
    """
    results = []
    for uploaded_file in files:
        if uploaded_file.content_type not in supported_image_mimes:
            response_body = {"status": "bad request. wrong file format"}
            return JSONResponse(content=response_body, status_code=400)

        contents = await uploaded_file.read()
        image = Image.open(io.BytesIO(contents))
        text = await perform_ocr(image)
        if not text:
            raise HTTPException(status_code=204, detail="No content provided")

        hashed_key = hashlib.md5(text.encode()).hexdigest()

        cached_result = redis_client.get(hashed_key)
        if cached_result:
            analysis_result = json.loads(cached_result)
        else:
            analysis_result = await analyze_text(text)  
            redis_client.setex(hashed_key, 300, json.dumps(analysis_result))

        results.append(analysis_result)

    return JSONResponse(content=results)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
