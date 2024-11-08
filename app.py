"""
This is the main application module for the blog application.
It defines the routes and handles user interactions with the blog posts.

Flask application serves HTML templates and processes requests
to view, add, update, delete, and like blog posts.
"""

from flask import Flask, render_template, request, redirect, abort
from blog_manager import BlogManager  # Import BlogManager class
from data import PATH

app = Flask(__name__)

blog_manager = BlogManager(PATH)


@app.route('/like/<int:post_id>')
def add_like(post_id):
    """
    Increments the like count for a specific blog post.

    Args:
        post_id (int): The ID of the post to like.

    Returns:
        Response: A redirect to the home page with the updated list of posts.

    Raises:
        404: If the post with the specified ID is not found.
    """
    post = blog_manager.get_post_by_id(post_id)
    if post is None:
        abort(404, description=f"Post with ID [{post_id}] not found.")
    post['likes'] = post.get('likes', 0) + 1
    blog_manager.save_posts()
    return redirect('/')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Deletes a blog post by its ID.

    Args:
        post_id (int): The ID of the post to delete.

    Returns:
        Response: Redirects to the home page if successful.

    Raises:
        404: If the post with the specified ID does not exist.
    """
    post = blog_manager.get_post_by_id(post_id)
    if post:
        blog_manager.delete_post(post)
        return redirect('/')
    abort(404, description=f"Error: Post with ID [{post_id}] does not exist.")


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Updates an existing blog post with new information.

    Args:
        post_id (int): The ID of the post to update.

    Returns:
        Response:
            - If POST: Redirects to the home page after updating the post.
            - If GET: Renders the update post form with the post details.

    Raises:
        404: If the post with the specified ID does not exist.
    """
    post = blog_manager.get_post_by_id(post_id)
    if post is None:
        abort(404, description=f"Error: Post with ID [{post_id}] does not exist.")
    if request.method == 'POST':
        data = {
            'author': request.form.get('author', post['author']),
            'title': request.form.get('title', post['title']),
            'content': request.form.get('content', post['content']),
        }
        blog_manager.update_post(post, data)
        return redirect('/')
    return render_template('update.html', post=post)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Adds a new blog post to the collection.

    Returns:
        Response:
            - If POST: Redirects to the home page after adding the post.
            - If GET: Renders the add post form.

    Raises:
        400: If required fields are missing in the POST request.
    """
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        if not all([author, title, content]):
            return "Error: All fields are required!", 400
        post_id = (blog_manager.blog_posts[-1]['id'] + 1) if blog_manager.blog_posts else 1
        post = {'id': post_id, 'author': author, 'title': title, 'content': content}
        blog_manager.add_post(post)
        return redirect('/')
    return render_template("add.html")


@app.route('/')
def index():
    """
    Renders the home page with a list of blog posts.

    Returns:
        Response: Renders the index page with the blog posts.
    """
    return render_template('index.html', posts=blog_manager.blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
