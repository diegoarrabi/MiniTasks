import os


folder_path = "/Users/diegoibarra/Media/TV Shows/The Legend of Korra"


all_seasons = os.listdir(folder_path)

for season in all_seasons:
    if season.startswith("."):
        continue
    if season[-2].isdigit():
        season_number = 10 + int(season[-1])
    else:
        season_number = int(season[-1])

    season_episodes = os.listdir(os.path.join(folder_path, season))

    for episode in season_episodes:
        if episode.startswith("."):
            continue
        episode_metadata = f"S{season_number:0>2}E"
        file_name = episode_metadata + episode

        old_name = os.path.join(folder_path, season, episode)
        new_name = os.path.join(folder_path, season, file_name)
        if os.path.isdir(old_name):
            continue
        os.rename(old_name, new_name)
