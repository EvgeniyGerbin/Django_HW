from django.contrib import admin
from Blog.models import *


@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    pass


@admin.register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(DisslikeComment)
class DisslikeCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    pass


@admin.register(DisslikePost)
class DisslikePostAdmin(admin.ModelAdmin):
    pass
