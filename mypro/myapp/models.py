from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image



# Create your models here.
class Flower(models.Model):
    fname=models.CharField(max_length=25,blank=True)
    fplace=models.CharField(max_length=50,blank=True)
    fprice=models.DecimalField(max_digits=7,decimal_places=2)

    image=models.ImageField(upload_to='media' ,null=True,blank=True)
    qrcode=models.ImageField(upload_to='qr_codes/',null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fname
    

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.fname)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qr_image)
        fname = f'qrcode-{self.fname}.png' 
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super(Flower, self).save(*args, **kwargs) 