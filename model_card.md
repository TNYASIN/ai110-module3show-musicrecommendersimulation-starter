# Model Card: VibeFinder 1.0

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This is a classroom simulation, not a real product. It's meant to show how a simple content-based recommender works step by step. It recommends songs from a 19-song catalog based on a user's preferred genre, mood, and energy level. Not for real users or for production.

---

## 3. How the Model Works

You give it a taste profile consisting of genre, moood and energy,etc. It goes through every song in the catalog and gives each one a score based on how well it matches:

- Songs in the same genre get 2 points
- Songs with the same mood get 1 point
- Songs close to your target energy get up to 1.5 points (the closer, the more)
- If you like acoustic music and the song is very acoustic, it gets a bonus 0.5

After scoring every song, it sorts them and returns the top ones.

---

## 4. Data

- 19 songs total (10 from the starter + 9 I added)
- Features: genre, mood, energy, tempo, valence, danceability, acousticness
- Genres in the catalog: folk, indie, rock, lofi, pop, jazz, ambient, synthwave, indie pop, world
- Moods: melancholy, chill, moody, intense, happy, relaxed, focused
- Some of the songs I added are real songs I actually listen to (Come Here by Kate Bloom, These Days by Nico, Keep the Rain by Searows, etc.)
- The energy and mood values I assigned manually — they're my interpretation, not pulled from actual audio analysis, so they're subjective

---

## 5. Strengths

- Really easy to understand what it's doing and why. The reason string tells you exactly which features matched.
- Works well when the user has a strong, clear preference (like "only folk" or "only high-energy rock"). The right songs rise to the top quickly.
- The energy similarity scoring it rewards closeness. So a "target 0.3" user doesn't get served 0.9 energy songs just because they score high elsewhere.

---

## 6. Limitations and Bias

- **Genre dominates too much.** A song that matches on mood and energy but has a slightly different genre label will almost always lose to a genre match with no other overlap. "Indie" and "folk" are basically the same vibe in real life but my system treats them as completely different.
- **The catalog is too small.** With only 19 songs, some genres have only 2-3 tracks. If you search for "world" music, there's literally one option. The recommendations aren't useful at that scale.
- **Moods are inconsistent.** I labeled songs with moods based on feel, but "moody" and "melancholy" are pretty similar and there's no rule separating them. That inconsistency leaks into the scores.
- **No diversity.** The top 5 can all be the same genre and essentially the same song. A real system would try to show variety.
- **Acoustic bonus is a guess.** I picked 0.7 as the threshold for "highly acoustic" but that's arbitrary. There's no good reason it's not 0.6 or 0.8.

---

## 7. Evaluation

I tested three profiles:

- **Folk/melancholy/low energy** (my actual taste): Came Here, These Days, Keep the Rain all ranked at the top. Felt right to me since those are songs I actually love.
- **High-energy rock**: Poison and Storm Runner rose to the top. JAURIM also appeared even though its mood label didn't match, purely on energy similarity. That was interesting.
- **Chill lofi**: Basically auto-filled with the three lofi tracks in the catalog. Not much insight there since the catalog has so few lofi songs.

What surprised me: when I removed mood scoring, *Spacewalk Thoughts* (ambient/chill) outranked *Strangers* (indie/moody) for the melancholy folk profile. The system couldn't tell that quiet + sad is different from quiet + spacey without that mood signal.

---

## 8. Future Work

1. Add genre proximity so "indie" and "folk" get partial credit for each other instead of zero.
2. Track which songs get skipped and use that to adjust the profile over time — even a simple version of that would make it way more useful.
3. Add a diversity rule so the same genre can only appear twice in the top 5.
4. Get the actual Spotify audio features for each song instead of manually guessing energy and valence.

---

## 9. Personal Reflection

Before this I kind of assumed recommenders were just "smarter" than simple math, like there had to be some deep model behind it. But building this showed me that even a few simple rules with the right weights can produce results that feel pretty reasonable. 

The thing that stuck with me most was how invisible these decisions are to the user. When Spotify serves me a song, I have no idea if it ranked high because of genre, because of tempo, or because 10 million other people with my listening history liked it. Building this from scratch made that opacity feel more real.
