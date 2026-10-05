from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    if data is None:
        return {"message": "Data from pictures are empty"}, 200
    else:
        return jsonify(data), 200


######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    if data is None:
        return {"message": "Data from pictures are empty"}, 200
    else:
        picture = next((item for item in data if item["id"] == id), None)
        if picture is not None:
            return jsonify(picture), 200
        else:
            return {"message": f"picture with id {id} not found"}, 404


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    if data is None:
        return {"message": "Data from pictures are empty"}, 200
    else:
        if not request.get_json():
            return {"message": "Content-Type must be application/json"}, 415
        picture = request.get_json()
        new_picture = next((item for item in data if item["id"] == picture["id"]), None)
        if new_picture is not None:
            return {"Message": f"picture with id {new_picture['id']} already present"}, 302
        try:
            data.append(picture)
            return jsonify(picture), 201
        except Exception as e:
            return {"message": f"Error to add new picture with id {new_picture['id']}"}, 500


######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    if data is None:
        return {"message": "Data from pictures are empty"}, 200
    else:
        picture = next((item for item in data if item["id"] == id), None)
        if picture is not None:
            updated_picture = request.json
            picture.update(updated_picture)
            return jsonify(picture), 200
        else:
            return {"message": f"picture with id {id} not found"}, 404


######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    if data is None:
        return {"message": "Data from pictures are empty"}, 200
    else:
        picture = next((item for item in data if item["id"] == id), None)
        if picture is not None:
            data.remove(picture)
            return jsonify({"message": f"picture with id {id} deleted"}), 204
        return {"message": f"picture with id {id} not found"}, 404
