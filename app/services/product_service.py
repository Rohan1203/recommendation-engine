from app.data.sample_data import products, user_interest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.data.sample_data import products, user_interest

def get_product(user_id: int):
    return {"id": user_id, "name": "Rohan"}

# def recommend_products(user_id: int):
    # interests = user_interest.get(user_id, [])

    # scored = []

    # for product in products:
    #     score = len(set(product["tags"]) & set(interests))
    #     if score > 0:
    #         scored.append((score, product))

    # # sort by best match
    # scored.sort(reverse=True, key=lambda x: x[0])

    # return [p for _, p in scored]


def recommend_products(user_id: int):
    interests = user_interest.get(user_id, [])

    # convert product tags to text
    product_texts = [" ".join(p["tags"]) for p in products]

    # user interest as text
    user_text = " ".join(interests)

    vectorizer = TfidfVectorizer()

    # fit + transform
    tfidf_matrix = vectorizer.fit_transform(product_texts + [user_text])

    # last vector = user
    user_vector = tfidf_matrix[-1]

    product_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(user_vector, product_vectors)[0]

    # attach score
    scored = list(zip(similarities, products))

    # sort by similarity
    scored.sort(reverse=True, key=lambda x: x[0])

    return [p for score, p in scored if score > 0]