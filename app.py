from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books_data = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    },
    {
        'id': 6,
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'publication_year': 1932,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 7,
        'title': 'Jane Eyre',
        'author': 'Charlotte Brontë',
        'publication_year': 1847,
        'genre': 'Gothic Fiction'
    },
    {
        'id': 8,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'publication_year': 1951,
        'genre': 'Coming-of-Age Fiction'
    },
    {
        'id': 9,
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'publication_year': 1954,
        'genre': 'Fantasy'
    },
    {
        'id': 10,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'publication_year': 1997,
        'genre': 'Fantasy'
    },
    {
        'id': 11,
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'publication_year': 1851,
        'genre': 'Adventure'
    },
    {
        'id': 12,
        'title': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
        'author': 'C.S. Lewis',
        'publication_year': 1950,
        'genre': 'Fantasy'
    },
    {
        'id': 13,
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel García Márquez',
        'publication_year': 1967,
        'genre': 'Magical Realism'
    },
    {
        'id': 14,
        'title': 'The Shining',
        'author': 'Stephen King',
        'publication_year': 1977,
        'genre': 'Horror'
    },
    {
        'id': 15,
        'title': 'The Picture of Dorian Gray',
        'author': 'Oscar Wilde',
        'publication_year': 1890,
        'genre': 'Gothic Fiction'
    },
    {
        'id': 16,
        'title': 'Fahrenheit 451',
        'author': 'Ray Bradbury',
        'publication_year': 1953,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 17,
        'title': 'The Merchant of Death',
        'author': 'D.J. MacHale',
        'publication_year': 2002,
        'genre': 'Fantasy'
    },
    {
        'id': 18,
        'title': 'The Road',
        'author': 'Cormac McCarthy',
        'publication_year': 2006,
        'genre': 'Post-Apocalyptic Fiction'
    },
    {
        'id': 19,
        'title': 'The Hitchhiker\'s Guide to the Galaxy',
        'author': 'Douglas Adams',
        'publication_year': 1979,
        'genre': 'Science Fiction'
    },
    {
        'id': 20,
        'title': 'Crime and Punishment',
        'author': 'Fyodor Dostoevsky',
        'publication_year': 1866,
        'genre': 'Psychological Fiction'
    }
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    # Extract filter parameters from the request
    book_id = request.args.get('id')
    title = request.args.get('title')
    author = request.args.get('author')
    publication_year = request.args.get('publication_year')
    genre = request.args.get('genre')

    # Apply filters based on the provided parameters
    filtered_books = books_data
    if book_id:
        try:
            book_id = int(book_id)
            filtered_books = [book for book in filtered_books if book.get('id') == book_id]
        except ValueError:
            return jsonify({"error": "Invalid id parameter (not an integer)"}), 400
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.get('title', '').lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.get('author', '').lower()]
    if publication_year:
        try:
            publication_year = int(publication_year)
            filtered_books = [book for book in filtered_books if book.get('publication_year') == publication_year]
        except ValueError:
            return jsonify({"error": "Invalid publication_year parameter (not an integer)"}), 400
    if genre:
        filtered_books = [book for book in filtered_books if genre.lower() in book.get('genre', '').lower()]

    if not filtered_books:
        return jsonify({"error": "No books match the specified criteria"}), 404

    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
