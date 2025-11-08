import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

# Configuration for flash messages - use environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')



# Function to open a connection to the database.db file
def get_db_connection():
    # create connection to the database
    conn = sqlite3.connect('database.db')
    
    # allows us to have name-based access to columns
    # the database connection will return rows we can access like regular Python dictionaries
    conn.row_factory = sqlite3.Row

    #return the connection object
    return conn


# Function to get a post by ID
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


# use the app.route() decorator to create a Flask view function called index()
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


# route to view a single post
@app.route('/<int:id>')
def post(id):
    post = get_post(id)
    return render_template('post.html', post=post)


# route to create a post
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Validation: check if title and content are not empty
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            # Insert the new post into the database
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            flash('Post created successfully!')
            return redirect(url_for('index'))

    return render_template('create.html')


# route to edit a post
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Validation: check if title and content are not empty
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            # Update the post in the database
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            flash('Post updated successfully!')
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


app.run()