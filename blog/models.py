import os.path

from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from markdownx.models import MarkdownxField


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    # toString override
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    # Categories 로 수정
    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_msg = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # override 해서 custom 객체로도 사용 가능, call back 함수를 통채로 넘겨줌, 일대다 관계
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # category
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # tag, many to many 는 null=True 가 default
    tag = models.ManyToManyField(Tag, blank=True)

    # toString method override
    def __str__(self):
        # f는 formatting
        return f'[{self.pk}] {self.title} - {self.author}'
        # return self.title

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        # 파일의 경로 부분을 잘라줌
        return os.path.basename(self.file_upload.name)

    def get_content_markdown(self):
        return markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # markdown 알아서 해라
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
