from rest_framework import serializers
from rest_framework.reverse import reverse

# from api.serializers import UserPublicSerializer

from .models import Product
# from . import validators


# class ProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(
#             view_name='product-detail',
#             lookup_field='pk',
#             read_only=True
#     )
#     title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    # owner = UserPublicSerializer(source='user', read_only=True)
    
    # title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # body = serializers.CharField(source='content')
    # my_discount=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'

        fields =[
            # 'owner',
            'pk',
            'title',
            'content',
            # 'body',
            'price',
            'discounted_price',
            # 'my_discount'
            # 'public',
            # 'path',
            # 'endpoint',
        ]

    def get_discount(self,obj):
        return obj.get_discount()
    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }
    
    # def get_edit_url(self, obj):
    #     request = self.context.get('request') # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request) 