"""
BlogManager Module

This module defines the BlogManager class, responsible for managing blog posts,
including loading, saving, adding, updating, deleting, and retrieving posts.
"""

import json


class BlogManager:
    """
    A class to manage blog posts, including loading, saving, adding, updating,
    and retrieving posts from a JSON file.
    """

    def __init__(self, path: str):
        """
        Initializes the BlogManager with a path to the JSON file and loads posts.

        Args:
            path (str): The file path to the JSON file containing blog posts.
        """
        self.path = path
        self.blog_posts = []
        self.load_posts()

    def load_posts(self) -> None:
        """
        Loads blog posts from the JSON file.

        If the file does not exist or contains invalid JSON, an empty list is loaded.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.blog_posts = sorted(json.load(file), key=lambda x: x['id'])
        except json.JSONDecodeError:
            print("Error: The JSON file could not be decoded. Please check the file format.")
            self.blog_posts = []
        except FileNotFoundError:
            print(f"Error: File '{self.path}' not found. Returning empty list.")
            self.blog_posts = []

    def get_post_by_id(self, post_id: int) -> dict | None:
        """
        Retrieves a post by its ID.

        Args:
            post_id (int): The ID of the post to retrieve.

        Returns:
            dict | None: The post data if found, otherwise None.
        """
        return next((post for post in self.blog_posts if post['id'] == post_id), None)

    def save_posts(self) -> None:
        """
        Saves the current list of blog posts to the JSON file.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(self.blog_posts, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error: Unable to write to the file '{self.path}'. Details: {e}")

    def add_post(self, post: dict) -> None:
        """
        Adds a new post to the blog posts list.

        Args:
            post (dict): A dictionary containing the post data.
        """
        self.blog_posts.append(post)
        self.save_posts()

    def update_post(self, post: dict, data: dict) -> None:
        """
        Updates an existing post with new data.

        Args:
            post (dict): The post to update.
            data (dict): The new data to update in the post.
        """
        post.update(data)
        self.save_posts()

    def delete_post(self, post: dict) -> None:
        """
        Deletes a post from the blog posts list.

        Args:
            post (dict): The post to delete.
        """
        self.blog_posts.remove(post)
        self.save_posts()
