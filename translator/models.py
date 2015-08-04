from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User



class Paper(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    userId=models.ForeignKey(User)
    code=models.CharField(max_length=150,null=False,blank=False,unique=True)
    docx=models.FileField(blank=True,upload_to='uploads/%Y/%m/')

    def __unicode__(self):
        return smart_unicode(self.name)


class Paragraph(models.Model):
    num=models.IntegerField(null=False,blank=False)
    paperId=models.ForeignKey(Paper)
    txt=models.TextField(null=False,blank=False)

    def __unicode__(self):
        return smart_unicode(self.paperId.name+":"+str(self.num))

class Translated_Paragraph(models.Model):
    user=models.ForeignKey(User,blank=True)
    paraId=models.ForeignKey(Paragraph)
    txt=models.TextField(null=False,blank=False)


    def __unicode__(self):
        return smart_unicode(self.paraId.paperId.name+":"+str(self.paraId.num))

class Contact_Us(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    subject=models.CharField(max_length=150,null=False,blank=False)
    message=models.TextField(null=False,blank=False)

    def __unicode__(self):
        return smart_unicode(self.name+": "+self.subject)
