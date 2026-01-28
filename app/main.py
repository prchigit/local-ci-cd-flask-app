from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({"message": "Production Flask App Running"})

    @app.route("/add")
    def add():
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})

    return app


app = create_app()

