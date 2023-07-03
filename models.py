from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	username = db.Column(db.String(60), nullable=False)
	firstName = db.Column(db.String(60), nullable=False)
	lastName = db.Column(db.String(60), nullable=False)
	type = db.Column(db.String(20), nullable=False, default='Member')
	registeredon = db.Column(db.DateTime, nullable=False)
	confirmedemail = db.Column(db.Boolean, nullable=True, default=False)
	listings = db.relationship('Listing', backref='owner', lazy=True)
	deliveryDetails = db.relationship('DeliveryDetails', backref='buyer', lazy=True)
	sentItems = db.relationship('SentItems', backref='sentItems', lazy=True)
	photolink = db.Column(db.String(500), nullable=True)
	region = db.Column(db.String(50), nullable=True)
	city = db.Column(db.String(50), nullable=True)
	description = db.Column(db.String(500), nullable=True)
	birth_year = db.Column(db.Integer, nullable=True)
	phone = db.Column(db.String(20), nullable=True)

	def hash_password(self):
		self.password = generate_password_hash(self.password).decode('utf8')

	def check_password_hash(self, password):
		return check_password_hash(self.password, password)


class Listing(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), nullable=False)
	description = db.Column(db.String(5000), nullable=False)
	isWomens = db.Column(db.Boolean, nullable=False)
	size = db.Column(db.String(5), nullable=False)
	category = db.Column(db.String(50), nullable=False)
	isActive = db.Column(db.Boolean, nullable=False)
	color = db.Column(db.String(120), nullable=False)
	price = db.Column(db.Float, nullable=False)
	original_price = db.Column(db.Float, nullable=True)
	offer_price = db.Column(db.Float, nullable=True)
	condition = db.Column(db.String(120), nullable=False)
	status = db.Column(db.String(20), nullable=True, default='new')
	deliveryDetailsId = db.relationship('DeliveryDetails', backref='listing', lazy=False)
	photos = db.relationship('Photo', backref='photo', lazy=True,cascade='all, delete')
	seller = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	created_on = db.Column(db.DateTime, nullable=True)
	bought_on = db.Column(db.DateTime, nullable=True)
	sent_on = db.Column(db.DateTime, nullable=True)
	deleted = db.Column(db.Boolean, nullable=True)
	deleted_reason = db.Column(db.String, nullable=True)
	style = db.Column(db.String(100), nullable=True)
	newColors = db.Column(ARRAY(db.String), nullable=True, default=[])
	newStyles = db.Column(ARRAY(db.String), nullable=True, default=[])