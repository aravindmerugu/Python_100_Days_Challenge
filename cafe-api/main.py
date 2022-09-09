import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.get(random.randint(1,22))
    return jsonify(cafe=cafes.to_dict())

@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    cafes_dict = []
    for cafe in cafes:
        cafes_dict.append(cafe.to_dict())
    return jsonify(cafes_dict)

@app.route("/search")
def get_cafe_at_location():
    try:
        query_location = request.args.get("loc")
        cafe = db.session.query(Cafe).filter_by(location=query_location).first()
        return jsonify(cafes=cafe.to_dict())
    except AttributeError:
        return jsonify({
            "error" : {
            "not found" : "Sorry, we don't have a cafe at that location"
        }
        }
        )

@app.route("/add",methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def patch_update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response = {
            "success": "successfully updated the price"
        }), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete:
        if api_key == 'TopSecretAPIKey':
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response = {
                "sucess" : "The cafe has been deleted from the existing database"
            }), 200
        return jsonify(
            response = {
                "APIKEYERROR" : "Make sure you have the correct API key"
            }
        ), 403
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
