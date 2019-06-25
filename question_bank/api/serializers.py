from rest_framework import serializers
from question_bank.models import *

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = [
            'id',
            'text',
            'picture',
            'explanation',
            'explanationPicture',
            'predicament',

        ]


class SSCQuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    class Meta:
        model = SSCquestions
        depth = 1
        #fields = '__all__'
        fields = [
            'id',
            'max_marks',
            'negative_marks',
            'text',
            'section_category',
            'picture',
            'source',
            'language',
            'choices',
        ]

    def get_choices(self,obj):
        return\
    ChoicesSerializer(obj.choices_set.all(),many=True,read_only=True).data