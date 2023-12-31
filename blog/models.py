from django.db import models
from user.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class ProjectImage(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"Image for {self.project.alt_text}"


class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(
        blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProfessionalAchievement(models.Model):
    achievement_type_choices = (
        ('Project', 'Project'),
        ('Promotion', 'Promotion'),
        ('Publication', 'Publication'),
        ('Quantifiable Result', 'Quantifiable Result'),
    )

    achievement_type = models.CharField(
        max_length=20, choices=achievement_type_choices)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # Fields specific to certain achievement types
    project_name = models.CharField(max_length=200, blank=True, null=True)
    promotion_details = models.CharField(max_length=200, blank=True, null=True)
    publication_title = models.CharField(max_length=200, blank=True, null=True)
    quantifiable_result = models.CharField(
        max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    feedback = models.TextField()
    img_url = models.ImageField(
        blank=True, null=True, default="skills/inledrobot.jpg")

    def __str__(self):
        return self.customer_name
