from app import app, db
from app.models import Post, User

@app.shell_context_processor
def make_shell_context():
    # RETURN DICTIONARY FROM CONTEXT
    return {
        'db': db,
        'Post': Post,
        'User': User
    }