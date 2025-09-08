# BlogMe - Django Blog Platform

A modern, responsive blog platform built with Django and styled with Tailwind CSS. BlogMe provides a clean interface for reading and managing blog posts with features like search, pagination, and a dark/light theme toggle.

## 🚀 Features

- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Dark/Light Theme**: Toggle between dark and light modes with persistent storage
- **Blog Management**: Create, read, update, and delete blog posts
- **Search Functionality**: Real-time search through blog titles
- **Pagination**: Efficient pagination for blog listings
- **Admin Interface**: Django admin panel for content management
- **Latest Topics Sidebar**: Dynamic sidebar showing recent blog posts
- **Clean UI**: Modern, minimalist interface with smooth transitions
- **Markdown Support**: Rich text editing with markdown syntax and live preview

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite (default)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Python**: 3.x
- **Additional Libraries**:
  - asgiref==3.9.1
  - sqlparse==0.5.3
  - tzdata==2025.2
  - markdown==3.5.2

## 📁 Project Structure

```
blogme/
├── blogme/                 # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── core/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/core/    # App-specific templates
│   │   ├── about.html
│   │   ├── blog_detail.html
│   │   ├── explore.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── tests.py          # Test cases
│   ├── urls.py           # App URL patterns
│   └── views.py          # View functions
├── templates/            # Global templates
│   └── layout.html       # Base template
├── .gitignore           # Git ignore file
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.x installed
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/buildwithhusnain/blogme.git
   cd blogme
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📖 Usage

### For Readers

1. **Home Page**: View the latest 6 published blog posts
2. **Explore Page**: Browse all published blogs with pagination (12 per page)
3. **Search**: Use the search functionality to find specific blog posts
4. **Blog Detail**: Click on any blog to read the full content
5. **Theme Toggle**: Switch between dark and light themes
6. **Latest Topics**: Check the sidebar for recently published topics

### For Content Creators

1. **Admin Access**: Log in to the admin panel at `/admin/`
2. **Create Blogs**: Add new blog posts using the markdown editor
3. **Markdown Writing**: Use markdown syntax for rich formatting (headings, lists, code, tables)
4. **Live Preview**: Preview your content in real-time while editing
5. **Manage Content**: Edit, publish/unpublish, or delete existing blogs
6. **Author Assignment**: Blogs are automatically assigned to the logged-in user

## 🔧 Configuration

### Settings

Key configuration options in `blogme/settings.py`:

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain names for production
- **SECRET_KEY**: Change the secret key for production
- **DATABASE**: Configure your preferred database (currently SQLite)

### Static Files

- Static files are served from the `assets/` URL
- Static root is set to `BASE_DIR / 'static'`

## 🎨 Customization

### Styling

The project uses Tailwind CSS with custom configuration:
- Primary color: Black (#000000)
- Secondary color: White (#ffffff)
- Dark mode support with automatic theme persistence

### Templates

- **Base Template**: `templates/layout.html`
- **App Templates**: Located in `core/templates/core/`
- All templates extend the base layout for consistency

## 📊 API Endpoints

The application provides several API endpoints:

- `GET /api/search/?q=<query>`: Search blog posts
- `GET /api/latest-topics/`: Get latest 10 published topics

## 🗄️ Database Schema

### Blog Model

```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Supports Markdown syntax
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def get_markdown_content(self):
        # Renders markdown to HTML with syntax highlighting
        return mark_safe(markdown.markdown(self.content, extensions=['codehilite', 'fenced_code', 'tables']))
```

## 🔒 Security Features

- CSRF protection enabled
- XFrame options middleware
- User authentication for admin access
- Published/unpublished blog control
- Author-based content ownership

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up proper logging
6. Use environment variables for sensitive settings
7. Set up HTTPS

### Environment Variables

Consider using environment variables for:
- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Husnain**
- GitHub: [@buildwithhusnain](https://github.com/buildwithhusnain)

## 🐛 Bug Reports

If you find a bug, please create an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check existing documentation
- Review the code comments

---

**Happy Blogging! 📝✨**