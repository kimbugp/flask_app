from flask import Blueprint, request, Response

sample_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["GET"])
def home():
    form = RegisterForm(request.form)
    return Response({"msg": "Hello"}, 200)