## Reviews Sourcing and Explanation

I created my "easy" test set by modifying real, existing reviews from the IMDB website. Generally, I took the opening few sentences/paragraphs from each review. Below are the 6 "easy" reviews along with a brief explanation as to why they were chosen.

### Easy Reviews:

**Positive**  
1. **"Wow, this was fantastic! As I was watching it, I asked myself, 'Is this the best animated movie I've ever seen?' I think the answer is 'yes.'"**

   Enthusiastic and exclamatory language such as "Wow," "fantastic," and "yes" make it an obviously positive review. These are also very common words likely to be found in many other positive reviews.

2. **"Yeah, I must admit, I love this movie. Which is nothing to be ashamed of; great movie, great directing, great set, great scale, great canvas, great story."**

   The repeated use of "great," which the model values highly as a positive feature, makes this a straightforward classification.

3. **"This is the finest movie I have ever seen of the drama kind; it has everything to make an excellent movie. All the actors play an outstanding role."**

   This is a genuine endorsement of the movie, shown through phrases like "finest movie" and "outstanding role." There is no attempt at sarcasm, so the model is very unlikely to be incorrect.

**Negative**  
1. **"I have no idea how anyone could like this dull, uninspiring movie. It was very, very predictable. The leading actress had no talent."**

   Due to n-grams being included in the feature list, a phrase like "no talent" will be identified as negative along with other strong criticisms like "dull" and "uninspiring."

2. **"This movie is probably one of the worst movies I have ever seen. Don't waste your time watching this. I almost turned this movie off watching it."**

   There is no ambiguity in this review. Hyperbolic negative language like "worst" and "waste" make it easy to classify.

3. **"If you want a quick and easy way to punish your kids, take them to see this film. This overlong and boring movie will put them to sleep."**

   Although there is slight sarcasm in this review, the negative connotations behind "punish," "boring," and "overlong" remove any uncertainty.

---

I wrote my own "adversarial" test set. My aim was to create reviews that the model would classify incorrectly due to sarcasm, ambiguity, or unfamiliarity with the language.

### Adversarial Reviews:

**Positive**  
1. **"I was dreading watching this movie as I had been told the acting was awful and the plot was confusing. However, having watched it myself, I completely disagree. Those reviews were absolute nonsense."**

   Initially, negative language is used to describe the writer's expectations (e.g. "dreading," "awful"). However, even when they express their own positive sentiment toward the film, it is through criticizing other negative reviews. The further use of "disagree" and "nonsense" compounds the false negative sentiment the model is likely to detect.

2. **"I wanted to turn this film off from the moment it began. It was a horrible and unsettling experience, exactly how a horror movie should be. Despite the awful fear I felt, I couldn’t look away."**

   As horror movies aim to evoke emotions like fear and anxiety, certain words such as "unsettling" and "awful" lose their usual negative sentiments. The model is unlikely to pick up on these becoming desirable traits in certain genres.

3. **"I usually hate the lead actor but his performance wasn’t a complete disaster this time around. I was shocked that he didn’t totally ruin the film and it was actually quite enjoyable."**

   "Hate" and "disaster" are typically associated with negative sentiments, but the writer's admission that the film exceeded their expectations and was "quite enjoyable" creates ambiguity and uncertainty for the model.

**Negative**  
1. **"For a horror film, it had me laughing out loud from start to finish—truly a unique experience for the genre."**

   This review describes a horror movie that was hilariously bad. Of course, it is not a horror film's intention to make the audience laugh. The model would not be familiar with the alternative use of some prominent features, considering "laughing" and "unique" are typically found in positive reviews.

2. **"What a delightful waste of time! I love sitting through a three-hour film that goes nowhere. I’m looking forward to the sequel already!"**

   I would not expect my model to detect the sarcasm in this review. Positive-sounding language such as "love" and "delightful" is used to express distaste for the film.

3. **"Almost everything about my day at the cinema was brilliant; the popcorn was lovely, the seats were fantastic, and the tickets were great value. The film itself though, the less said the better."**

   Here, positive language is used to describe elements not relating explicitly to the film itself. Later, there is an abrupt shift to negative sentiments about the movie, but the use of a euphemism that the model is not familiar with means it is unlikely to be picked up on.
