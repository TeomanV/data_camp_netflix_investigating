#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#import csv file with csv reader
netflix_df = pd.read_csv("netflix_data.csv")

#make subset for get movies
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

#for get only 90s movies we need to subset again
movies90s = netflix_movies[(netflix_movies["release_year"] >= 1990) & (netflix_movies["release_year"] < 2000)]

#show in histogram
plt.hist(movies90s["duration"])
plt.title('All Movies in the 90s')
plt.xlabel('Minutes of movies')
plt.ylabel('Number of Movies')
plt.show()

#subset action movies
action_movies90s = movies90s[movies90s["genre"] == "Action"]

#subset which is fewer than 90 minutes
actionfewer = action_movies90s[action_movies90s["duration"] < 90]
print(actionfewer.loc[:, ["title", "duration"]].to_string(index=0))

# Bar grafiği oluşturuyoruz
plt.figure(figsize=(10, 6))
plt.bar(actionfewer["title"], actionfewer["duration"])
plt.title('Duration of Action Movies in the 90s (Less than 90 minutes)')
plt.xlabel('Movies')
plt.ylabel('Duration (minutes)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
