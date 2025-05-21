from flask import Flask
from src import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

# Voor Vercel serverless functions
def handler(request):
    """Handle requests in a Vercel serverless function."""
    if request.method == 'GET':
        response = app.handle_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
    return {
        'statusCode': 405,
        'body': 'Method not allowed'
    }

# Voor lokale ontwikkeling
if __name__ == '__main__':
    app.run(port=5000)