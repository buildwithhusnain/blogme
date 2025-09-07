# Contributing to BlogMe

Thank you for your interest in contributing to BlogMe! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Git
- Basic knowledge of Django
- Familiarity with HTML, CSS, and JavaScript

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/blogme.git
   cd blogme
   ```

2. **Set up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Test Data**
   ```bash
   python manage.py createsuperuser
   ```

## 📋 Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use Django best practices

### Commit Messages

Use clear, descriptive commit messages:
```
feat: add search functionality to blog posts
fix: resolve pagination issue on explore page
docs: update README with installation instructions
style: improve responsive design for mobile devices
```

### Branch Naming

- `feature/feature-name` for new features
- `fix/bug-description` for bug fixes
- `docs/documentation-update` for documentation
- `refactor/component-name` for refactoring

## 🧪 Testing

### Running Tests

```bash
python manage.py test
```

### Writing Tests

- Write tests for new features
- Test both positive and negative cases
- Use Django's TestCase class
- Mock external dependencies

Example test structure:
```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_blog_creation(self):
        blog = Blog.objects.create(
            title='Test Blog',
            content='Test content',
            author=self.user
        )
        self.assertEqual(blog.title, 'Test Blog')
        self.assertTrue(blog.is_published)
```

## 🎯 Areas for Contribution

### High Priority
- User authentication and registration
- Comment system for blog posts
- Categories and tags for blogs
- Rich text editor for blog creation
- Image upload functionality

### Medium Priority
- Social media sharing
- Email notifications
- RSS feed
- Blog analytics
- SEO optimization

### Low Priority
- Multi-language support
- Advanced search filters
- User profiles
- Blog bookmarking
- Export functionality

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Detailed steps to reproduce the bug
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: OS, Python version, Django version
6. **Screenshots**: If applicable

### Bug Report Template

```markdown
**Bug Description**
A clear and concise description of the bug.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
- OS: [e.g. Windows 10, macOS, Ubuntu]
- Python Version: [e.g. 3.9.0]
- Django Version: [e.g. 5.2.6]
- Browser: [e.g. Chrome, Firefox]

**Additional Context**
Add any other context about the problem here.
```

## 💡 Feature Requests

For feature requests, please:

1. Check if the feature already exists
2. Search existing issues for similar requests
3. Provide a clear use case
4. Explain the expected behavior
5. Consider the impact on existing functionality

### Feature Request Template

```markdown
**Feature Description**
A clear and concise description of the feature you'd like to see.

**Use Case**
Explain the problem this feature would solve or the value it would add.

**Proposed Solution**
Describe how you envision this feature working.

**Alternatives Considered**
Any alternative solutions or features you've considered.

**Additional Context**
Add any other context, mockups, or examples about the feature request.
```

## 🔄 Pull Request Process

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write clean, well-documented code
   - Follow the coding standards
   - Add tests for new functionality

3. **Test Your Changes**
   ```bash
   python manage.py test
   python manage.py runserver  # Manual testing
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Use a clear, descriptive title
   - Provide detailed description of changes
   - Reference any related issues
   - Add screenshots for UI changes

### Pull Request Template

```markdown
**Description**
Brief description of the changes made.

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

**Testing**
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

**Screenshots**
If applicable, add screenshots of the changes.

**Checklist**
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Code is commented where necessary
- [ ] Documentation updated if needed
```

## 📚 Resources

### Django Documentation
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

### Frontend Resources
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [MDN Web Docs](https://developer.mozilla.org/)

### Git Resources
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 🤝 Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Unacceptable Behavior

Examples of unacceptable behavior include:
- The use of sexualized language or imagery
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## 📞 Getting Help

If you need help or have questions:

1. Check the [README](README.md) for basic setup and usage
2. Search existing [GitHub Issues](https://github.com/buildwithhusnain/blogme/issues)
3. Create a new issue with the "question" label
4. Join our community discussions

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- GitHub contributors page

Thank you for contributing to BlogMe! 🎉