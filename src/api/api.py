import sys
from typing import List

sys.path.append("..")
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modules.perform_ocr import perform_ocr
from modules.analyze_text import analyze_text
from my_redis.redis_config import redis_client

from PIL import Image
import io
import json
import hashlib

app = FastAPI()
templates = Jinja2Templates(directory="../../templates")
app.mount("/static", StaticFiles(directory="../../static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_search_form(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "status": "Success"}
    )

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = await perform_ocr(image)
        if not text:
            raise HTTPException(status_code=204, detail="No content provided")
        
        hashed_key = hashlib.md5(text.encode()).hexdigest()  # Hash the text using MD5
        
        cached_result = redis_client.get(hashed_key)
        if cached_result:
            analysis_result = json.loads(cached_result)  # Load JSON data from cache
        else:
            analysis_result = await analyze_text(text)  # Analyze the extracted text
            redis_client.setex(hashed_key, 300, json.dumps(analysis_result))  # Convert to JSON and cache
        
        results.append(analysis_result)  # Append the analysis result to the list
    
    return JSONResponse(content=results)  # Return the list of analysis results as JSON

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
