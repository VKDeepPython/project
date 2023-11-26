from app import Application
from responses import JSONResponse

if __name__ == "__main__":
    app = Application()

    @app.route('/hello', method="GET")
    def hello():
        return JSONResponse({"res GET": "sdjasdjasodhi, World!"})
    

    @app.route('/hello', method="POST")
    def hello():
        return JSONResponse({"res POST": "sdjasdjasodhi, World!"})
    

    @app.route('/health', method="GET")
    def hello():
        # return {"status success"}
        return JSONResponse({"status": "success"})

    app.start()