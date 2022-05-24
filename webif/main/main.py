#states all pages for website
from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect, request

main = Blueprint('main', __name__)

@main.route('/missionctrl',methods=['GET', 'POST'])
def missionctrl():
	return render_template("main.html")


@main.route('/')
def operations():
	return render_template("operations.html")
