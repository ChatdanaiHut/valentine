from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

html_folder = Path(r"C:\Users\BROTHER_PC\Desktop\Coding\valentine\valentine")

@app.get("/")
def read_root():
    file_path = html_folder / "index.html"   # adjust filename if needed
    return HTMLResponse(content=file_path.read_text(encoding="utf-8"), status_code=200)
