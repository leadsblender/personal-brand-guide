"""
Routes package for the Personal Brand Guide application.
"""
from .brand_guide import brand_guide_bp
from .pdf import pdf_bp

__all__ = ['brand_guide_bp', 'pdf_bp']