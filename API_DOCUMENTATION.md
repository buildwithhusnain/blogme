# BlogMe API Documentation

This document describes the API endpoints available in the BlogMe application.

## 🌐 Base URL

```
http://127.0.0.1:8000  # Development
https://yourdomain.com  # Production
```

## 📋 API Endpoints

### 1. Search Blogs

Search through published blog posts by title.

**Endpoint:** `GET /api/search/`

**Parameters:**
- `q` (string, optional): Search query string

**Example Request:**
```bash
GET /api/search/?q=django
```

**Example Response:**
```json
{
  "results": [
    {
      "id": 1,
      "title": "Getting Started with Django",
      "author": "admin",
      "created_at": "2024-01-15"
    },
    {
      "id": 3,
      "title": "Django Best Practices",
      "author": "john_doe",
      "created_at": "2024-01-10"
    }
  ]
}
```

**Response Fields:**
- `id` (integer): Blog post ID
- `title` (string): Blog post title
- `author` (string): Author username
- `created_at` (string): Creation date in YYYY-MM-DD format

**Status Codes:**
- `200 OK`: Successful request
- `400 Bad Request`: Invalid parameters

**Notes:**
- Returns maximum 10 results
- Only searches published blogs
- Search is case-insensitive
- Empty query returns empty results

---

### 2. Latest Topics

Get the latest published blog topics for the sidebar.

**Endpoint:** `GET /api/latest-topics/`

**Parameters:** None

**Example Request:**
```bash
GET /api/latest-topics/
```

**Example Response:**
```json
{
  "topics": [
    {
      "id": 5,
      "title": "Advanced Django Techniques",
      "created_at": "2024-01-20 14:30"
    },
    {
      "id": 4,
      "title": "Building REST APIs with Django",
      "created_at": "2024-01-19 10:15"
    },
    {
      "id": 3,
      "title": "Django Best Practices",
      "created_at": "2024-01-18 16:45"
    }
  ]
}
```

**Response Fields:**
- `id` (integer): Blog post ID
- `title` (string): Blog post title
- `created_at` (string): Creation date and time in YYYY-MM-DD HH:MM format

**Status Codes:**
- `200 OK`: Successful request

**Notes:**
- Returns maximum 10 latest topics
- Only includes published blogs
- Ordered by creation date (newest first)
- Used for sidebar dynamic content

---

## 🔧 Frontend Integration

### JavaScript Fetch Examples

#### Search Functionality
```javascript
async function searchBlogs(query) {
    try {
        const response = await fetch(`/api/search/?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        return data.results;
    } catch (error) {
        console.error('Search error:', error);
        return [];
    }
}

// Usage
searchBlogs('django').then(results => {
    console.log('Search results:', results);
});
```

#### Latest Topics
```javascript
async function loadLatestTopics() {
    try {
        const response = await fetch('/api/latest-topics/');
        const data = await response.json();
        return data.topics;
    } catch (error) {
        console.error('Error loading topics:', error);
        return [];
    }
}

// Usage
loadLatestTopics().then(topics => {
    console.log('Latest topics:', topics);
});
```

### jQuery Examples

#### Search with jQuery
```javascript
function searchBlogs(query) {
    $.ajax({
        url: '/api/search/',
        method: 'GET',
        data: { q: query },
        success: function(data) {
            console.log('Search results:', data.results);
        },
        error: function(xhr, status, error) {
            console.error('Search error:', error);
        }
    });
}
```

#### Latest Topics with jQuery
```javascript
function loadLatestTopics() {
    $.ajax({
        url: '/api/latest-topics/',
        method: 'GET',
        success: function(data) {
            console.log('Latest topics:', data.topics);
        },
        error: function(xhr, status, error) {
            console.error('Error loading topics:', error);
        }
    });
}
```

## 🔒 Authentication

Currently, the API endpoints are public and do not require authentication. However, they only return published content.

**Future Authentication:**
- JWT token-based authentication planned
- API key authentication for external integrations
- Rate limiting for public endpoints

## 📊 Response Format

All API responses follow a consistent JSON format:

**Success Response:**
```json
{
  "results": [...],  // For search endpoint
  "topics": [...]    // For latest topics endpoint
}
```

**Error Response:**
```json
{
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

## 🚀 Rate Limiting

Currently, no rate limiting is implemented. For production use, consider implementing:

- **Per IP**: 100 requests per minute
- **Per User**: 1000 requests per hour
- **Search**: 10 requests per minute per IP

## 📈 Performance Considerations

### Caching
- Consider implementing Redis caching for frequently accessed data
- Cache search results for common queries
- Cache latest topics for 5-10 minutes

### Database Optimization
- Add database indexes on frequently queried fields
- Use `select_related()` for foreign key relationships
- Implement pagination for large result sets

### Example Optimized Views
```python
# Optimized search view
def search_blogs(request):
    query = request.GET.get('q', '')
    if query:
        blogs = Blog.objects.select_related('author').filter(
            Q(title__icontains=query) & Q(is_published=True)
        )[:10]
        # ... rest of the view
```

## 🔮 Future API Enhancements

### Planned Endpoints

1. **Blog CRUD API**
   - `GET /api/blogs/` - List all blogs
   - `POST /api/blogs/` - Create new blog
   - `GET /api/blogs/{id}/` - Get specific blog
   - `PUT /api/blogs/{id}/` - Update blog
   - `DELETE /api/blogs/{id}/` - Delete blog

2. **User Management**
   - `POST /api/auth/login/` - User login
   - `POST /api/auth/logout/` - User logout
   - `POST /api/auth/register/` - User registration
   - `GET /api/users/profile/` - Get user profile

3. **Comments System**
   - `GET /api/blogs/{id}/comments/` - Get blog comments
   - `POST /api/blogs/{id}/comments/` - Add comment
   - `PUT /api/comments/{id}/` - Update comment
   - `DELETE /api/comments/{id}/` - Delete comment

4. **Categories and Tags**
   - `GET /api/categories/` - List categories
   - `GET /api/tags/` - List tags
   - `GET /api/blogs/?category={id}` - Filter by category
   - `GET /api/blogs/?tag={id}` - Filter by tag

### API Versioning
Future versions will include versioning:
- `GET /api/v1/search/`
- `GET /api/v2/search/`

## 🛠️ Testing the API

### Using cURL

**Search Blogs:**
```bash
curl -X GET "http://127.0.0.1:8000/api/search/?q=django"
```

**Latest Topics:**
```bash
curl -X GET "http://127.0.0.1:8000/api/latest-topics/"
```

### Using Postman

1. Create a new request
2. Set method to GET
3. Enter the endpoint URL
4. Add query parameters if needed
5. Send the request

### Using Python Requests

```python
import requests

# Search blogs
response = requests.get('http://127.0.0.1:8000/api/search/', params={'q': 'django'})
print(response.json())

# Latest topics
response = requests.get('http://127.0.0.1:8000/api/latest-topics/')
print(response.json())
```

## 📞 Support

For API-related questions or issues:
1. Check this documentation
2. Review the source code in `core/views.py`
3. Create an issue on GitHub
4. Contact the development team

---

**API Version:** 1.0  
**Last Updated:** January 2024  
**Maintained by:** BlogMe Development Team