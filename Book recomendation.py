book_recommendations = {
    'Fantasy': ['The Hobbit', 'A Song of ice and fire (Game of thrones)', 'The Name of the Wind', 'The Lies of Locke Lamora', 'The Way of Kings', 'The Priory of the Orange Tree', 'The Stormlight Archive', 'The Broken Empire Trilogy'],
    
    'Sci-Fi': ['Dune', 'Ender''s Game', 'Neuromancer', 'Foundation', 'Snow Crash', 'The Hitchhiker''s Guide to the Galaxy', 'Blindsight'],
    
    'Mystery': ['Sherlock Holmes: The Complete Novels and Stories', 'Gone Girl', 'The Girl with the Dragon Tattoo', 'And Then There Were None', 'The Big Sleep', 'In the Woods', 'The No. 1 Ladies'' Detective Agency', 'The Shadow of the Wind'],
    
    'Romance': ['Pride and Prejudice', 'The Notebook', 'Outlander', 'Jane Eyre', 'Wuthering Heights', 'The Thorn Birds', 'Love in the Time of Cholera', 'The Time Traveler''s Wife'],
    
    'Poetry': ['The Waste Land', 'Ariel', 'Leaves of Grass', 'The Sun and Her Flowers', 'The Essential Rumi', 'Pablo Neruda: Selected Poems', 'Howl and Other Poems', 'The Collected Poems of W.B. Yeats'],

    'Comedy': ['The Importance of Being Earnest', 'P.G. Wodehouse: A Life in Letters', 'Three Men in a Boat', 'Don Quixote', 'A Confederacy of Dunces', 'Bridget Jones Diary', 'Good Omens', 'The Hitchhiker\'s Guide to the Galaxy'],

    'Noir': ['The Big Sleep', 'The Maltese Falcon', 'Double Indemnity', 'Red Harvest', 'The Postman Always Rings Twice', 'Farewell, My Lovely', 'The Thin Man', 'Darkness at Noon'],

    'True Crime': ['In Cold Blood', 'The Suspicions of Mr. Whicher', 'The Black Dahlia', 'The Poisoner\'s Handbook', 'The Suspicions of Mr. Whicher', 'The Murder of Roger Ackroyd', 'Death in the City of Light', 'The Case of Mary Bell'],

    'History': ['A Short History of Nearly Everything', 'The Silk Roads: A New History of the World', 'A History of the World in 10½ Chapters', 'The Histories']
}

def recommend_books(favorite_genre):
    if favorite_genre in book_recommendations:
        recommended_books = book_recommendations[favorite_genre]
        print(f"Here are some recommended books in the {favorite_genre} genre")
        for book in recommended_books:
            print(f"- {book}")
    else:
        print("Sorry, I don't have recommendations for that genre.")

def main():
    print("Welcome to my little book recomendation program.")
    print("Please select your favorite genre from the following options below")
    
    for genre in book_recommendations.keys():
        print(f"- {genre}")
    
    favorite_genre = input("Enter your favorite genre (or type exit to quit) ")
    
    if favorite_genre.lower() == 'exit':
        print("Thank you for using the book recomendation program. Goodbye.")
        return

    recommend_books(favorite_genre)

    while True:
        try_again = input("Would you like to try another genre? (Write yes or no) ").lower()
        if try_again == 'yes':
            favorite_genre = input("Enter your favorite genre (or type exit to quit) ")
            if favorite_genre.lower() == 'exit':
                print("Thank you for using the Book Recommendation System. Goodbye!")
                break
            recommend_books(favorite_genre)
        elif try_again == 'no':
            print("Thank you for using my book recomendation program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'")

if __name__ == "__main__":
    main()