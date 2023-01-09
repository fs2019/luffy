from rest_framework.generics import ListAPIView

from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constants

class BannerListAPIView(ListAPIView): # alt + enter 自动导包
    queryset = Banner.objects.filter(is_show=True,is_deleted=False).order_by('-orders','id')[:constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer

