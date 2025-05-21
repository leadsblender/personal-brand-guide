import os
from flask import send_from_directory, current_app

def serve_static(path):
    """Serve static files."""
    if path != "" and os.path.exists(os.path.join(current_app.static_folder, path)):
        return send_from_directory(current_app.static_folder, path)
    return current_app.send_static_file('index.html')