# Changelog

All notable changes to the BlogMe project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- User authentication and registration system
- Comment system for blog posts
- Categories and tags for better organization
- Rich text editor for blog creation
- Image upload functionality
- Social media sharing buttons
- Email notifications for new posts
- RSS feed support
- Advanced search with filters
- User profiles and author pages

## [1.1.0] - 2024-01-20

### Added
- **Markdown Support**: Full markdown editing and rendering
- **Rich Text Editor**: EasyMDE markdown editor in Django admin
- **Syntax Highlighting**: Code blocks with syntax highlighting
- **Live Preview**: Real-time markdown preview in admin
- **Enhanced Styling**: Comprehensive CSS for markdown elements

## [1.0.0] - 2024-01-20

### Added
- Initial release of BlogMe
- Django 5.2.6 framework implementation
- Responsive design with Tailwind CSS
- Dark/Light theme toggle with persistent storage
- Blog post management through Django admin
- Home page displaying latest 6 blog posts
- Explore page with pagination (12 posts per page)
- Blog detail view for individual posts
- Real-time search functionality through AJAX
- Latest topics sidebar with auto-refresh
- About page for site information
- Clean, modern UI with smooth transitions
- Mobile-first responsive design
- SQLite database for development
- Basic SEO-friendly URL structure

### Technical Features
- Django admin interface for content management
- CSRF protection and security middleware
- Automatic author assignment for blog posts
- Published/unpublished blog control
- Pagination for better performance
- AJAX-powered search with JSON responses
- Auto-updating sidebar content
- Template inheritance for consistent design
- Static file management
- Database migrations system

### API Endpoints
- `GET /api/search/?q=<query>` - Search blog posts
- `GET /api/latest-topics/` - Get latest published topics

### Models
- **Blog Model**
  - Title (CharField, max_length=200)
  - Content (TextField)
  - Author (ForeignKey to User)
  - Created at (DateTimeField, auto_now_add=True)
  - Updated at (DateTimeField, auto_now=True)
  - Is published (BooleanField, default=True)
  - Ordering by creation date (newest first)

### Views
- `index` - Home page with recent blogs
- `explore` - All blogs with pagination
- `about` - About page
- `blog_detail` - Individual blog post view
- `search_blogs` - AJAX search functionality
- `latest_topics` - API endpoint for sidebar content

### Templates
- Base layout with navigation and sidebar
- Home page template
- Explore page with pagination
- Blog detail template
- About page template
- Responsive design for all screen sizes

### Styling
- Tailwind CSS integration
- Custom color scheme (Black/White)
- Dark mode support
- Smooth transitions and animations
- Mobile-optimized navigation
- Accessible design patterns

### Dependencies
- Django==5.2.6
- asgiref==3.9.1
- sqlparse==0.5.3
- tzdata==2025.2
- markdown==3.5.2

### Configuration
- Development settings with DEBUG=True
- SQLite database configuration
- Static files configuration
- Template directories setup
- Middleware configuration for security
- Admin interface customization

### Documentation
- Comprehensive README.md
- API documentation
- Contributing guidelines
- Deployment guide
- MIT License

## [0.1.0] - 2024-01-15

### Added
- Initial project setup
- Basic Django project structure
- Core app creation
- Initial models and migrations
- Basic template structure
- Admin interface setup

---

## Version History Summary

- **v1.0.0** - Full-featured blog platform with modern UI
- **v0.1.0** - Initial project setup and basic structure

## Migration Notes

### From v0.1.0 to v1.0.0
- Run `python manage.py migrate` to apply all database changes
- Update requirements.txt with new dependencies
- Collect static files with `python manage.py collectstatic`
- No breaking changes in this release

## Breaking Changes

None in current version.

## Security Updates

- CSRF protection enabled
- XFrame options middleware added
- Secure session configuration
- Input validation for search queries

## Performance Improvements

- Efficient pagination implementation
- Optimized database queries
- Static file optimization
- AJAX for dynamic content loading

## Bug Fixes

None reported in current version.

## Known Issues

- Search is limited to blog titles only
- No user authentication system yet
- No comment system implemented
- Limited to SQLite database in development

## Deprecations

None in current version.

## Contributors

- **Husnain** - Initial development and project setup

---

**Note**: This changelog will be updated with each release. For detailed commit history, please refer to the Git repository.

**Repository**: https://github.com/buildwithhusnain/blogme.git