from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import User, Project, BlogPost, Experience, Education

class AdminProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = User
        fields = '__all__'

class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Project
        fields = '__all__'

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = BlogPost
        fields = '__all__'

class ExperienceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Experience
        fields = '__all__'

class EducationAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Education
        fields = '__all__'
