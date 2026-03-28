import csv
import json

# -------------------------------
# Convert Genre → Mood
# -------------------------------
def get_mood(genre_list):
    genres = [g["name"] for g in genre_list]

    if "Comedy" in genres or "Family" in genres:
        return "Happy"
    elif "Romance" in genres:
        return "Romantic"
    elif "Drama" in genres:
        return "Sad"
    elif "Action" in genres or "Adventure" in genres or "Science Fiction" in genres:
        return "Excited"
    elif "Horror" in genres or "Thriller" in genres:
        return "Scared"
    else:
        return "Other"


# -------------------------------
# Load Movies from Kaggle CSV
# -------------------------------
def load_movies():
    movie_list = []

    with open("tmdb_5000_movies.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                # Convert genres string → list
                genres = json.loads(row["genres"])

                mood = get_mood(genres)

                movie = {
                    "title": row["title"],
                    "rating": float(row["vote_average"]),
                    "mood": mood
                }

                movie_list.append(movie)

            except:
                continue  # skip bad rows

    return movie_list


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend():
    movies = load_movies()

    print("\nChoose your mood:")
    print("Happy, Sad, Excited, Romantic, Scared")

    user_mood = input("Enter your mood: ").capitalize()

    # Filter movies
    filtered = [m for m in movies if m["mood"] == user_mood]

    if filtered:
        # Sort by rating
        filtered.sort(key=lambda x: x["rating"], reverse=True)

        print(f"\nTop movies for your '{user_mood}' mood:\n")

        for movie in filtered[:10]:
            print(f"{movie['title']} (⭐ {movie['rating']})")

    else:
        print("No movies found for this mood.")


# -------------------------------
# Run Program
# -------------------------------
recommend()