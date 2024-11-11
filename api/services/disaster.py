from flask import Blueprint, jsonify, request
# from db import 
from datetime import datetime
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient, errors

disaster = Blueprint('disaster', 'disaster', url_prefix='/api/v1/disaster')
CORS(disaster)

