from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.book = Book.objects.create(
		title="A good title",
		subtitle="A good subtitle",
		author="Tom Clancy",
		isbn="1234567891234",
		)

	def test_book_content(self):
		self.assertEqual(self.book.title, "A good title")
		self.assertEqual(self.book.subtitle, "A good subtitle")
		self.assertEqual(self.book.author, "Tom Clancy")
		self.assertEqual(self.book.isbn, "1234567891234")

	def test_book_list_view(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "A good subtitle")
		self.assertTemplateUsed(response, "books/book_list.html")

