from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Product, CarouselImage, SiteSettings, Page
from app import db

main_bp = Blueprint('main', __name__)

def get_setting(key, default=''):
    setting = SiteSettings.query.filter_by(key=key).first()
    return setting.value if setting else default

def get_contact_settings():
    """Get all contact settings for footer"""
    return {
        'contact_address': get_setting('contact_address', '123 Furniture Street, City, State 12345'),
        'contact_phone': get_setting('contact_phone', '+1 (555) 123-4567'),
        'contact_email': get_setting('contact_email', 'info@furnilux.com')
    }

def get_page_content(page_name):
    page = Page.query.filter_by(name=page_name).first()
    return page if page else None

@main_bp.route('/')
def index():
    carousel_images = CarouselImage.query.filter_by(is_active=True).order_by(CarouselImage.order).all()
    whatsapp_number = get_setting('whatsapp_number', '+1234567890')
    site_description = get_setting('site_description', 'Welcome to our premium furniture store!')
    
    contact_info = get_contact_settings()
    return render_template('index.html', 
                         carousel_images=carousel_images,
                         whatsapp_number=whatsapp_number,
                         site_description=site_description,
                         get_setting=get_setting,
                         **contact_info)

@main_bp.route('/products')
def products():
    category = request.args.get('category', 'all')
    if category == 'all':
        products = Product.query.filter_by(is_active=True).all()
    else:
        products = Product.query.filter_by(is_active=True, category=category).all()
    
    categories = db.session.query(Product.category).distinct().all()
    categories = [cat[0] for cat in categories]
    whatsapp_number = get_setting('whatsapp_number', '+1234567890')
    
    contact_info = get_contact_settings()
    return render_template('products.html', 
                         products=products, 
                         categories=categories, 
                         current_category=category,
                         whatsapp_number=whatsapp_number,
                         **contact_info)

@main_bp.route('/services')
def services():
    page_content = get_page_content('services')
    whatsapp_number = get_setting('whatsapp_number', '+1234567890')
    contact_info = get_contact_settings()
    return render_template('services.html', page_content=page_content, whatsapp_number=whatsapp_number, **contact_info)

@main_bp.route('/about')
def about():
    page_content = get_page_content('about')
    whatsapp_number = get_setting('whatsapp_number', '+1234567890')
    contact_info = get_contact_settings()
    return render_template('about.html', page_content=page_content, whatsapp_number=whatsapp_number, **contact_info)

@main_bp.route('/admin')
def admin_redirect():
    return redirect(url_for('admin.login'))
