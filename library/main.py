from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import sqlite3
from flask_sqlalchemy import SQLAlchemy

import csv

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# CREATE RECORD
# new_book = Book(id=1, title="mar", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

class BookForm(FlaskForm):
    bookName = StringField('Book Name', validators=[DataRequired()])
    bookAuthor = StringField("Author Name", validators=[DataRequired()])
    bookRating = StringField("Coffee Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    # print(db.select([Book]))
    # all_books = db.session.commit()
    # print(all_books)
    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add_book():
    # form = BookForm()
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

