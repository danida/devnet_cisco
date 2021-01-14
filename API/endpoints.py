from flask import Blueprint
from Services.Meraki import *

endpoints = Blueprint('endpoints', __name__, template_folder='templates')
meraki = Scanning_API()

@endpoints.route('/meraki/location',methods=["POST"])
def location ():
    meraki.get_locationJSON()

