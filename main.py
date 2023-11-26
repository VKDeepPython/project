from app import Application
from responses import JSONResponse, TextResponse, HTMLResponse

app = Application()


@app.route("/health", method="GET")
def health(*args, **kwargs):
    return JSONResponse({"status": "success"})


@app.route("/products/<product_id>/info/<info_id>", method="POST")
def create_products(*args, **kwargs):
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
def html(*args, **kwargs):
    return HTMLResponse("text.html")


@app.route("/text/<id>/<name>", method="GET")
def text(*args, **kwargs):
    return TextResponse("IT IS TEXT")


if __name__ == "__main__":
    app.start()
