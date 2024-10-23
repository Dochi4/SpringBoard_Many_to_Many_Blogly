"""Blogly application."""

from flask import Flask, request, render_template, redirect 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "blogly_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

with app.app_context():
    db.create_all()

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Redirects to user list."""
    return redirect("/users")

@app.route("/users")
def list_page():
    """Shows list of users from the database."""
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/users/new")
def add_page():
    """Show new user form."""
    return render_template("add_user.html") 

@app.route("/users/new", methods=['POST'])
def add_new():
    """Adds new user to the database."""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>')
def detail_user(user_id):
    """Show detail + posts of a user."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template("details.html", user=user,posts=posts)

@app.route('/users/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/edit')
def user_update_page(user_id):
    """Show the form to update a user."""
    user = User.query.get_or_404(user_id)
    return render_template("update.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    """Update a user."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/new')
def add_post_page(user_id):
    """Show new post form."""
    user = User.query.get_or_404(user_id)
    tags= Tag.query.all()

    return render_template("add_post.html", user=user , tags=tags)

@app.route("/users/<int:user_id>/posts/new", methods=['POST'])
def add_post(user_id):
    """Adds post to a page ."""
    user = User.query.get_or_404(user_id)
    title = request.form.get("title")
    content = request.form.get("content")
    selected_tags = request.form.getlist("tags")

    new_post = Post(title=title, content=content, user_id=user.id)  

    db.session.add(new_post)

    for tag_id in selected_tags:
        tag = Tag.query.get(tag_id)
        new_post.tags.append(tag)

    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route('/users/<int:user_id>/posts/<int:post_id>')
def detail_post(user_id,post_id):
    """Show Details of a POst ."""
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template("detail_post.html", user=user,post=post)

@app.route('/users/<int:user_id>/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(user_id, post_id):
    """Delete a Post"""
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route('/users/<int:user_id>/posts/<int:post_id>/edit')
def post_update_page(user_id,post_id):
    """Show the form to update a post."""
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    tags= Tag.query.all()
    return render_template("update_post.html", user=user,post=post, tags=tags)

@app.route('/users/<int:user_id>/posts/<int:post_id>/edit', methods=['POST'])
def update_post(user_id, post_id):
    """Update a post."""
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    post.title = request.form.get("title")
    post.content = request.form.get("content")
    selected_tags = request.form.getlist("tags")

    post.tags.clear()

    for tag_id in selected_tags:
        tag = Tag.query.get(tag_id)
        if tag:
            post.tags.append(tag)
    
    db.session.commit()

    return redirect(f"/users/{user_id}/posts/{post_id}")

@app.route("/tags")
def list_tags():
    """Shows list of Tags from the database."""
    tags = Tag.query.all()
    return render_template("list_tag.html", tags=tags)

@app.route('/tags/<int:tag_id>')
def detail_tag(tag_id):
    """Show details of a tag and its associated posts."""
    tag = Tag.query.get_or_404(tag_id)
    return render_template("detail_tag.html", tag=tag)

@app.route("/tags/new")
def add_tags_page():
    """New Tags page."""
    tags = Tag.query.all()
    return render_template("add_tag.html", tags=tags)

@app.route("/tags/new", methods=['POST'])
def add_tags():
    """Adds tage to a page ."""
    name = request.form.get("name")

    new_tag = Tag(name = name )  

    db.session.add(new_tag)
    db.session.commit()

    return redirect(f"/tags")

@app.route('/tags/<int:tag_id>/edit')
def user_tag_page(tag_id):
    """Show the form to update a user."""
    tags= Tag.query.get_or_404(tag_id)
    return render_template("update_tag.html", tags=tags)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def update_tag(tag_id):
    """Update a user."""
    tags= Tag.query.get_or_404(tag_id)
    tags.name = request.form["name"]
    
    db.session.commit()

    return redirect(f"/tags/{tag_id}")

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    """Delete a tags."""
    tags= Tag.query.get_or_404(tag_id)
    db.session.delete(tags)
    db.session.commit()

    return redirect("/tags")