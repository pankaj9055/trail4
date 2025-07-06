# FurniLux - Premium Furniture Website

## Overview

FurniLux is a premium furniture e-commerce website built with Flask, featuring a modern responsive design and comprehensive admin management system. The application serves as a showcase for furniture products with an integrated WhatsApp booking system and a complete content management backend.

## System Architecture

### Frontend Architecture
- **Framework**: Template-based rendering with Jinja2
- **Styling**: Tailwind CSS for responsive design and modern UI components
- **Typography**: Google Fonts (Inter + Playfair Display) for professional appearance
- **Icons**: Font Awesome for consistent iconography
- **JavaScript**: Vanilla JS for interactive components (carousel, mobile menu)
- **Responsive Design**: Mobile-first approach with breakpoint-based layouts

### Backend Architecture
- **Framework**: Flask with Blueprint-based modular architecture
- **Database ORM**: SQLAlchemy with Flask-SQLAlchemy integration
- **Authentication**: Session-based admin authentication with password hashing
- **File Handling**: Werkzeug for secure file uploads
- **Security**: CSRF protection, secure session management, and input validation

### Application Structure
```
├── app.py (Main application factory)
├── main.py (Application entry point)
├── models.py (Database models)
├── seed_data.py (Initial data seeding)
├── blueprints/
│   ├── main.py (Public routes)
│   └── admin.py (Admin panel routes)
├── templates/ (Jinja2 templates)
├── static/ (CSS, JS, images)
```

## Key Components

### Database Models
- **Admin**: User authentication for admin panel access
- **Product**: Core furniture product catalog with categories
- **CarouselImage**: Homepage showcase images with ordering
- **SiteSettings**: Dynamic website configuration (WhatsApp, descriptions)
- **Page**: Dynamic content pages (About, Services) with rich text support

### Blueprint Architecture
- **Main Blueprint**: Public-facing routes (/, /products, /about, /services)
- **Admin Blueprint**: Protected admin panel (/admin/*) with authentication

### Core Features
- **Product Catalog**: Categorized furniture display with filtering
- **Image Carousel**: Auto-scrolling homepage showcase
- **WhatsApp Integration**: Direct booking through WhatsApp API
- **Admin Panel**: Complete CRUD operations for content management
- **Content Management**: Dynamic page content and site settings

## Data Flow

### Public User Flow
1. Homepage → Carousel display → Product browsing → WhatsApp booking
2. Category filtering → Product details → Contact via WhatsApp
3. Static pages (About/Services) → Dynamic content rendering

### Admin Flow
1. Login authentication → Dashboard overview → Content management
2. Product management → CRUD operations → Image uploads
3. Site settings → Dynamic content updates → Page management

### Database Operations
- **Read-heavy**: Product catalog, carousel images, site settings
- **Write operations**: Admin content management, settings updates
- **File uploads**: Product images, carousel images via secure handling

## External Dependencies

### Frontend Dependencies
- **Tailwind CSS**: Utility-first CSS framework via CDN
- **Font Awesome**: Icon library via CDN
- **Google Fonts**: Typography (Inter, Playfair Display)

### Backend Dependencies
- **Flask**: Web framework and routing
- **SQLAlchemy**: Database ORM and migrations
- **Werkzeug**: Security utilities and file handling
- **Jinja2**: Template engine (included with Flask)

### Database
- **Primary**: SQLite for development (configurable via DATABASE_URL)
- **Production Ready**: PostgreSQL support through SQLAlchemy URI configuration

### Third-party Integrations
- **WhatsApp Business API**: Direct messaging integration for bookings
- **Image Hosting**: External image URLs for product/carousel images

## Deployment Strategy

### Environment Configuration
- **Development**: SQLite database, debug mode enabled
- **Production**: Environment variables for database, session secrets
- **File Storage**: Local static/uploads directory for admin uploads

### Security Considerations
- **Session Management**: Secure session keys and admin authentication
- **File Uploads**: Restricted file types and size limits (16MB)
- **Database Security**: Parameterized queries through SQLAlchemy
- **CSRF Protection**: Session-based protection for admin forms

### Scalability
- **Database**: Configurable through DATABASE_URL for different environments
- **Static Files**: Served through Flask in development, CDN-ready for production
- **Session Storage**: Memory-based sessions (can be upgraded to Redis)

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 06, 2025. Initial setup
- July 06, 2025. Fixed navigation lines and products disappearing after page refresh
- July 06, 2025. Reduced white space throughout website by optimizing CSS padding and margins
- July 06, 2025. Enhanced JavaScript visibility controls to ensure all elements remain visible
- July 06, 2025. Fixed admin panel authentication system
- July 06, 2025. Improved About page content display and minimized spacing
- July 06, 2025. Fixed database connection issues and font consistency across all templates
- July 06, 2025. Implemented consistent font rendering with Inter for body text and Playfair Display for headings
- July 06, 2025. Updated all admin templates with proper font imports and consistent styling
- July 06, 2025. Enhanced CSS animations to prevent font display issues under images
- July 06, 2025. Resolved text overlapping issues throughout the website by removing conflicting z-index and positioning
- July 06, 2025. Fixed hero section text overlapping in Transform Your Space and About FurniLux sections
- July 06, 2025. Standardized line heights and margins for all headings and paragraphs to prevent overlaps
- July 06, 2025. Fixed carousel navigation arrows positioning to stay on image area with proper z-index
- July 06, 2025. Corrected navigation cards icon and arrow positioning for Premium Products, Expert Services, and Our Story sections
- July 06, 2025. Enhanced auto-scroll carousel system with proper indicator positioning
- July 06, 2025. Fixed product card button positioning and visibility issues in photos section
- July 06, 2025. Ensured WhatsApp inquiry buttons are properly positioned and functional on product images
- July 06, 2025. Redesigned carousel with premium styling - larger arrows, enhanced indicators, and backdrop blur effects
- July 06, 2025. Fixed carousel arrows and dots positioning to stay within image area only
- July 06, 2025. Added premium visual effects including shadows, blur, and smooth hover animations
- July 06, 2025. Removed all carousel navigation controls (arrows, dots, auto-scroll button) for minimal design
- July 06, 2025. Created minimal auto-scroll carousel with pause-on-hover functionality only
- July 06, 2025. Removed text overlay from carousel images for cleaner appearance
- July 06, 2025. Added scroll navigation buttons back to carousel for manual control
- July 06, 2025. Set 4-second auto-scroll timing and configured 6 carousel images total
- July 06, 2025. Removed carousel arrows completely for minimal design
- July 06, 2025. Fixed auto-scroll functionality and changed timing to 3 seconds
- July 06, 2025. Ensured all 6 carousel images display properly with smooth transitions
- July 06, 2025. Fixed carousel CSS layout issues with proper flex properties and container sizing
- July 06, 2025. Updated carousel HTML structure with inline styles for consistent display
- July 06, 2025. Resolved carousel track positioning to ensure all images are visible during transitions