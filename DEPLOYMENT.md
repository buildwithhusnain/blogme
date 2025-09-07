# BlogMe Deployment Guide

This guide covers various deployment options for the BlogMe Django application.

## 🚀 Production Deployment Checklist

Before deploying to production, ensure you complete these essential steps:

### Security Configuration

1. **Environment Variables**
   ```bash
   # Create .env file
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgresql://user:password@localhost:5432/blogme
   ```

2. **Update settings.py**
   ```python
   import os
   from pathlib import Path
   
   # Security settings
   SECRET_KEY = os.environ.get('SECRET_KEY')
   DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
   ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
   
   # Database configuration
   if os.environ.get('DATABASE_URL'):
       import dj_database_url
       DATABASES = {
           'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
       }
   ```

3. **Install Production Dependencies**
   ```bash
   pip install gunicorn psycopg2-binary python-decouple dj-database-url
   ```

4. **Update requirements.txt**
   ```txt
   asgiref==3.9.1
   Django==5.2.6
   sqlparse==0.5.3
   tzdata==2025.2
   gunicorn==21.2.0
   psycopg2-binary==2.9.9
   python-decouple==3.8
   dj-database-url==2.1.0
   ```

### Static Files Configuration

```python
# settings.py
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# For serving media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Additional static files directories
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

## 🐳 Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blogme.wsgi:application"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secret-key
      - DATABASE_URL=postgresql://blogme_user:password@db:5432/blogme_db
    depends_on:
      - db
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=blogme_db
      - POSTGRES_USER=blogme_user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### Nginx Configuration

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream blogme {
        server web:8000;
    }

    server {
        listen 80;
        server_name yourdomain.com www.yourdomain.com;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl;
        server_name yourdomain.com www.yourdomain.com;

        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;

        location / {
            proxy_pass http://blogme;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }

        location /static/ {
            alias /app/staticfiles/;
        }

        location /media/ {
            alias /app/media/;
        }
    }
}
```

## ☁️ Cloud Platform Deployments

### Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Procfile**
   ```
   web: gunicorn blogme.wsgi:application --log-file -
   release: python manage.py migrate
   ```

3. **Create runtime.txt**
   ```
   python-3.11.0
   ```

4. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   heroku addons:create heroku-postgresql:mini
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   git push heroku main
   heroku run python manage.py createsuperuser
   ```

### DigitalOcean App Platform

1. **Create app.yaml**
   ```yaml
   name: blogme
   services:
   - name: web
     source_dir: /
     github:
       repo: buildwithhusnain/blogme
       branch: main
     run_command: gunicorn --worker-tmp-dir /dev/shm blogme.wsgi:application
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: DEBUG
       value: "False"
     - key: SECRET_KEY
       value: "your-secret-key"
   databases:
   - name: blogme-db
     engine: PG
     version: "15"
   ```

2. **Deploy via CLI**
   ```bash
   doctl apps create app.yaml
   ```

### AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Create .ebextensions/django.config**
   ```yaml
   option_settings:
     aws:elasticbeanstalk:container:python:
       WSGIPath: blogme.wsgi:application
     aws:elasticbeanstalk:environment:proxy:staticfiles:
       /static: staticfiles
   ```

3. **Deploy**
   ```bash
   eb init
   eb create production
   eb deploy
   ```

## 🖥️ VPS Deployment (Ubuntu)

### Server Setup

1. **Update System**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Dependencies**
   ```bash
   sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib
   ```

3. **Create Database**
   ```bash
   sudo -u postgres psql
   CREATE DATABASE blogme_db;
   CREATE USER blogme_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE blogme_db TO blogme_user;
   \q
   ```

4. **Setup Application**
   ```bash
   cd /var/www
   sudo git clone https://github.com/buildwithhusnain/blogme.git
   sudo chown -R $USER:$USER blogme
   cd blogme
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Environment**
   ```bash
   # Create .env file
   echo "SECRET_KEY=your-secret-key" >> .env
   echo "DEBUG=False" >> .env
   echo "DATABASE_URL=postgresql://blogme_user:your_password@localhost:5432/blogme_db" >> .env
   echo "ALLOWED_HOSTS=your-domain.com,www.your-domain.com" >> .env
   ```

6. **Run Migrations**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

### Gunicorn Configuration

1. **Create Gunicorn Socket**
   ```bash
   sudo nano /etc/systemd/system/blogme.socket
   ```
   
   ```ini
   [Unit]
   Description=blogme socket

   [Socket]
   ListenStream=/run/blogme.sock

   [Install]
   WantedBy=sockets.target
   ```

2. **Create Gunicorn Service**
   ```bash
   sudo nano /etc/systemd/system/blogme.service
   ```
   
   ```ini
   [Unit]
   Description=blogme daemon
   Requires=blogme.socket
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/var/www/blogme
   ExecStart=/var/www/blogme/venv/bin/gunicorn \
             --access-logfile - \
             --workers 3 \
             --bind unix:/run/blogme.sock \
             blogme.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Start Services**
   ```bash
   sudo systemctl start blogme.socket
   sudo systemctl enable blogme.socket
   sudo systemctl start blogme.service
   sudo systemctl enable blogme.service
   ```

### Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/blogme
```

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/blogme;
    }

    location /media/ {
        root /var/www/blogme;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/blogme.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/blogme /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## 📊 Monitoring and Logging

### Application Monitoring

1. **Install Sentry**
   ```bash
   pip install sentry-sdk[django]
   ```

2. **Configure Sentry**
   ```python
   # settings.py
   import sentry_sdk
   from sentry_sdk.integrations.django import DjangoIntegration

   sentry_sdk.init(
       dsn="your-sentry-dsn",
       integrations=[DjangoIntegration()],
       traces_sample_rate=1.0,
   )
   ```

### Log Configuration

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/blogme/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## 🔄 Continuous Deployment

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to server
      uses: appleboy/ssh-action@v0.1.5
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        key: ${{ secrets.KEY }}
        script: |
          cd /var/www/blogme
          git pull origin main
          source venv/bin/activate
          pip install -r requirements.txt
          python manage.py migrate
          python manage.py collectstatic --noinput
          sudo systemctl restart blogme
```

## 🛡️ Security Best Practices

1. **Use HTTPS everywhere**
2. **Keep dependencies updated**
3. **Regular security audits**
4. **Database backups**
5. **Monitor application logs**
6. **Use strong passwords**
7. **Implement rate limiting**
8. **Regular security updates**

## 📋 Post-Deployment Checklist

- [ ] Application loads correctly
- [ ] Database migrations applied
- [ ] Static files serving properly
- [ ] SSL certificate installed
- [ ] Admin panel accessible
- [ ] Search functionality working
- [ ] API endpoints responding
- [ ] Error pages configured
- [ ] Monitoring setup
- [ ] Backups configured

## 🆘 Troubleshooting

### Common Issues

1. **Static files not loading**
   ```bash
   python manage.py collectstatic --noinput
   sudo systemctl restart nginx
   ```

2. **Database connection errors**
   - Check DATABASE_URL environment variable
   - Verify database credentials
   - Ensure database server is running

3. **Permission errors**
   ```bash
   sudo chown -R www-data:www-data /var/www/blogme
   sudo chmod -R 755 /var/www/blogme
   ```

4. **Gunicorn not starting**
   ```bash
   sudo systemctl status blogme.service
   sudo journalctl -u blogme.service
   ```

For additional support, check the logs and create an issue on GitHub.

---

**Happy Deploying! 🚀**