from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class BaseModle(models.Model):
    #商品状态，1为上架，0为下架
    STATU=[
    (0,'下架'),
    (1,'上架'),
    (2,'放入仓库'),

    ]
    
    status=models.IntegerField(default="0",choices=STATU,verbose_name="商品状态")
    addtime=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    is_delete=models.BooleanField(default=False,verbose_name='删除标记')
    class Meta:
        abstract=True
        
class Manufacturer(models.Model):
    
    manufacturer=models.CharField(max_length=200,verbose_name='生产商')
    M_license=models.CharField(max_length=100,verbose_name='生产许可证号')
    address=models.CharField(max_length=100,verbose_name='生产商地址')
    cont=models.IntegerField(blank=True,null=True,verbose_name="联系电话")
    odm=models.CharField(max_length=100,blank=True,null=True,verbose_name='委托商')
    odm_cont=models.IntegerField(blank=True,null=True,verbose_name='联系方式')
    odm_address=models.CharField(max_length=100,null=True,blank=True,verbose_name="委托商地址")
    class Meta:
        verbose_name="生产商"
        verbose_name_plural='生产商管理'
    def __str__(self):
       return (self.manufacturer)

class Brand(models.Model):
    manu=models.ForeignKey(Manufacturer,on_delete=models.DO_NOTHING)
    brand=models.CharField(max_length=12,verbose_name="品牌名称")
    class Meta:
        verbose_name='品牌'
        verbose_name_plural='品牌管理'
    def get_shangpings(self):
    
        return Shangping.objects.filter(brand=self).order_by('manu')
    def __str__(self):
       return (self.brand)

def get_upload_path(instance, filename):
        name = instance.name.replace(' ', '_')
        return f'{name}/images/{filename}'
      
        
class Shangping(BaseModle):#子表
    PACK=[
    (0,"袋"),
    (1,"瓶"),
    (2,'支'),
    (3,'其他'),
    ];
    TYPE=[
    (0,'罐装'),
    (1,'瓶装'),
    (2,'袋装'),
    (3,'盒装'),
    (4,'组合装'),
    (5,'其他'),
    ];
    DOSAGE=[
    (0,'固体饮料'),
    (1,'压片糖果'),
    (2,'代用茶'),
    (3,'其他'),]
    name=models.CharField(max_length=30,verbose_name='产品名称')
    video=models.FileField(default='',upload_to=get_upload_path,verbose_name='产品视频')
    pic1=models.ImageField(default='',upload_to=get_upload_path,verbose_name="图片1")
    pic2=models.ImageField(default='',upload_to=get_upload_path,verbose_name="图片2")
    pic3=models.ImageField(default='',upload_to=get_upload_path,verbose_name="图片3")
    pic4=models.ImageField(default='',upload_to=get_upload_path,verbose_name="图片4")
    pic5=models.ImageField(default='',upload_to=get_upload_path,verbose_name="图片5")
    manu=models.ForeignKey(Manufacturer,on_delete=models.DO_NOTHING,verbose_name='生产商')
    brand=models.ForeignKey(Brand,on_delete=models.DO_NOTHING,verbose_name='品牌名')
    dosage=models.IntegerField(choices=DOSAGE,verbose_name='产品类型')
    standards=models.CharField(max_length=50,verbose_name='产品标准号')
    mixture=models.TextField(verbose_name="配料表")
    cat=models.CharField(max_length=100,verbose_name="商品标签")
    types=models.IntegerField(default="0",choices=TYPE,verbose_name='包装种类')
    first=models.CharField(max_length=15,verbose_name="装箱数")
    pack=models.IntegerField(choices=PACK,verbose_name='最小包装')
    net_veight=models.CharField(max_length=30,verbose_name='净含量')
    shelf_life=models.CharField(max_length=30,verbose_name='保质期')
    storge=models.CharField(max_length=100,verbose_name='储存方法')
    edible=models.CharField(max_length=200,verbose_name='食用方法')
    pr_name=models.CharField(max_length=100,verbose_name='宝贝标题')
    time=models.CharField(max_length=50,verbose_name="食用周期（天）")
    suitable_for=models.CharField(max_length=100,verbose_name='适宜人群')
    unsuitable_for=models.CharField(max_length=100,verbose_name='不适宜人群')

    price1 = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='零售价' )#商品价格，最长9位小数
    price2 = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='折扣价')
    content=RichTextUploadingField(verbose_name='产品详情')
    class Meta:
        db_table='db_shangpings' #指定表名
        verbose_name='产品详情'
        verbose_name_plural='产品详情'
        """def get_dosage(self,obj):
        return obj.get_dosage_display(),显示选项的名称，在urls中已解决"""
    def __str__(self):
       return (self.pr_name)
