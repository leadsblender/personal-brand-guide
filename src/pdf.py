from flask import Blueprint, render_template, request, jsonify, make_response, session
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from src.models.brand_guide import BrandGuide
from src.models.user import User
import tempfile
import os
from datetime import datetime

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/generate-pdf/<int:guide_id>')
def generate_pdf(guide_id):
    email = request.args.get('email')
    
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    guide = BrandGuide.query.get(guide_id)
    if not guide or guide.user_id != user.id:
        return jsonify({'success': False, 'message': 'Guide not found or access denied'}), 404
    
    # Get language preference
    lang = guide.language if guide.language else 'nl'
    
    # Generate HTML for PDF
    html_content = render_template(
        'pdf_template.html',
        guide=guide,
        lang=lang,
        date=datetime.now().strftime("%d-%m-%Y")
    )
    
    # Configure fonts
    font_config = FontConfiguration()
    css = CSS(string='''
        @font-face {
            font-family: 'Noto Sans CJK SC';
            src: url(/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc);
        }
        @font-face {
            font-family: 'WenQuanYi Zen Hei';
            src: url(/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc);
        }
        body {
            font-family: 'Noto Sans CJK SC', 'WenQuanYi Zen Hei', sans-serif;
        }
    ''', font_config=font_config)
    
    # Create PDF
    html = HTML(string=html_content)
    pdf_file = html.write_pdf(stylesheets=[css], font_config=font_config)
    
    # Create response
    response = make_response(pdf_file)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=personal_brand_guide_{guide_id}.pdf'
    
    return response
