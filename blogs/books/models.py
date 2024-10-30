from django.db import models
from django.core.exceptions import ValidationError

class Author(models.Model):
    
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# One to Many relations with Book
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    def __str__(self):
        return self.name
    

# Many to One relations with Author
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title


### # Add your app in settings.py

### python manage.py makemigrations

### python manage.py migrate

### go to admin.py

### 

'''
from books.models import Author, Book, Publisher

# Create some sample publishers
publisher1 = Publisher.objects.create(name="Publisher 1")
publisher2 = Publisher.objects.create(name="Publisher 2")

# Create authors
author1 = Author.objects.create(name="Author 1", country="USA")
author2 = Author.objects.create(name="Author 2", country="UK")
author3 = Author.objects.create(name="Author 3", country="Canada")

# Create books for Author 1
Book.objects.create(
    author=author1,
    title="Book 1 by Author 1",
    description="First book by Author 1",
    publication_date="2023-01-01",
    price=19.99,
    publisher=publisher1,
    genre="Fiction"
)

Book.objects.create(
    author=author1,
    title="Book 2 by Author 1",
    description="Second book by Author 1",
    publication_date="2023-02-01",
    price=24.99,
    publisher=publisher2,
    genre="Non-Fiction"
)

# Create books for Author 2
Book.objects.create(
    author=author2,
    title="Book 1 by Author 2",
    description="First book by Author 2",
    publication_date="2023-03-01",
    price=29.99,
    publisher=publisher1,
    genre="Science Fiction"
)

Book.objects.create(
    author=author2,
    title="Book 2 by Author 2",
    description="Second book by Author 2",
    publication_date="2023-04-01",
    price=34.99,
    publisher=publisher2,
    genre="Romance"
)

# Create a book for Author 3
Book.objects.create(
    author=author3,
    title="Book 1 by Author 3",
    description="First book by Author 3",
    publication_date="2023-05-01",
    price=39.99,
    publisher=publisher1,
    genre="Thriller"
)

print("Sample data has been added.")

'''
'''
from books.models import Author

# Create sample authors
author1 = Author.objects.create(
    name="Author 1",
    birth_date="1980-05-15",  # YYYY-MM-DD format
    country="USA",
    website="https://author1.com"
)

author2 = Author.objects.create(
    name="Author 2",
    birth_date="1975-11-20",
    country="UK",
    website="https://author2.com"
)

author3 = Author.objects.create(
    name="Author 3",
    birth_date="1990-03-10",
    country="Canada",
    website="https://author3.com"
)

author4 = Author.objects.create(
    name="Author 4",
    birth_date="1985-09-25",
    country="Australia",
    website="https://author4.com"
)

print("Authors added successfully.")

#Verification:
for author in Author.objects.all():
    print(f"Author: {author.name}, Birth Date: {author.birth_date}, Country: {author.country}, Website: {author.website}")

'''
'''
from books.models import Publisher

# Create sample publishers
publisher1 = Publisher.objects.create(
    name="Publisher 1",
    published_date="2005-08-01",  # YYYY-MM-DD format
    address="123 Main St, New York, NY",
    phone="123-456-7890"
)

publisher2 = Publisher.objects.create(
    name="Publisher 2",
    published_date="2010-05-15",
    address="456 Elm St, London, UK",
    phone="234-567-8901"
)

publisher3 = Publisher.objects.create(
    name="Publisher 3",
    published_date="2015-02-20",
    address="789 Maple Ave, Toronto, Canada",
    phone="345-678-9012"
)

publisher4 = Publisher.objects.create(
    name="Publisher 4",
    published_date="2020-11-05",
    address="321 Oak Rd, Sydney, Australia",
    phone="456-789-0123"
)

print("Publishers added successfully.")

'''
'''
from books.models import Book, Author, Publisher

# Assuming the authors and publishers were created previously
author1 = Author.objects.get(name="Author 1")
author2 = Author.objects.get(name="Author 2")
publisher1 = Publisher.objects.get(name="Publisher 1")
publisher2 = Publisher.objects.get(name="Publisher 2")

# Create sample books
book1 = Book.objects.create(
    author=author1,
    title="Book 1 by Author 1",
    description="This is the first book by Author 1.",
    publication_date="2023-01-01",  # YYYY-MM-DD format
    price=19.99,
    publisher=publisher1
)

book2 = Book.objects.create(
    author=author1,
    title="Book 2 by Author 1",
    description="The second book by Author 1 is even more exciting.",
    publication_date="2023-06-15",
    price=24.99,
    publisher=publisher2
)

book3 = Book.objects.create(
    author=author2,
    title="Book 1 by Author 2",
    description="A great debut by Author 2.",
    publication_date="2023-03-10",
    price=29.99,
    publisher=publisher1
)

book4 = Book.objects.create(
    author=author2,
    title="Book 2 by Author 2",
    description="The follow-up novel by Author 2.",
    publication_date="2023-08-05",
    price=34.99,
    publisher=publisher2
)

print("Books added successfully.")

'''