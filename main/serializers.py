from rest_framework import serializers
from .models import *
from rest_framework.fields import SerializerMethodField

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class SkillSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'icon']


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = '__all__'



class ProjectsCoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCoverImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    image = serializers.ImageField(required=False)
    cover_images = ProjectsCoverImageSerializer(many=True, read_only=True)  # vaqtincha

    class Meta:
        model = Project
        fields = '__all__'

class ProjectSerializerCreate(serializers.ModelSerializer):
    tag = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        tag_names = validated_data.pop('tag', [])
        project = Project.objects.create(**validated_data)

        tags = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag_obj)

        project.tag.set(tags)
        return project


class BlogCoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCoverImage
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    view_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    image = serializers.ImageField(required=False)
    cover_images = BlogCoverImageSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'image', 'tag',
            'created_at', 'updated_at',
            'view_count', 'comment_count', 'description', 'is_published', 'read_time', 'cover_images'
        ]
        read_only_fields = ['slug']

    def get_view_count(self, obj):
        return obj.views.count()

    def get_comment_count(self, obj):
        return obj.comment_set.count()



class BlogPostSerializerCreate(serializers.ModelSerializer):
    tag = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['slug']

    def create(self, validated_data):
        tag_names = validated_data.pop('tag', [])
        blog = BlogPost.objects.create(**validated_data)

        tags = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag_obj)

        blog.tag.set(tags)
        return blog

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'



class PageViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageViewLog
        fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},

        }