from django.contrib import admin
from .models import Author,Book,Publisher#Register the models

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)

### python manage.py shell
###
'''
from books.models import Author, Book

# Create an author
author = Author(name='J.K. Rowling', bio='British author, best known for Harry Potter series')
author.save()

# Create a book associated with that author
book = Book(title='Harry Potter and the Philosopher\'s Stone', author=author, published_date='1997-06-26', summary='A young boy discovers he is a wizard.')
book.save()

# Verify the saved data
Author.objects.all()
Book.objects.all()
'''
###
# Fetch and print
#  all authors and books
'''
authors = Author.objects.all()
books = Book.objects.all()

# Print out all authors and books
for author in authors:
    print(f'Author: {author.name} - Bio: {author.bio}')

for book in books:
    print(f'Book: {book.title} - Author: {book.author.name} - Published Date: {book.published_date}')
'''
### delete
'''
#=>specific author
# Import your models
from books.models import Author, Book

# Fetch the object you want to delete (e.g., an author)
author = Author.objects.get(name='J.K. Rowling')

# Delete the object
author.delete()

# Verify deletion
Author.objects.all()  # This should no longer show the deleted author

#=>specific word
# Delete all authors whose name starts with 'J.'
Author.objects.filter(name__startswith='J.').delete()

# Delete all books published before the year 2000
Book.objects.filter(published_date__lt='2000-01-01').delete()

# Verify deletion
Author.objects.all()  # This should no longer show authors starting with 'J.'
Book.objects.all()    # This should no longer show books published before 2000

#=>All record
# Delete all authors (Be careful with this, as it will delete all records!)
Author.objects.all().delete()

# Delete all books
Book.objects.all().delete()

# Verify deletion
Author.objects.all()  # Should return an empty queryset
Book.objects.all()    # Should return an empty queryset
'''