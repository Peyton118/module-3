from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    is_favorite = models.BooleanField(max_length=50)

def create_contact(name, email, phone, is_favorite):
    new_contact = Contact.objects.create(name = name, email = email, phone = phone, is_favorite = is_favorite)
    return new_contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    for i in Contact.objects.all():
        if i.name == name:
            print(i)
            return i
        else:
            continue
    
def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
    Contact.objects.filter(name=name).update(email=new_email)

def delete_contact(name):
    Contact.object.filter(name=name).delete()