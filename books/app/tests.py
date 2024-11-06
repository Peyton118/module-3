from django.test import TestCase

# Create your tests here.
def test_can_create_books(self):
        Books = models.create_books(
            "Lord of The Rings",
            "J. R. R. Tolkien",
            "1954",
            True,
        )
        self.assertEqual(Books.id, 1)
        self.assertEqual(Books.name, "Lord of The Rings")
        self.assertEqual(Books.author, "J. R. R. Tolkien")
        self.assertTrue(Books.is_favorite)
def test_can_view_all_books_at_once(self):
        books_data = [
            {
                "name": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "release_date": "1937",
                "is_favorite": True,
            },
            {
                "name": "Wings of Fire",
                "author": "Tui Sutherland",
                "release_date": "1967",
                "is_favorite": False,
            },
            {
                "name": "Hunger Games",
                "author": "Suzanne Collins",
                "release_date": "2008",
                "is_favorite": True,
            },
        ]
        for Books_data in Books_data:
            models.create_Books(
                Books_data["name"],
                Books_data["author"],
                Books_data["release_date"],
                Books_data["is_favorite"],
            )
        Books = models.all_Books()
        self.assertEqual(len(Books), len(Books_data))
        Books_data = sorted(Books_data, key=lambda c: c["name"])
        Books = sorted(Books, key=lambda c: c.name)
        for data, Books in zip(Books_data, Books):
            self.assertEqual(data["name"], Books.name)
            self.assertEqual(data["email"], Books.author)
            self.assertEqual(data["phone"], Books.release_date)
            self.assertEqual(data["is_favorite"], Books.is_favorite)
def test_can_search_by_name(self):
        Books_data = [
            {
                "name": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "release_date": "1937",
                "is_favorite": True,
            },
            {
                "name": "Wings of Fire",
                "author": "Tui Sutherland",
                "release_date": "1967",
                "is_favorite": False,
            },
            {
                "name": "Hunger Games",
                "author": "Suzanne Collins",
                "release_date": "2008",
                "is_favorite": True,
            },
        ]
        for Books_data in Books_data:
            models.create_Books(
                Books_data["name"],
                Books_data["author"],
                Books_data["release_date"],
                Books_data["is_favorite"],
            )
        self.assertIsNone(models.find_Books_by_name("aousnth"))
        contact = models.find_Books_by_name("Hunger Games")
        self.assertIsNotNone(Books)
        self.assertEqual(Books.author, "Suzanne Collins")
def test_can_view_favorites(self):
        Books_data = [
            {
                "name": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "release_date": "1937",
                "is_favorite": True,
            },
            {
                "name": "Wings of Fire",
                "author": "Tui Sutherland",
                "release_date": "1967",
                "is_favorite": False,
            },
            {
                "name": "Hunger Games",
                "author": "Suzanne Collins",
                "release_date": "2008",
                "is_favorite": True,
            },
        ]
        for Books_data in Books_data:
            models.create_Books(
                Books_data["name"],
                Books_data["author"],
                Books_data["release_date"],
                Books_data["is_favorite"],
            )
        self.assertEqual(len(models.favorite_Books()), 2)
def test_can_update_Books_author(self):
        Books_data = [
            {
                "name": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "release_date": "1937",
                "is_favorite": True,
            },
            {
                "name": "Wings of Fire",
                "author": "Tui Sutherland",
                "release_date": "1967",
                "is_favorite": False,
            },
            {
                "name": "Hunger Games",
                "author": "Suzanne Collins",
                "release_date": "2008",
                "is_favorite": True,
            },
        ]
        for Books_data in Books_data:
            models.create_Books(
                Books_data["name"],
                Books_data["author"],
                Books_data["release_date"],
                Books_data["is_favorite"],
            )
        models.update_Books_author("Hunger Games", "Suzanne Collins")
        self.assertEqual(
            models.find_Books_by_name("Hunger Games").email, "Suzanne Collin"
        )
def test_can_delete_Books(self):
        Books_data = [
            {
                "name": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "release_date": "1937",
                "is_favorite": True,
            },
            {
                "name": "Wings of Fire",
                "author": "Tui Sutherland",
                "release_date": "1967",
                "is_favorite": False,
            },
            {
                "name": "Hunger Games",
                "author": "Suzanne Collins",
                "release_date": "2008",
                "is_favorite": True,
            },
        ]
        for Books_data in Books_data:
            models.create_Books(
                Books_data["name"],
                Books_data["author"],
                Books_data["release_date"],
                Books_data["is_favorite"],
            )
        models.delete_Books("Wings of Fire")
        self.assertEqual(len(models.all_Books()), 2)