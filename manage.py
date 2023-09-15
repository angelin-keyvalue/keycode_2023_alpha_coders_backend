import os
from app import create_app
from app.models import db
from app.models.client import Client


app = create_app()

if __name__ == '__main__':
    app.run()


if os.getenv('ENV') == 'development':
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'client': Client}