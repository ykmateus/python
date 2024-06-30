const books = [
    {
        title: "1984",
        author: "George Orwell",
        genre: "Distopia",
        year: 1949,
        rating: 5
    },
    {
        title: "O Senhor dos Anéis",
        author: "J.R.R. Tolkien",
        genre: "Fantasia",
        year: 1954,
        rating: 5
    },
    {
        title: "Dom Quixote",
        author: "Miguel de Cervantes",
        genre: "Aventura",
        year: 1605,
        rating: 4
    }
];

document.addEventListener('DOMContentLoaded', () => {
    loadBooks();

    document.getElementById('addBookButton').addEventListener('click', addBook);
    document.getElementById('searchButton').addEventListener('click', searchBooks);
    document.getElementById('sortCriteria').addEventListener('change', loadBooks);
});

function loadBooks() {
    displayBooks(books);
}

function displayBooks(books) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    const criteria = document.getElementById('sortCriteria').value;
    books.sort((a, b) => {
        if (criteria === 'title') {
            return a.title.localeCompare(b.title);
        } else if (criteria === 'author') {
            return a.author.localeCompare(b.author);
        } else {
            return b.rating - a.rating;
        }
    });
    books.forEach(book => {
        const bookItem = document.createElement('li');
        bookItem.classList.add('book-item');
        bookItem.innerHTML = `${book.title} - ${book.author} (${book.genre}, ${book.year}) - Avaliação: ${book.rating}`;
        bookList.appendChild(bookItem);
    });
}

function addBook() {
    const title = document.getElementById('titleInput').value;
    const author = document.getElementById('authorInput').value;
    const genre = document.getElementById('genreInput').value;
    const year = parseInt(document.getElementById('yearInput').value);
    const rating = parseFloat(document.getElementById('ratingInput').value);

    const newBook = { title, author, genre, year, rating };
    books.push(newBook);
    loadBooks();
}

function searchBooks() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const filteredBooks = books.filter(book =>
        book.title.toLowerCase().includes(query) ||
        book.author.toLowerCase().includes(query) ||
        book.genre.toLowerCase().includes(query)
    );
    displayBooks(filteredBooks);
}
