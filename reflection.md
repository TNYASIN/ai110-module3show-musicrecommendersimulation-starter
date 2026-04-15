# Profile Comparison Notes

## Folk/melancholy vs High-energy rock

Folk/melancholy (`energy: 0.25`) → top: Come Here, These Days, Keep the Rain  
Rock/intense (`energy: 0.9`) → top: Poison, 9+1#, Storm Runner

No overlap at all, which makes sense. These two profiles are basically opposite ends of the catalog. What's interesting is that JAURIM showed up for the rock profile even though its mood is "moody" not "intense" — the energy (0.80) was close enough to 0.9 that it still ranked high. That shows energy can compensate for a mood mismatch if the gap is small enough.

---

## Folk/melancholy vs Chill lofi

Folk/melancholy → top: Come Here, These Days, Keep the Rain (folk songs)  
Chill lofi (`genre: lofi, mood: chill, energy: 0.35`) → top: Library Rain, Midnight Coding, Focus Flow

Both profiles want quiet, low-energy music but they end up with completely different results because genre is weighted so high. A lofi user never gets folk songs even though they'd probably enjoy them. That's the genre dominance problem in action. If I lowered the genre weight, these two profiles would probably overlap more, which might actually be more useful.

---

## High-energy rock vs Chill lofi

Rock/intense → high energy, electric, fast  
Chill lofi → low energy, mellow, slow

These two have nothing in common and the results show it. No shared songs anywhere in the top 5. The energy ranges don't overlap at all (rock profile targets 0.9, lofi targets 0.35). This is the pair where the system does exactly what you'd want — it keeps them completely separate. No weird cross-recommendations.

---

## Adversarial: conflicting preferences (rock genre, but melancholy mood, energy 0.5)

The genre match (+2.0) still dominated. *Storm Runner* and *Poison* ranked near the top even though their mood is "intense," not "melancholy." The mood signal just couldn't overcome the genre bonus. So someone asking for "sad rock" would basically get served "intense rock" because the system treats genre as the top priority. That felt like a real limitation — there's no way to say "I want the rock sound but the emotional weight of a sad song."
