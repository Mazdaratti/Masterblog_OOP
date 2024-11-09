# Masterblog ✨

Masterblog is a simple, Flask-based blog application developed as part of a Software Engineer Bootcamp assignment. It demonstrates using Flask to manage dynamic web content and handle form submissions, allowing users to create, update, delete, and like blog posts.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Project Requirements](#project-requirements)
- [Contributing](#contributing)
- [License](#license)

## Features 🛠

- **Add Blog Post**: Create new blog posts with an author, title, and content.
- **Update Blog Post**: Modify existing blog posts.
- **Delete Blog Post**: Remove posts as needed.
- **Like Button**: Each post has a like button, allowing users to increase the like count.
- **Responsive Layout**: Styled with CSS for a clean, user-friendly interface.

## Installation ⚙

### Prerequisites
- **Python**: Version 3.7 or higher.
- **pip**: For Python package management.

### Setup
1. Clone the repository
   git clone https://github.com/Mazdaratti/Masterblog.git

2. Navigate into the project directory
   cd Masterblog

3. Create a virtual environment (recommended)
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run the Flask application
   http://localhost:5000

## Usage 📖

To run the application:

1. Start the Flask server:

    flask run

    By default, the application is accessible at http://127.0.0.1:5000.

2. Interact with the Blog:

   - Home Page: View all blog posts.
   - New Post: Use the "Add a post" button to create a new blog post.
   - Update Post: Use the "✏️" button to edit the post.
   - Delete: Use the "🗑️" button to delete the post.
   - Like: Click the "👍" button on each post to increase its like count.

## Project Structure 📂
```
Masterblog/
├── data/                    
│   ├── __init__.py             # Package initializer
│   └── blog_posts.json         # Blog data storage
├── static/
│   └── styles.css              # Styles for the application
├── templates/
│   ├── index.html              # Main page showing blog posts
│   ├── add.html                # Form page for adding new posts
│   └── update.html             # Form page for updating posts
├── tests
│   └── test_blog_manager.py    # Pytests
├── app.py                      # Main application file with routes and logic
├── blog_manager.py             # BlogManager class, responsible for managing blog posts
├── requirements.txt            # Dependencies
└── readme.md                   # Project documentation
```
## Technologies Used 💻

- **Flask**: Web framework used to create the server-side logic and handle routing.
- **Jinja2**: Templating engine used to render dynamic content in HTML pages.
- **HTML/CSS**: For designing the user interface.
- **JSON**: Used for storing the blog posts locally.

## Project Requirements 📦

- Python 3.x
- Flask 3.0.3
- Jinja2 3.1.4

## Contributing 🤝

Contributions are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   git checkout -b feature-branch
3. Commit your changes:
   git commit -am 'Add new feature'
4. Push to the branch:
   git push origin feature-branch
5. Create a Pull Request.

## Lisense 📜

---

This revised version adds a table of contents, a more detailed usage section, and a clear project structure outline. It’s designed for easy navigation and user-friendliness for anyone setting up or contributing to the project.
