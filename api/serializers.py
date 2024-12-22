from rest_framework import serializers
from .models import Meal,Rating
from django.contrib.auth.models import User


#Note:
# UUID > it is best practice, because it is not good to produce id from the serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')  # Represents keys in the JSON format
        extra_kwargs = {'password': {'write_only': True, 'required': True}}  # to hide the password



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description','no_of_ratings','avg_rating')  # Represents keys in the JSON format


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','meal')  # Represents keys in the JSON format

