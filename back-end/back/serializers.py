from rest_framework import serializers
from .models import Year, Sector, Subject, Course, Exam

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name='me').exists():
            raise serializers.ValidationError("Only admin users can create a Year.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name='me').exists():
            raise serializers.ValidationError("Only admin users can update a Year.")
        return super().update(instance, validated_data)

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name='me').exists():
            raise serializers.ValidationError("Only admin users can create a Sector.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name='me').exists():
            raise serializers.ValidationError("Only admin users can update a Sector.")
        return super().update(instance, validated_data)



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can create a Sector.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can update a Sector.")
        return super().update(instance, validated_data)



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can create a Sector.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can update a Sector.")
        return super().update(instance, validated_data)



class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can create a Sector.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.groups.filter(name=['me', 'others']).exists():
            raise serializers.ValidationError("Only admin users can update a Sector.")
        return super().update(instance, validated_data)
