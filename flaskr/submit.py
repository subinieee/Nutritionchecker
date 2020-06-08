import click
import requests 

from flask import (Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask import jsonify
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('submit', __name__)

def checkrecipe(recipe):
    endpoint="https://api.edamam.com/api/food-database/parser"
    payload={"app_id":"1dbb4707","app_key":"e4c61d76694126307807831e256ba0cf", "ingr":recipe}
    response = requests.get(endpoint, params=payload)
    data=response.json()
    return data

@bp.route("/submit", methods=["POST"])
def submit_food():
    # if request.method == 'POST':
    data = request.form
    recipe_results = checkrecipe(data["recipe"])
    global item
    item = recipe_results['hints'][0]['food']['label']
    global itemtwo
    itemtwo = recipe_results['hints'][0]['food']['nutrients']
    return render_template("submit.html", myItem= item, myItemtwo=itemtwo)


@bp.route("/index")
@login_required
def index():
	db = get_db()
	posts = db.execute(
	'SELECT p.id, created, item, energy, protein, fat, carbs, author_id, username'
	' FROM post p JOIN user u ON p.author_id = u.id'
	' ORDER BY created DESC').fetchall()
	
	return render_template('blog/index.html', posts=posts)

@bp.route("/profile")
@login_required
def save_food():
		energy = itemtwo['ENERC_KCAL']
		protein = itemtwo['PROCNT']
		fat = itemtwo['FAT']
		carbs = itemtwo['CHOCDF']
		db = get_db()
		db.execute(
		'INSERT INTO post (item, energy, protein, fat, carbs, author_id)'
		' VALUES (?, ?, ?, ?, ?, ?)',
		(item, energy, protein, fat, carbs, g.user['id'])
		)
		db.commit()
		return redirect(url_for('submit.index'))
    	

def get_post(id, check_author=True):
    post = get_db().execute(
		'SELECT p.id, item, energy, protein, fat, carbs, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
    
    
    
    
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('submit.index'))




