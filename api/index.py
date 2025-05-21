from flask import Flask, request, send_from_directory, render_template
from src import create_app
from .static import serve_static

app = create_app()

# Route voor static files
@app.route('/static/<path:path>')
def static_file(path):
    return serve_static(path)

# Route voor alle andere paden
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('api/'):
        return app.handle_request()
    return render_template('index.html')

# Handler voor Vercel
def handler(request):
    with app.request_context(request):
        return app.handle_request()