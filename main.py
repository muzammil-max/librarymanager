library = []
def add_book():
    print("-- ADD BOOK --")
    title = input("enter book title: ").strip()
    author = input("Enter Book author: ").strip()
    try:
        publication_year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Publication year must be an integer. Book not added.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

def remove_book():
     print("==Remove a Book==")
     removetitle = input("ENTER A TITLE THAT YOU NEED TO REMOVE").strip().lower()
     for book in library:
            if book["title"].lower() == removetitle:
             library.remove(book)
             print("book removed sucessfully",book["title"])
            return
     print("book not found")

def searchbook():
    print("\n--- Search for a Book ---")
    search_type = input("Search by title or author? (title/author): ").strip().lower()
    query = input("Enter your search query: ").strip().lower()

    if search_type == "title":
        results = [book for book in library if query in book["title"].lower()]
    elif search_type == "author":
        results = [book for book in library if query in book["author"].lower()]
    else:
        print("Invalid search type.")
        return

    if results:
        print("\nMatching Books:")
        for idx, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")


def displayall():
    print("---Your Library---")
    if library:
            for idx, book in enumerate(library, start=1):
             status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
    else:
        print("Library is empty.")


def displayStats():
    print('--Library Stats--')
    total_books = len(library)
    read_count = sum(i for book in library if book["read"])
    percentage_read = (read_count / total_books * 100) if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")


def main():
    while True:
        print("Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            searchbook()
        elif choice == "4":
            displayall()
        elif choice == "5":
            displayStats()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



            
