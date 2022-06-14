from rest_framework import serializers

from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']

    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self,data):
        ct = data.get('city')
        rl = data.get('roll')
        if rl == 188 or ct.lower() != "lhr":
            raise serializers.ValidationError("City must be lhr")
        return data