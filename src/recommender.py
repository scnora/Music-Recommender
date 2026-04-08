from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"]       = float(row["energy"])
            row["tempo_bpm"]    = float(row["tempo_bpm"])
            row["valence"]      = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs


# ---------------------------------------------------------------------------
# Scoring weights
# ---------------------------------------------------------------------------
# Genre carries the most weight because it is the hardest boundary in taste:
# a jazz fan and a metal fan share almost no overlap.  Mood is softer and
# context-dependent (same user may want "chill" or "intense" on different days),
# so it is worth half a genre match.  The three numeric features split the
# remaining 1.5 points; energy is the most discriminating single feature in
# this dataset, so it gets the largest numeric slice.
#
#   genre match   +2.0   hard categorical boundary
#   mood match    +1.0   soft categorical signal
#   energy        +0.75  strongest numeric separator (rock vs lofi)
#   valence       +0.50  emotional positivity — meaningful but secondary
#   acousticness  +0.25  useful for ambient/folk/lofi, less so elsewhere
#                 -----
#   max possible   4.50
# ---------------------------------------------------------------------------

WEIGHTS = {
    "genre":       2.00,
    "mood":        1.00,
    "energy":      0.75,
    "valence":     0.50,
    "acousticness":0.25,
}


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Score a single song against user preferences.

    Scoring recipe
    --------------
    Categorical matches  → full point value if equal, 0 otherwise
    Numeric features     → weight × (1 - |song_value - user_value|)
                           gives 1.0 when perfect, 0.0 when maximally far

    Returns (score, explanation_string).
    """
    score = 0.0
    reasons = []

    # --- categorical ---
    if song.get("genre", "").lower() == user_prefs.get("genre", "").lower():
        score += WEIGHTS["genre"]
        reasons.append(f"genre match ({song['genre']})")

    if song.get("mood", "").lower() == user_prefs.get("mood", "").lower():
        score += WEIGHTS["mood"]
        reasons.append(f"mood match ({song['mood']})")

    # --- numeric proximity ---
    for feature in ("energy", "valence", "acousticness"):
        if feature in user_prefs:
            proximity = 1.0 - abs(song[feature] - user_prefs[feature])
            points    = WEIGHTS[feature] * proximity
            score    += points
            reasons.append(f"{feature} {proximity:.2f}×{WEIGHTS[feature]}")

    explanation = " | ".join(reasons) if reasons else "no strong match"
    return round(score, 3), explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Score every song, then return the top-k ranked by score descending.
    Expected return format: (song_dict, score, explanation)
    """
    scored = [(*score_song(user_prefs, song), song) for song in songs]
    # unpack to (song, score, explanation) and sort highest score first
    ranked = sorted(
        [(song, sc, exp) for sc, exp, song in scored],
        key=lambda x: x[1],
        reverse=True,
    )
    return ranked[:k]
