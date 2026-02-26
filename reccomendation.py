# EXPANDED RECOMMENDATION SYSTEM - COLLABORATIVE FILTERING

from math import sqrt

# Updated dataset with new names and movies
ratings = {
    "rahul": {"KGF": 5, "Bahubali": 3, "RRR": 4},
    "ananya": {"KGF": 4, "Bahubali": 5, "RRR": 2, "Pushpa": 5},
    "vishal": {"KGF": 2, "Bahubali": 5, "Pushpa": 4},
    "meera": {"Bahubali": 3, "RRR": 5, "Pushpa": 4},
    "kiran": {"KGF": 5, "RRR": 4, "Salaar": 5, "Jawan": 3},
    "divya": {"Bahubali": 4, "Jawan": 5, "Pushpa": 5},
    "rohit": {"KGF": 4, "Salaar": 4, "RRR": 5},
    "sneha": {"Bahubali": 5, "Jawan": 4, "RRR": 3},
    "arav": {"KGF": 3, "Pushpa": 5, "Salaar": 4},
    "niharika": {"RRR": 5, "Salaar": 5, "Jawan": 4}
}

# Cosine similarity
def similarity(user1, user2):
    common = set(ratings[user1]) & set(ratings[user2])
    if not common:
        return 0

    sum1 = sum(ratings[user1][item] ** 2 for item in common)
    sum2 = sum(ratings[user2][item] ** 2 for item in common)
    dot_product = sum(ratings[user1][item] * ratings[user2][item] for item in common)

    return dot_product / (sqrt(sum1) * sqrt(sum2))

# Recommendation function
def recommend(target_user):
    scores = {}

    for other_user in ratings:
        if other_user == target_user:
            continue

        sim = similarity(target_user, other_user)

        for item in ratings[other_user]:
            if item not in ratings[target_user]:
                scores.setdefault(item, 0)
                scores[item] += sim * ratings[other_user][item]

    recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recommendations

# Run system
if __name__ == "__main__":
    print("Available Users:")
    print(", ".join(ratings.keys()))

    user = input("\nEnter your name: ")

    if user not in ratings:
        print("User not found! Try one from the list.")
    else:
        recs = recommend(user)
        print(f"\n🎬 Recommended for {user}:")
        for movie, score in recs:
            print(f"⭐ {movie} (score: {round(score, 2)})")
