import os
import feedparser
import playsound

feeds_directory = "feeds"
downloads_directory = "downloads"

print("Listing all feeds...")

# List all files in the feeds directory
feeds = os.listdir(feeds_directory)

# Print the title of each feed
for index, i in enumerate(feeds, start=1):
  print(f"[{index}] {feedparser.parse(f'{feeds_directory}/{i}')['feed']['title']}")

# Ask the user to select a feed
feed_index = int(input("Select a feed: ")) - 1
feed = feeds[feed_index]

# Parse the feed
parsed_feed = feedparser.parse(f"{feeds_directory}/{feed}")

# List all episodes
for index, i in enumerate(parsed_feed.entries, start=1):
  print(f"[{index}] {i['title']}")

# Ask the user to select an episode
episode_index = int(input("Select an episode: ")) - 1
episode = parsed_feed.entries[episode_index]

# Print the episode title and description
print(f"Title: {episode['title']}")

# Download the episode to the downloads directory
os.system(f"wget {episode['enclosures'][0]['href']} -O {downloads_directory}/episode.mp3")

# Play the episode with playsound
playsound.playsound(downloads_directory + "/episode.mp3", True)