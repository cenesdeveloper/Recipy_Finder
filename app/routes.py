import pprint

from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models import User
from app.forms import RegisterForm, LoginForm
from app.utils import search_recipes
from app.models import RecipeBookmark
from flask import request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.search'))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.search'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.search'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    query = request.args.get('query', '')
    diet = request.args.get('diet')
    cuisine = request.args.get('cuisine')
    intolerances = request.args.get('intolerances')

    recipes = []
    if query:
        recipes = search_recipes(query, diet, intolerances, cuisine)
        pprint.pprint(recipes)

    return render_template('search.html', recipes=recipes)

@main.route('/bookmarks')
@login_required
def bookmarks():
    saved = RecipeBookmark.query.filter_by(user_id=current_user.id).all()
    return render_template('bookmarks.html', bookmarks=saved)

@main.route('/bookmark/<int:id>/delete', methods=['POST'])
@login_required
def delete_bookmark(id):
    recipe = RecipeBookmark.query.get_or_404(id)
    if recipe.user_id != current_user.id:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Bookmark removed.', 'info')
    return redirect(url_for('main.bookmarks'))

@main.route('/bookmark', methods=['POST'])
@login_required
def bookmark():
    recipe_id = request.form['recipe_id']
    title = request.form['title']
    image_url = request.form['image_url']
    source_url = request.form['source_url']

    # Prevent duplicate bookmarks
    existing = RecipeBookmark.query.filter_by(recipe_id=recipe_id, user_id=current_user.id).first()
    if not existing:
        bookmark = RecipeBookmark(
            recipe_id=recipe_id,
            title=title,
            image_url=image_url,
            source_url=source_url,
            user_id=current_user.id
        )
        db.session.add(bookmark)
        db.session.commit()
        flash('Recipe saved to bookmarks!', 'success')
    else:
        flash('Recipe already bookmarked.', 'info')

    return redirect(url_for('main.search'))
