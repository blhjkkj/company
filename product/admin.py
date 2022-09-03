from django.contrib import admin
from .models import  Manufacturer, Brand,Shangping
# Register your models here.
from django.utils.safestring import mark_safe

class BrandInline(admin.TabularInline):
    model=Brand
    extra=3
class SpInline(admin.StackedInline):
    model=Shangping
    extra=1
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display=('manufacturer','M_license','odm')
    fieldsets=(
    ('生产商信息',
        {'fields':[('manufacturer','M_license',),('address','cont',),]#加[]由列变行
        }),
    ('委托商信息',
        {'fields':[('odm','odm_cont','odm_address',),]

        })
        
        )
    inlines=[SpInline]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines=[SpInline]    
@admin.register(Shangping)
class ShangpingAdmin(admin.ModelAdmin):
    list_display=('pr_name','upload_image','upload_video','brand','manu','price1','price2')
    list_filter=('pr_name','manu','brand')
    def upload_image(self,obj):#实现admin后台显示上传图片缩略图
        try:
            pic1=mark_safe('<img src="%s" width="100px"/>'%(obj.pic1.url,))
        except Exception as e:
            pic1=''
        return pic1
    upload_image.short_description="产品图片"
    upload_image.allow_tags=True
    def upload_video(self,obj):
        try:
            video=mark_safe('<video class=video width="200px" controls type=video/mp4 src="%s"  />'%(obj.video.url,))
        except Exception as e:
            video=''
        return video
    upload_video.short_description="产品视频"
    upload_video.allow_tags=True    
"""
    def show_pic1(request):
        f1=request.FILES.get('shangping')
    show_pic1.short_deseription="商品主图"
    show_pic1.allow_tags=True
    readonly_fields = ['show_pic']"""
        
    