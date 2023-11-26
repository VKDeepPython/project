from app import Application

if __name__ == "__main__":
    app = Application()

    @app.route('/hello', method="GET")
    def hello():
        return {"sdjasdjasodhi, World!"}

    app.start()