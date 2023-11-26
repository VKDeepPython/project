from app import Application
from responses import JSONResponse, TextResponse, HTMLResponse, HTMLTextResponse
from database import Model, users
from renderTemplate.render_template import render_template

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
    # print(users.all())

    return JSONResponse({"response": user})

@app.route("/user", method="GET")
def get_users(*args, **kwargs):
    res = users.all()

    return JSONResponse({"response": res})

@app.route("/user_template/<id>", method="GET")
def get_users_template(*args, **kwargs):
    pattern_dict = args[0]
    # print(pattern_dict)
    # print(f"id = {pattern_dict['id']}")
    user_id = int(pattern_dict['id'])
    user = users.find('id', user_id)
    user_name = user[0][1]
    user_age = user[0][2]
    print(f"username = {user_name}")
    # html = render_template()
    # res = users.all()
    html = render_template(
        "templates/user.html", 
        name=user_name, 
        age=user_age,
    )

    # return HTMLResponse("text.html")
    # return TextResponse(html)
    return HTMLTextResponse(html)

@app.route("/user_template2/<id>", method="GET")
def get_users_template1(*args, **kwargs):
    pattern_dict = args[0]
    user_id = int(pattern_dict['id'])
    user = users.find('id', user_id)
    user_name = user[0][1]
    user_age = user[0][2]
    html = render_template(
        "templates/user.html", 
        name=user_name, 
        age=user_age,
    )

    return TextResponse(html)

@app.route("/user_template3/<id>", method="GET")
def get_users_template2(*args, **kwargs):
    params_dict = args[1]
    pattern_dict = args[0]
    user_id = int(pattern_dict['id'])
    user = users.find('id', user_id)
    user_name = user[0][1]
    user_age = user[0][2]
    is_age = False
    try:
        is_age = params_dict['is_age'] 
    except Exception as e:
        pass

    print(f"is age {params_dict}")
    print(f"is age {is_age}")

    html = render_template(
        "templates/user2.html", 
        name=user_name, 
        age=user_age,
        is_age=bool(is_age)
    )

    return HTMLTextResponse(html)

if __name__ == "__main__":
    app.start()
