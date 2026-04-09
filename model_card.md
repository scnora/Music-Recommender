# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  


VibeMatcher 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


This recommender is designed to suggest songs based on a user’s vibe and preferences. It mainly recommends songs using features like energy, mood, and genre.

It assumes the user has a general taste (like chill, high-energy, etc.) that can be represented with a few numbers and categories.

This is not for real users. It’s for classroom exploration to understand how recommendation systems work.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


The model looks at features like energy, valence, acousticness, genre, and mood. It compares those to what the user likes.

For numeric features, it checks how close the song is to the user’s preference. The closer it is, the higher the score.

For genre and mood, it gives bonus points if they match. Genre has the biggest weight, so it matters the most.

Then it adds everything together to get a final score. After that, it sorts all songs by score and recommends the top ones.

I kept the main logic the same, but I focused more on how weights affect the results and how the system behaves with different users.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  


The dataset has a small number of songs.

It includes different genres like lofi, pop, rock, classical, hip-hop, and more. It also includes moods like chill, energetic, and others.

I added some data.

A lot of musical taste is missing. Some genres and moods only have one song, and there are gaps in energy levels.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear preferences, like lofi or high-energy listeners.

It does a good job matching the “vibe” when the dataset has similar songs.

Energy and acousticness together help separate chill vs. intense music pretty well.

In many cases, the recommendations made sense based on the user profile.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system prioritizes genre too much because of the +2.0 weight. This creates a filter bubble, especially when a genre only has one song.

It ignores features like danceability and tempo, so some users are not well represented.

Some moods only have one song, so the system can’t recommend variety for those users.

The dataset is uneven, so some users get better recommendations than others.

## Reflection.md for Phase 4 step 5 

Lofi vs. High-Energy Profile
The lofi profile consistently recommended low-energy, high-acousticness songs, while the high-energy profile shifted toward pop, rock, and electronic tracks. This makes sense because energy is one of the stronger weighted numeric features, so changing it has a big impact on results.

Lofi vs. Classical Profile
Even though both profiles prefer high acousticness, the classical profile always ranked the same classical song at the top due to the genre weight. The lofi profile had more variety because there are multiple songs in that genre. This shows how genre weighting + dataset size can create very different experiences.

High-Energy vs. Mid-Energy Profile
The high-energy profile got strong matches with clear top results, while the mid-energy profile had more mixed and lower scores. This is because there are fewer songs in the mid-energy range, so the system can’t find close matches. It highlights how the dataset distribution affects fairness.

Mood-Based Profile (euphoric) vs. General Profile
The euphoric profile always recommended the same song at the top, while a more general mood profile had more variety. This happens because only one song has that mood, so the system can’t really generalize. It ends up overfitting to that single track.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.


I tested multiple user profiles to see how the recommender responds to different preferences. I tried a lofi/chill profile (low energy, high acousticness), a high-energy/EDM-type profile, and a genre-specific profile like classical.

One thing that surprised me was how strongly genre dominated the results. Even when a song matched really well on energy and acousticness, it would still lose to a genre match because of the +2.0 weight. 

Another surprising result was how little impact some features had. For example, acousticness and valence mattered less than I expected, and danceability had no effect at all since it isn’t included in scoring. This made the system feel less accurate for certain types of listeners.


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would add more songs to balance the dataset.

I would include features like danceability and tempo in scoring.

I would lower the genre weight to reduce filter bubbles.

I would also add rules to increase diversity in the recommendations.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  


I learned that recommendation systems are not just about matching things, but also about how you weight features.

It was interesting to see how small changes in weights can completely change results.

This made me realize that real music apps probably deal with a lot of bias and data issues behind the scenes.


## my own reflection 

My biggest learning moment was realizing how much the weights actually matter. Even like making genre worth more, completely changed the recommendations. It showed me that the logic isn’t just about the formula, but about the choices behind it.

AI tools helped me a lot with structuring my ideas and debugging, especially when I wasn’t sure how to design the scoring. But I had to double-check things when it came to reasoning about fairness and bias, because sometimes the suggestions sounded right but didn’t actually match how my system behaved.

What surprised me the most is that even a really simple algorithm can still feel like it’s making “smart” recommendations. Just comparing a few features and sorting results already starts to feel personalized.

If I extended this project, I would add more features like danceability and maybe let users have multiple moods or genres at once. I’d also try to improve diversity so the recommendations don’t feel repetitive.