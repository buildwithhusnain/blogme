from django.db import models
from django.contrib.auth.models import User
import markdown
from django.utils.safestring import mark_safe

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_markdown_content(self):
        return mark_safe(markdown.markdown(self.content, extensions=['codehilite', 'fenced_code', 'tables']))
    
    def get_content_preview(self, words=30):
        plain_text = markdown.markdown(self.content)
        # Remove HTML tags for preview
        import re
        clean_text = re.sub('<.*?>', '', plain_text)
        words_list = clean_text.split()
        if len(words_list) > words:
            return ' '.join(words_list[:words]) + '...'
        return clean_text
