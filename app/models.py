from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class BlogModel(models.Model):
    id = fields.UUIDField(pk=True)
    url = fields.CharField(max_length=50, unique=True)
    name = fields.CharField(max_length=50, unique=True)
    topic = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)


class PostModel(models.Model):
    id = fields.UUIDField(pk=True)
    blog = fields.ForeignKeyField('models.BlogModel', related_name='posts')
    text = fields.TextField()


# Pydantic schema
BlogSchema = pydantic_model_creator(BlogModel, name=f"{BlogModel.__name__}Schema")
BlogSchemaCreate = pydantic_model_creator(BlogModel, name=f"{BlogModel.__name__}SchemaCreate", exclude_readonly=True)

PostSchema = pydantic_model_creator(PostModel, name=f"{PostModel.__name__}Schema")
PostSchemaCreate = pydantic_model_creator(PostModel, name=f"{PostModel.__name__}SchemaCreate", exclude_readonly=True)
