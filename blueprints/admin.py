from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from models import Admin, Product, CarouselImage, SiteSettings, Page
from app import db, app
import os
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session['admin_logged_in'] = True
            session['admin_id'] = admin.id
            flash('Successfully logged in!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('admin/login.html')

@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_id', None)
    flash('Successfully logged out!', 'info')
    return redirect(url_for('admin.login'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    products_count = Product.query.filter_by(is_active=True).count()
    carousel_count = CarouselImage.query.filter_by(is_active=True).count()
    return render_template('admin/dashboard.html', 
                         products_count=products_count,
                         carousel_count=carousel_count)

@admin_bp.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        category = request.form['category']
        image_url = request.form['image_url']
        
        product = Product()
        product.name = name
        product.description = description
        product.price = price
        product.category = category
        product.image_url = image_url
        
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.products'))
    
    return render_template('admin/products.html')

@admin_bp.route('/products/edit/<int:product_id>', methods=['POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    product.name = request.form['name']
    product.description = request.form['description']
    product.price = float(request.form['price'])
    product.category = request.form['category']
    product.image_url = request.form['image_url']
    
    db.session.commit()
    flash('Product updated successfully!', 'success')
    return redirect(url_for('admin.products'))

@admin_bp.route('/products/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin.products'))

@admin_bp.route('/carousel')
@login_required
def carousel():
    images = CarouselImage.query.order_by(CarouselImage.order).all()
    return render_template('admin/carousel.html', images=images)

@admin_bp.route('/carousel/add', methods=['POST'])
@login_required
def add_carousel_image():
    title = request.form['title']
    image_url = request.form['image_url']
    order = int(request.form.get('order', 0))
    
    image = CarouselImage()
    image.title = title
    image.image_url = image_url
    image.order = order
    
    db.session.add(image)
    db.session.commit()
    flash('Carousel image added successfully!', 'success')
    return redirect(url_for('admin.carousel'))

@admin_bp.route('/carousel/delete/<int:image_id>', methods=['POST'])
@login_required
def delete_carousel_image(image_id):
    image = CarouselImage.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    flash('Carousel image deleted successfully!', 'success')
    return redirect(url_for('admin.carousel'))

@admin_bp.route('/settings')
@login_required
def settings():
    whatsapp_number = SiteSettings.query.filter_by(key='whatsapp_number').first()
    site_description = SiteSettings.query.filter_by(key='site_description').first()
    footer_content = SiteSettings.query.filter_by(key='footer_content').first()
    company_section_title = SiteSettings.query.filter_by(key='company_section_title').first()
    company_description = SiteSettings.query.filter_by(key='company_description').first()
    contact_address = SiteSettings.query.filter_by(key='contact_address').first()
    contact_phone = SiteSettings.query.filter_by(key='contact_phone').first()
    contact_email = SiteSettings.query.filter_by(key='contact_email').first()
    
    pages = Page.query.all()
    
    return render_template('admin/settings.html',
                         whatsapp_number=whatsapp_number,
                         site_description=site_description,
                         footer_content=footer_content,
                         company_section_title=company_section_title,
                         company_description=company_description,
                         contact_address=contact_address,
                         contact_phone=contact_phone,
                         contact_email=contact_email,
                         pages=pages)

@admin_bp.route('/settings/update', methods=['POST'])
@login_required
def update_settings():
    settings_data = [
        ('whatsapp_number', request.form.get('whatsapp_number', '')),
        ('site_description', request.form.get('site_description', '')),
        ('footer_content', request.form.get('footer_content', '')),
        ('company_section_title', request.form.get('company_section_title', '')),
        ('company_description', request.form.get('company_description', '')),
        ('contact_address', request.form.get('contact_address', '')),
        ('contact_phone', request.form.get('contact_phone', '')),
        ('contact_email', request.form.get('contact_email', ''))
    ]
    
    for key, value in settings_data:
        setting = SiteSettings.query.filter_by(key=key).first()
        if setting:
            setting.value = value
            setting.updated_at = datetime.utcnow()
        else:
            new_setting = SiteSettings()
            new_setting.key = key
            new_setting.value = value
            db.session.add(new_setting)
    
    db.session.commit()
    flash('Settings updated successfully!', 'success')
    return redirect(url_for('admin.settings'))

@admin_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    
    admin = Admin.query.get(session.get('admin_id'))
    
    if not admin or not admin.check_password(current_password):
        flash('Current password is incorrect!', 'error')
        return redirect(url_for('admin.settings'))
    
    if new_password != confirm_password:
        flash('New passwords do not match!', 'error')
        return redirect(url_for('admin.settings'))
    
    admin.set_password(new_password)
    db.session.commit()
    flash('Password changed successfully!', 'success')
    return redirect(url_for('admin.settings'))

@admin_bp.route('/pages/update/<page_name>', methods=['POST'])
@login_required
def update_page(page_name):
    title = request.form['title']
    content = request.form['content']
    
    page = Page.query.filter_by(name=page_name).first()
    if page:
        page.title = title
        page.content = content
        page.updated_at = datetime.utcnow()
    else:
        page = Page()
        page.name = page_name
        page.title = title
        page.content = content
        db.session.add(page)
    
    db.session.commit()
    flash(f'{page_name.title()} page updated successfully!', 'success')
    return redirect(url_for('admin.settings'))
