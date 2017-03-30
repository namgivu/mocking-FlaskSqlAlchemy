from app import db


class SomeModel(db.Model):
  #table mapping
  __tablename__ = "some_table"

  #region column mapping
  id    = db.Column(db.Integer, primary_key=True)
  name  = db.Column(db.Text)
