import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict


@dataclass
class Song:
    """Represents a song and its audio/metadata attributes."""
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
    """Represents a user's taste preferences used to score and rank songs."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dicts with proper numeric types."""
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences; returns (score, list of reasons)."""
    score = 0.0
    reasons = []

    # Genre match: worth most because genre is the strongest taste signal
    if song.get('genre') == user_prefs.get('genre'):
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: secondary taste signal
    if song.get('mood') == user_prefs.get('mood'):
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity: reward closeness on a 0-1 scale, up to +1.5 pts
    if 'energy' in user_prefs:
        energy_gap = abs(float(song.get('energy', 0)) - float(user_prefs['energy']))
        energy_score = round((1.0 - energy_gap) * 1.5, 2)
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song, sorts by score descending, and returns the top k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong match"
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]


class Recommender:
    """OOP wrapper around the scoring logic that operates on Song dataclass objects."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k Song objects ranked by score for the given UserProfile."""
        user_dict = {
            'genre': user.favorite_genre,
            'mood': user.favorite_mood,
            'energy': user.target_energy,
        }
        scored = []
        for song in self.songs:
            base_score, _ = score_song(user_dict, asdict(song))
            # Acoustic bonus: reward songs that match an acoustic preference
            acoustic_bonus = 0.5 if user.likes_acoustic and song.acousticness > 0.7 else 0.0
            scored.append((song, base_score + acoustic_bonus))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [s for s, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a plain-language explanation of why a song was recommended."""
        user_dict = {
            'genre': user.favorite_genre,
            'mood': user.favorite_mood,
            'energy': user.target_energy,
        }
        _, reasons = score_song(user_dict, asdict(song))
        if user.likes_acoustic and song.acousticness > 0.7:
            reasons.append("acoustic preference match (+0.5)")
        return ", ".join(reasons) if reasons else "no strong match found"
