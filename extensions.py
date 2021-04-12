from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from telebot import TeleBot

from config import Config

db = SQLAlchemy()
bot = TeleBot(token=Config.BOT_KEY)
jwt = JWTManager()
