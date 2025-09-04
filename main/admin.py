from django.contrib import admin
from .models import (
    Skill, SoftSkill, Tag,
    Project, ProjectCoverImage,
    BlogPost, BlogCoverImage,
    Experience, Education, Message, PageViewLog
)


# Skill
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


# SoftSkill
@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'user')


# Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Project uchun inline
class ProjectCoverImageInline(admin.TabularInline):
    model = ProjectCoverImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [ProjectCoverImageInline]


# Blog uchun inline
class BlogCoverImageInline(admin.TabularInline):
    model = BlogCoverImage
    extra = 1


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'read_time')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogCoverImageInline]


# Tajriba
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')


# Ta’lim
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'teacher', 'start_year', 'end_year')


# Xabarlar
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'is_read', 'created_at')
    search_fields = ('subject', 'message', 'user__username')
    list_filter = ('is_read', 'created_at')



