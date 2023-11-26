from app import Application
from responses import JSONResponse, TextResponse, HTMLResponse

app = Application()


@app.route("/health", method="GET")
def health():
    return JSONResponse({"status": "success"})


@app.route("/products", method="DELETE")
def create_products():
    return JSONResponse(
        {
            "products": [
                {
                    "name": "test",
                },
                {
                    "name": "test2",
                },
            ]
        }
    )


@app.route("/html", method="GET")
def html():
    import time

    time.sleep(5)
    return HTMLResponse("text.html")


@app.route("/text", method="GET")
def text():
    import time

    time.sleep(5)
    return TextResponse("IT IS TEXT")


if __name__ == "__main__":
    app.start()
