import tempfile
import pytest
from blog_manager import BlogManager


@pytest.fixture
def blog_manager():
    """Fixture to initialize BlogManager with a temporary JSON file."""
    # Create a temporary file for storing blog posts
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        # Initialize the BlogManager with the path of the temporary file
        manager = BlogManager(temp_file.name)
        yield manager


@pytest.fixture
def sample_post():
    """Fixture to provide a sample blog post."""
    return {
        "id": 1,
        "author": "Author1",
        "title": "Title1",
        "content": "Content1",
        "likes": 0
    }


def test_load_posts(blog_manager):
    """Test that BlogManager loads posts from the JSON file correctly."""
    assert blog_manager.blog_posts == []  # Should start empty with no data


def test_add_post(blog_manager, sample_post):
    """Test adding a post to BlogManager."""
    blog_manager.add_post(sample_post)
    assert len(blog_manager.blog_posts) == 1
    assert blog_manager.blog_posts[0]["title"] == "Title1"


def test_get_post_by_id(blog_manager, sample_post):
    """Test retrieving a post by its ID."""
    blog_manager.add_post(sample_post)
    post = blog_manager.get_post_by_id(1)
    assert post is not None
    assert post["id"] == 1
    assert post["title"] == "Title1"


def test_update_post(blog_manager, sample_post):
    """Test updating an existing post."""
    blog_manager.add_post(sample_post)
    post = blog_manager.get_post_by_id(1)
    blog_manager.update_post(post, {"title": "Updated Title"})
    updated_post = blog_manager.get_post_by_id(1)
    assert updated_post["title"] == "Updated Title"


def test_delete_post(blog_manager, sample_post):
    """Test deleting a post."""
    blog_manager.add_post(sample_post)
    post = blog_manager.get_post_by_id(1)
    blog_manager.delete_post(post)
    assert blog_manager.get_post_by_id(1) is None


def test_save_posts(blog_manager, sample_post):
    """Test saving posts to the JSON file."""
    blog_manager.add_post(sample_post)
    # Load posts again to confirm persistence
    blog_manager.load_posts()
    assert len(blog_manager.blog_posts) == 1
    assert blog_manager.blog_posts[0]["title"] == "Title1"


def test_load_invalid_json():
    """Test loading from an invalid JSON file."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        # Write invalid JSON to the file
        temp_file.write("{ invalid json }")
        temp_file.seek(0)
        manager = BlogManager(temp_file.name)
        # The blog_posts should be an empty list due to JSON decoding error
        assert manager.blog_posts == []
