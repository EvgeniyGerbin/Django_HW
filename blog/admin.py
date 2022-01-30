from django.contrib import admin
from Blog.models import *


admin.site.register(Bloger)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikeComment)
admin.site.register(DisslikeComment)
admin.site.register(LikePost)
admin.site.register(DisslikePost)