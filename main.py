from app import Application
from responses import JSONResponse, TextResponse, HTMLResponse

app = Application()

@app.route("/health", method="GET")
def health():
    return JSONResponse({"status": "success"})

@app.route("/html", method="GET")
def html():
    return HTMLResponse("text.html")

@app.route("/text", method="GET")
def text():
    return TextResponse("IT IS TEXT")

if __name__ == "__main__":
    app.start()
