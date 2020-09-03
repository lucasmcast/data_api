import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app
from app.models import Account, Extract, LastTransaction, Profile, db

app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.app_context().push()

app.config

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Account=Account, Extract=Extract, LastTransaction=LastTransaction,Profile=Profile)
