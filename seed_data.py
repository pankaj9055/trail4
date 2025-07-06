from models import Admin, Product, CarouselImage, SiteSettings, Page
from app import db
import os

def seed_initial_data():
    """Seed the database with initial data if it doesn't exist"""
    
    # Check if admin user already exists
    if Admin.query.first() is None:
        # Create default admin user
        admin = Admin(username='admin')
        admin.set_password('admin123')  # Change this in production
        db.session.add(admin)
        print("Created default admin user (username: admin, password: admin123)")
    
    # Check if products exist
    if Product.query.first() is None:
        # Living Room Furniture
        living_room_products = [
            {
                'name': 'Modern Sectional Sofa',
                'description': 'Elegant sectional sofa with premium fabric upholstery. Perfect for modern living rooms with comfortable seating for the whole family.',
                'price': 1299.99,
                'category': 'living room',
                'image_url': 'https://pixabay.com/get/g872ff4eb85e85f20610176226c64d521fe456dbbc97c633443f88c24643c13e80e69a066ace53e6899ecbbe8d8806c6d61486f6faf8a03a09094f95e2c47808a_1280.jpg'
            },
            {
                'name': 'Minimalist Coffee Table',
                'description': 'Sleek glass-top coffee table with wooden legs. Adds a contemporary touch to any living space.',
                'price': 399.99,
                'category': 'living room',
                'image_url': 'https://pixabay.com/get/g5a1784c0e30763709a009dd43213d68492a483cc3a733f464251abfdcd3b1be439304e57b765563c7d207d35ba84a8f1a3a97ae6a4245c6297a3603b764cced0_1280.jpg'
            },
            {
                'name': 'Luxury Armchair Set',
                'description': 'Set of two premium armchairs with velvet upholstery. Comfortable and stylish addition to any living room.',
                'price': 899.99,
                'category': 'living room',
                'image_url': 'https://pixabay.com/get/ga1979ad66b9183fae4ce17e2095c9a93fd3163bcc9aed33a3db595068bf8873ae0cc5a328689f3b2a4e9c0d9557690cf9ba84be84475b1659061dabdbeaca34f_1280.jpg'
            },
            {
                'name': 'Contemporary TV Stand',
                'description': 'Modern TV stand with storage compartments. Clean lines and functional design for modern living rooms.',
                'price': 549.99,
                'category': 'living room',
                'image_url': 'https://pixabay.com/get/gbe5bcd68bd8fccd6cdc8bbb23452af0fe719d2b6bbfac73704bff8c239321f21e1a7ae11673b32c8a10c0c252492713904f175ca5b049d0c28adc81e0c305aef_1280.jpg'
            }
        ]
        
        # Bedroom Furniture
        bedroom_products = [
            {
                'name': 'Luxury Platform Bed',
                'description': 'King-size platform bed with upholstered headboard. Crafted from premium materials for ultimate comfort.',
                'price': 1599.99,
                'category': 'bedroom',
                'image_url': 'https://pixabay.com/get/gcdf84c2cc8472d941a2b0f494c53af870a4f71e281e5d0ec43cf029c1c16900920cbdbece56f50b7f42919966f754c3d85aff827fa12c2c687c65d74851ff6ca_1280.jpg'
            },
            {
                'name': 'Modern Dresser',
                'description': 'Six-drawer dresser with sleek design. Ample storage space with soft-close drawers and premium hardware.',
                'price': 799.99,
                'category': 'bedroom',
                'image_url': 'https://pixabay.com/get/g4ed57ecdb3f7d0783b2ebfbbc0891931d3e09ccce3570560a9642a7e5aacb769c6429a388d9ff5ac37c92294d626f49c56139c4cfda2094d1af65c900d7c0cbe_1280.jpg'
            },
            {
                'name': 'Elegant Nightstand Set',
                'description': 'Set of two matching nightstands with built-in USB charging ports. Perfect complement to any bedroom.',
                'price': 449.99,
                'category': 'bedroom',
                'image_url': 'https://pixabay.com/get/g7b3dd4b86c0a4f410991cc746b7c60c8b158a3fe39b34c0dbc12258db6954153d75438ce36f70f5f6830443d90016a86fbb8269aa363c72d248e2ec4bd5e9bf7_1280.jpg'
            },
            {
                'name': 'Designer Wardrobe',
                'description': 'Spacious wardrobe with mirror doors and LED lighting. Organized storage for all your clothing needs.',
                'price': 1299.99,
                'category': 'bedroom',
                'image_url': 'https://pixabay.com/get/g9e3c785bf0311fc468f54f80c5c4ae448adc4751488795c623f64beac7cec646efd3fd40771defb9889c8e84ef50f1334f63836d2f643e0131129ed83d6cfe90_1280.jpg'
            }
        ]
        
        # Office Furniture
        office_products = [
            {
                'name': 'Executive Desk',
                'description': 'Large executive desk with built-in storage and cable management. Perfect for home offices and professional spaces.',
                'price': 899.99,
                'category': 'office',
                'image_url': 'https://pixabay.com/get/g2545d7fb966a2100c8a367db1dbe4d4c51a967eab0458fc0c21f22d1cc178a1a008000807e621037d8d52f33ef9d2004fac385056bf66fc72ba9a024e40f834a_1280.jpg'
            },
            {
                'name': 'Ergonomic Office Chair',
                'description': 'Premium ergonomic chair with lumbar support and adjustable height. Designed for long hours of comfortable work.',
                'price': 599.99,
                'category': 'office',
                'image_url': 'https://pixabay.com/get/g44c9437353597cd73645cc03cac6a45ee9d877a89efa14c0b32652c11b76b4d22c508431f887458c3b6a98fc80f38a3190ca9ce3855ad96c2433eb225f36df3f_1280.jpg'
            },
            {
                'name': 'Modern Bookshelf',
                'description': 'Five-tier bookshelf with contemporary design. Ideal for organizing books, decorative items, and office supplies.',
                'price': 349.99,
                'category': 'office',
                'image_url': 'https://pixabay.com/get/g9e222e04d0f3cde3dd1acfbec61f2b36b82433da0664b2c3dd6f4623c1e42b86043b1a9bb0d200ed4aa33fa7fd747493c918bf07e105021d50b36f60683f27ab_1280.jpg'
            },
            {
                'name': 'Storage Cabinet',
                'description': 'Lockable storage cabinet with multiple compartments. Secure storage solution for important documents and supplies.',
                'price': 429.99,
                'category': 'office',
                'image_url': 'https://pixabay.com/get/gd2314d65aebf83bbe4a940c951ea63c9b7352fd618b39584ef4d550bc2859ea575ccb31962366eb0e2fadd45ac046622c56e1f7201b5a62474959179768c04d6_1280.jpg'
            }
        ]
        
        # Add all products to database
        all_products = living_room_products + bedroom_products + office_products
        
        for product_data in all_products:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                category=product_data['category'],
                image_url=product_data['image_url']
            )
            db.session.add(product)
        
        print(f"Created {len(all_products)} sample products")
    
    # Check if carousel images exist
    if CarouselImage.query.first() is None:
        carousel_images = [
            {
                'title': 'Modern Living Room Collection',
                'image_url': 'https://pixabay.com/get/ge9d75ee4a5e59f977239abffefaae826b61897437f0204f6da19ce073a6deffe80d0fe23e3018bcdf422d6d725bd8da8c11b025298b3965e66c8b233ac062253_1280.jpg',
                'order': 1
            },
            {
                'title': 'Luxury Bedroom Furniture',
                'image_url': 'https://pixabay.com/get/g75ca47c09ed1dae9db9f4e9baf11f8b29d4b64d22ed78033eb1cc5632cd0ac8731cc06ddc2d28e0ec5089bd07564dbf4faf8b56875f76840a262ab211b9cc344_1280.jpg',
                'order': 2
            },
            {
                'title': 'Contemporary Office Spaces',
                'image_url': 'https://pixabay.com/get/gd2314d65aebf83bbe4a940c951ea63c9b7352fd618b39584ef4d550bc2859ea575ccb31962366eb0e2fadd45ac046622c56e1f7201b5a62474959179768c04d6_1280.jpg',
                'order': 3
            },
            {
                'title': 'Furniture Showroom Experience',
                'image_url': 'https://pixabay.com/get/gc7493a97764054a283b8367f68a38d973956f3c32d712776ac2316bc2680f559edf887677517e5ce7a624a2a382ed0401cbe041cd4fe07841b54e444b3a96b44_1280.jpg',
                'order': 4
            },
            {
                'title': 'Designer Home Interiors',
                'image_url': 'https://pixabay.com/get/ga14688667205850bd08ced127d2af668fffe359f796bc3f8ad91fdfb6a0624a34385e739f88ef9642fe34b9ebabdf77d5baac287f4429bd5c1ca502e8f9fc61d_1280.jpg',
                'order': 5
            },
            {
                'title': 'Premium Furniture Collection',
                'image_url': 'https://pixabay.com/get/gb296967feea890fa195ab509ee41ff0e2d0174696f697c39e518087a5bd0e74603bbb5bda7003ac5386522fee9cec8f632a4ef4da748374902c649e4e9abb9b4_1280.jpg',
                'order': 6
            }
        ]
        
        for image_data in carousel_images:
            carousel_image = CarouselImage(
                title=image_data['title'],
                image_url=image_data['image_url'],
                order=image_data['order']
            )
            db.session.add(carousel_image)
        
        print(f"Created {len(carousel_images)} carousel images")
    
    # Check if site settings exist
    if SiteSettings.query.first() is None:
        settings = [
            {
                'key': 'whatsapp_number',
                'value': '+1234567890'
            },
            {
                'key': 'site_description',
                'value': '''
                <p class="mb-4">At FurniLux, we believe that your home should be a reflection of your unique style and personality. Our carefully curated collection of premium furniture combines exceptional craftsmanship with contemporary design to create pieces that are both beautiful and functional.</p>
                
                <p class="mb-4">From luxurious living room sets to elegant bedroom furniture, we offer a wide range of high-quality pieces that will transform your space into the home of your dreams. Each item in our collection is selected for its superior quality, durability, and timeless appeal.</p>
                
                <p class="mb-4">Our commitment to excellence extends beyond our products to our customer service. We work closely with each client to understand their needs and help them find the perfect furniture solutions for their home or office.</p>
                
                <p>Experience the FurniLux difference today and discover why thousands of customers trust us with their furniture needs.</p>
                '''
            },
            {
                'key': 'footer_content',
                'value': 'Premium furniture for your dream home. Quality craftsmanship meets modern design. Transform your space with FurniLux - where style meets comfort.'
            },
            {
                'key': 'company_section_title',
                'value': 'Experience FurniLux Excellence'
            },
            {
                'key': 'contact_address',
                'value': '123 Furniture Street, City, State 12345'
            },
            {
                'key': 'contact_phone',
                'value': '+1 (555) 123-4567'
            },
            {
                'key': 'contact_email',
                'value': 'info@furnilux.com'
            },
            {
                'key': 'company_description',
                'value': 'At FurniLux, we understand that furniture is more than just functional pieces – it\'s an investment in your lifestyle and comfort. Our commitment to excellence spans over a decade, during which we\'ve perfected the art of combining traditional craftsmanship with modern design principles. Every piece in our collection undergoes rigorous quality checks and is crafted using sustainable materials sourced from trusted suppliers worldwide. Our dedicated team of interior designers works closely with clients to create personalized spaces that reflect individual style preferences. From initial consultation to final installation, we ensure seamless service delivery with attention to every detail. Our state-of-the-art showroom features the latest furniture trends, allowing customers to experience the quality and comfort firsthand before making their purchase decision.'
            }
        ]
        
        for setting_data in settings:
            setting = SiteSettings(
                key=setting_data['key'],
                value=setting_data['value']
            )
            db.session.add(setting)
        
        print("Created default site settings")
    
    # Check if page content exists
    if Page.query.first() is None:
        pages = [
            {
                'name': 'services',
                'title': 'Our Premium Services',
                'content': '''
                <div class="space-y-6">
                    <p class="text-lg">At FurniLux, we go beyond just selling furniture. We provide comprehensive services to ensure your complete satisfaction from consultation to installation.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h3 class="text-xl font-bold mb-3">Interior Design Consultation</h3>
                            <p>Our expert designers work with you to create the perfect space that reflects your style and meets your functional needs. We provide personalized recommendations and design solutions.</p>
                        </div>
                        
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h3 class="text-xl font-bold mb-3">Custom Furniture Design</h3>
                            <p>Can't find exactly what you're looking for? Our skilled craftsmen can create custom furniture pieces tailored to your specific requirements and space constraints.</p>
                        </div>
                        
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h3 class="text-xl font-bold mb-3">Professional Installation</h3>
                            <p>Our trained installation team ensures that your furniture is properly set up and positioned for optimal functionality and aesthetic appeal.</p>
                        </div>
                        
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h3 class="text-xl font-bold mb-3">Maintenance & Care</h3>
                            <p>We provide ongoing support and maintenance services to keep your furniture looking beautiful and functioning perfectly for years to come.</p>
                        </div>
                    </div>
                    
                    <div class="bg-blue-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold mb-3">Why Choose Our Services?</h3>
                        <ul class="list-disc list-inside space-y-2">
                            <li>Over 10 years of experience in furniture design and installation</li>
                            <li>Certified professionals with attention to detail</li>
                            <li>Warranty on all installation work</li>
                            <li>Flexible scheduling to fit your convenience</li>
                            <li>Comprehensive after-sales support</li>
                        </ul>
                    </div>
                </div>
                '''
            },
            {
                'name': 'about',
                'title': 'About FurniLux',
                'content': '''
                <div class="space-y-6">
                    <p class="text-lg">Founded in 2010, FurniLux has been at the forefront of the furniture industry, bringing premium quality furniture to homes and offices worldwide. Our journey began with a simple mission: to make beautiful, high-quality furniture accessible to everyone.</p>
                    
                    <div class="bg-gray-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold mb-3">Our Story</h3>
                        <p>What started as a small family business has grown into a trusted name in the furniture industry. We've remained committed to our founding principles of quality, craftsmanship, and customer satisfaction. Every piece in our collection is carefully selected and crafted by skilled artisans who share our passion for excellence.</p>
                    </div>
                    
                    <div class="bg-gray-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold mb-3">Our Mission</h3>
                        <p>To transform living and working spaces with furniture that combines exceptional quality, timeless design, and affordable pricing. We believe that everyone deserves to live and work in beautiful, comfortable environments.</p>
                    </div>
                    
                    <div class="bg-gray-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold mb-3">Our Values</h3>
                        <ul class="list-disc list-inside space-y-2">
                            <li><strong>Quality:</strong> We never compromise on the quality of our furniture</li>
                            <li><strong>Customer Focus:</strong> Your satisfaction is our top priority</li>
                            <li><strong>Innovation:</strong> We continuously seek new designs and technologies</li>
                            <li><strong>Sustainability:</strong> We're committed to environmentally responsible practices</li>
                            <li><strong>Integrity:</strong> We conduct business with honesty and transparency</li>
                        </ul>
                    </div>
                    
                    <div class="bg-blue-50 p-6 rounded-lg">
                        <h3 class="text-xl font-bold mb-3">Why Customers Choose FurniLux</h3>
                        <div class="grid md:grid-cols-2 gap-4">
                            <div>
                                <h4 class="font-semibold">10+ Years Experience</h4>
                                <p class="text-sm">Decade of expertise in furniture design and manufacturing</p>
                            </div>
                            <div>
                                <h4 class="font-semibold">10,000+ Happy Customers</h4>
                                <p class="text-sm">Satisfied customers across the country trust our quality</p>
                            </div>
                            <div>
                                <h4 class="font-semibold">Premium Materials</h4>
                                <p class="text-sm">Only the finest materials are used in our furniture</p>
                            </div>
                            <div>
                                <h4 class="font-semibold">Nationwide Delivery</h4>
                                <p class="text-sm">Fast and secure delivery to your doorstep</p>
                            </div>
                        </div>
                    </div>
                </div>
                '''
            }
        ]
        
        for page_data in pages:
            page = Page(
                name=page_data['name'],
                title=page_data['title'],
                content=page_data['content']
            )
            db.session.add(page)
        
        print(f"Created {len(pages)} default pages")
    
    # Commit all changes
    try:
        db.session.commit()
        print("Successfully seeded database with initial data")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")
