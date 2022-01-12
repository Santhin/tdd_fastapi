from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Blog(models.Model):
    id = fields.UUIDField(pk=True)
    url = fields.CharField(max_length=50, unique=True)
    name = fields.CharField(max_length=50, unique=True)
    topic = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)


class Post(models.Model):
    id = fields.UUIDField(pk=True)
    blog = fields.ForeignKeyField(
        "models.Blog", related_name="posts"
    )  # blog_id <- Blog.id
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)


BlogSchema = pydantic_model_creator(Blog)
PostSchema = pydantic_model_creator(Post)
