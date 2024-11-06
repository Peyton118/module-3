from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    is_favorite = models.BooleanField(max_length=50)

def create_book(name, author, release_date, is_favorite):
    new_book = Books.objects.create(name = name, author = author, release_date = release_date, is_favorite = is_favorite)
    return new_book

def all_books():
    return Books.objects.all()

def find_books_by_name(name):
    for i in Books.objects.all():
        if i.name == name:
            print(i)
            return i
        else:
            continue
    
def favorite_Books():
    return Books.objects.filter(is_favorite=True)

def update_Books_author(name, new_author):
    Books.objects.filter(name=name).update(author=new_author)

    def delete_contact(name):
        Contact.object.filter(name=name).delete()