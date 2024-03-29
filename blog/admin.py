from django.contrib import admin
from . models import (
    ContactProfile,
    Testimonial,
    Media,
    Certificate,
    Skill,
    Project,
    ProjectImage,
    Post,
    Tag,
    Comment,
    Review,

)


class ProjectImageInline(admin.TabularInline):
    list_display = ('id', 'image', 'alt_text')
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    inlines = [
        ProjectImageInline,
    ]
    readonly_fields = ('slug',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'timestamp', )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Review)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id',  'rating')


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
