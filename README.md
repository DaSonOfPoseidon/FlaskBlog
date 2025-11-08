# Flask Blog Application

A simple blogging application built with Python Flask and SQLite database, featuring full CRUD operations for blog posts.

## Features

- **View Posts**: Display all blog posts on the home page
- **View Individual Post**: Click on any post title to view full details
- **Create Post**: Add new blog posts with title and content
- **Edit Post**: Update existing blog posts
- **Delete Post**: Remove posts with confirmation dialog
- **Form Validation**: Required field validation with flash messages
- **Responsive Design**: Mobile-friendly layout with modern styling

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Environment**: python-dotenv for configuration

## Installation

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/DaSonOfPoseidon/FlaskBlog.git
   cd FlaskBlog
   ```

2. **Install dependencies**
   ```bash
   pip install flask python-dotenv
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and set a secure SECRET_KEY

4. **Initialize the database**
   ```bash
   python init_db.py
   ```
   This creates `database.db` with sample blog posts.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
FlaskBlog/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── schema.sql          # Database schema definition
├── database.db         # SQLite database (created after init)
├── .env                # Environment variables (not in git)
├── .env.example        # Environment template
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── templates/          # HTML templates
    ├── base.html       # Base template with styling
    ├── index.html      # Home page (all posts)
    ├── post.html       # Individual post view
    ├── create.html     # Create new post form
    └── edit.html       # Edit post form
```

## Usage

### Creating a Post
1. Click "New Post" in the navigation
2. Fill in the title and content
3. Click "Submit"
4. You'll be redirected to the home page with a success message

### Editing a Post
1. Click "Edit" on any post (from home page or post detail page)
2. Modify the title and/or content
3. Click "Update Post"
4. You'll be redirected to the home page with a success message

### Deleting a Post
1. Click "Delete" on any post
2. Confirm the deletion in the dialog
3. The post will be removed and you'll see a confirmation message

## Database Schema

The application uses a single `posts` table:

```sql
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
```

## Configuration

Environment variables (in `.env` file):

- `SECRET_KEY`: Flask secret key for sessions and flash messages
- `FLASK_ENV`: Set to `development` for debug mode

## Security Notes

- Never commit the `.env` file to version control
- Change the SECRET_KEY to a random, secure value in production
- The database file (`*.db`) is excluded from git
- This is a development application - use a production WSGI server for deployment

## Development

To modify the application:

1. **Add new routes**: Edit `app.py` and add route decorators
2. **Change database**: Update `schema.sql` and re-run `init_db.py`
3. **Modify styling**: Edit CSS in `templates/base.html`
4. **Add templates**: Create new files in `templates/` directory

## Testing

To test the application:

1. Create a post and verify it appears on the home page
2. Edit the post and verify changes are saved
3. Delete the post and verify it's removed
4. Test form validation by submitting empty fields

## License

This project is for educational purposes as part of the IT4320 course.
