"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# User profiles
# ---------------------------------------------------------------------------

PROFILES = {
    # --- Standard profiles ---
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "valence": 0.80,
        "acousticness": 0.10,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "valence": 0.58,
        "acousticness": 0.80,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "valence": 0.40,
        "acousticness": 0.08,
    },

    # --- Edge case / adversarial profiles ---

    # Conflict: very high energy but a sad/melancholic mood.
    # Most high-energy songs have positive valence; this profile wants loud but sad.
    # Expected: scores will be split — energy matches metal/electronic but mood matches nothing well.
    "Sad Headbanger": {
        "genre": "metal",
        "mood": "melancholic",
        "energy": 0.95,
        "valence": 0.20,
        "acousticness": 0.05,
    },

    # Conflict: genre=jazz (typically low energy, acoustic) but energy=0.9.
    # No jazz song in the catalog has high energy, so the genre bonus will be cancelled
    # out by a poor energy proximity score. Tests whether categorical weight can "override"
    # numeric reality.
    "Wired Jazz Fan": {
        "genre": "jazz",
        "mood": "focused",
        "energy": 0.90,
        "valence": 0.65,
        "acousticness": 0.85,
    },

    # Extreme: every numeric preference sits at the midpoint (0.5).
    # No feature strongly pulls toward any song — tests whether the system
    # returns a meaningful ranking or collapses everything to near-equal scores.
    "Perfectly Average": {
        "genre": "indie pop",
        "mood": "happy",
        "energy": 0.50,
        "valence": 0.50,
        "acousticness": 0.50,
    },

    # No genre or mood keys at all — only numeric preferences.
    # Tests that score_song handles missing categorical keys without crashing
    # and still produces a valid ranking from numeric scores alone.
    "Numbers Only": {
        "energy": 0.60,
        "valence": 0.70,
        "acousticness": 0.55,
    },
}


def run_profile(name: str, user_prefs: dict, songs: list, k: int = 3) -> None:
    print(f"{'='*55}")
    print(f"Profile: {name}")
    print(f"Prefs:   {user_prefs}")
    print(f"{'='*55}")
    for song, score, explanation in recommend_songs(user_prefs, songs, k=k):
        print(f"  {song['title']} ({song['genre']}, {song['mood']}) — Score: {score:.2f}")
        for reason in explanation.split(" | "):
            print(f"    • {reason}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}\n")

    for name, prefs in PROFILES.items():
        run_profile(name, prefs, songs)


if __name__ == "__main__":
    main()
