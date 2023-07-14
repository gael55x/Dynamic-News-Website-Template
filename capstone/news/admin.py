from django.contrib import admin
from .models import (
    User,
    Post_Category,
    Post,
    ApprovedPost,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'if_journalist')


@admin.register(Post_Category)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'admin_evaluation', 'if_trending')


@admin.register(ApprovedPost)
class ApprovedPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'time_posted')
