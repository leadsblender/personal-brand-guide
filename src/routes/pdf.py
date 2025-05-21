from flask import Blueprint, jsonify

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/generate-pdf/<int:guide_id>')
def generate_pdf(guide_id):
    """Temporary disabled PDF generation."""
    return jsonify({
        'success': False,
        'error': 'PDF generation temporarily disabled'
    }), 501