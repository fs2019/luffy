from django.db import models

class Banner(models.Model):
    '''轮播广告图'''
    title=models.CharField(max_length=500,verbose_name='广告标题')
    link=models.CharField(max_length=500,verbose_name='广告链接')
    image_url=models.ImageField(upload_to='banner',null=True,blank=True,max_length=255,verbose_name='广告图片')
    remark=models.TextField(verbose_name='备注信息')
    is_show=models.BooleanField(default=False,verbose_name='是否显示')
    orders=models.IntegerField(default=1,verbose_name='排序')
    is_deleted=models.BooleanField(default=False,verbose_name='是否逻辑删除')
    class Meta:
        db_table='ly_banner'
        verbose_name='轮播广告'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title
