# import os
#
# from flask import Flask, render_template, redirect
# from flask import request
# from flask_sqlalchemy import SQLAlchemy
#
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "mysql+pymysql://root:admin123@localhost/gbl"
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
#
# db = SQLAlchemy(app)
#
#
# class tagging_tag(db.Model):
#     id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#
#     def __repr__(self):
#         return "<ID: {}, Name: {}>".format(self.id, self.name)
#
#
# @app.route("/blog", methods=["GET", "POST"])
# def home():
#     if request.form:
#         book = tagging_tag(id=request.form.get("id"),
#                            name=request.form.get("name"))
#         db.session.add(book)
#         db.session.commit()
#
#     tags = tagging_tag.query.all()
#
#     return render_template("blog_home.html", tags=tags)
#
#
# @app.route("/update", methods=["POST"])
# def update():
#     newtitle = request.form.get("newtitle")
#     oldtitle = request.form.get("oldtitle")
#     book = Book.query.filter_by(title=oldtitle).first()
#     book.title = newtitle
#     db.session.commit()
#     return redirect("/")
#
#
# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")
#
#
# if __name__ == "__main__":
#     # app.run(debug=True)
#     app.run(threaded=True)