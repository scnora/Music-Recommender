# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  


The system prioritized genre more than usualy because of the +2.0 weight, especially if the dataset only has one song per genre. This causes there to be a filter bubble where users who like very different genres get the same song recommended everytime, even if another song would be more suiting.The system also ignores features like danceability and tempo, which means users who care about those (like funk or hip-hop listeners) aren’t really being represented in the scoring at all. Another feature that isnt being considered is the moods of the songs. Some moods only have one song in the dataset . The combination of uneven data and weighted scoring makes the system feel unfair depending on what kind of listener you are.


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

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
