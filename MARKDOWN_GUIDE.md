# Markdown Guide for BlogMe

This guide shows you how to use markdown syntax in BlogMe to create rich, formatted blog posts.

## 📝 Basic Syntax

### Headings
```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~
```

### Lists

**Unordered Lists:**
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```

**Ordered Lists:**
```markdown
1. First item
2. Second item
   1. Nested item
   2. Another nested item
3. Third item
```

### Links and Images
```markdown
[Link text](https://example.com)
![Alt text](image-url.jpg)
```

### Blockquotes
```markdown
> This is a blockquote
> It can span multiple lines
>
> And have multiple paragraphs
```

## 💻 Code Syntax

### Inline Code
```markdown
Use `backticks` for inline code
```

### Code Blocks
````markdown
```python
def hello_world():
    print("Hello, World!")
    return "success"
```

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```

```html
<div class="container">
    <h1>Hello World</h1>
</div>
```
````

## 📊 Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More data|
| Row 2    | Data     | More data|
| Row 3    | Data     | More data|
```

**Alignment:**
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Left | Center | Right |
```

## 🔗 Advanced Features

### Horizontal Rule
```markdown
---
```

### Line Breaks
```markdown
Line 1  
Line 2 (two spaces at end of Line 1)

Or use a blank line between paragraphs.
```

### Escape Characters
```markdown
\*This won't be italic\*
\# This won't be a heading
```

## 🎨 BlogMe-Specific Features

### Supported Languages for Code Highlighting
- Python
- JavaScript
- HTML
- CSS
- SQL
- JSON
- Bash/Shell
- And many more...

### Best Practices

1. **Use headings hierarchically** - Start with H2 (##) for main sections
2. **Add blank lines** around code blocks and lists
3. **Use descriptive link text** instead of "click here"
4. **Keep lines under 80 characters** when possible
5. **Preview your content** using the live preview feature

## 📱 Mobile Considerations

- Tables automatically scroll horizontally on mobile
- Code blocks are optimized for mobile viewing
- Images are responsive by default

## 🌙 Dark Mode Support

All markdown elements are styled for both light and dark themes:
- Code blocks adapt to theme
- Tables have appropriate borders
- Blockquotes maintain readability

## 🔧 Editor Features

The BlogMe admin editor includes:

- **Live Preview**: See your formatted content in real-time
- **Toolbar**: Quick access to common formatting
- **Auto-save**: Your work is saved automatically
- **Full-screen**: Distraction-free writing mode
- **Word count**: Track your progress

## 📖 Example Blog Post

```markdown
# Getting Started with Python Web Development

Python has become one of the most popular languages for web development. In this post, we'll explore why.

## Why Choose Python?

Python offers several advantages:

- **Simple syntax** - Easy to read and write
- **Large ecosystem** - Thousands of packages available
- **Great frameworks** - Django, Flask, FastAPI
- **Strong community** - Excellent documentation and support

## Your First Django App

Here's how to create a simple Django view:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

## Comparison of Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| Django | Full-stack | Large applications |
| Flask | Micro | Small to medium apps |
| FastAPI | Modern | APIs and microservices |

> **Tip**: Start with Django if you're building a full web application with admin interface, user authentication, and database integration.

## Next Steps

1. Install Python and Django
2. Follow the official tutorial
3. Build your first project
4. Deploy to production

Happy coding! 🚀
```

## 🆘 Troubleshooting

### Common Issues

**Code not highlighting:**
- Make sure to specify the language after the opening ```
- Check that the language is supported

**Table not formatting:**
- Ensure proper spacing around pipes |
- Include the header separator row

**Images not showing:**
- Verify the image URL is accessible
- Use proper markdown image syntax

**Preview not updating:**
- Check your internet connection
- Refresh the page if needed

## 📚 Additional Resources

- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

---

**Happy writing with BlogMe! ✍️**