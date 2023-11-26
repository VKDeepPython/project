from app import Application
from responses import JSONResponse, TextResponse, HTMLResponse
from database import Model, users

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


@app.route("/user", method="POST")
def create_user(*args, **kwargs):
    body = args[2]
    print(f"name={body['name']}, age={body['age']}")
    users.insert(["name", "age"], [body['name'], body['age']])
    user = users.find("name", body['name'])
    return JSONResponse({"status": user})


@app.route("/user/<id>", method="GET")
def get_user(*args, **kwargs):
    pattern_dict = args[0]
    user = users.find("id", pattern_dict['id'])
    print(users.all())

    return JSONResponse({"response": user})

@app.route("/user", method="GET")
def get_users(*args, **kwargs):
    res = users.all()

    return JSONResponse({"response": res})

if __name__ == "__main__":
    app.start()
