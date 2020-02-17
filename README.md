# Steam Dataset Crawler
The dataset in "Game Recommendation based on Dynamic Graph Convolutional Network"

## Dataset

### Dataset case
The file contain the reviews of app 535230.
![Screenshot](https://raw.githubusercontent.com/Anonymous-code-repo/CGR/master/other/1.png)

### Full Dataset
There is the [Full Dataset](https://mega.nz/#!AvhH3C4R!m8cOY5_AIey-0X2UYrYEUzKFA7-hCMfWSSV5D7g4zW8) link in mega.nz

### Structure
```Python
#for each review
{
    'recommendationid': str # The unique id of the recommendation
    'author': {
        'steamid': str # the user’s SteamID
        'num_games_owned': int # number of games owned by the user
        'num_reviews': int #n umber of reviews written by the user
        'playtime_forever': int # lifetime playtime tracked in this app
        'playtime_last_two_weeks': int # playtime tracked in the past two weeks for this app
        'last_played': int # time for when the user last played
    }
    'language': str # language the user indicated when authoring the review
    'review': str # text of written review
    'timestamp_created': int # date the review was created (unix timestamp)
    'timestamp_updated': int # date the review was last updated (unix timestamp)
    'voted_up': bool # true means it was a positive recommendation
    'votes_up': int # the number of users that found this review helpful
    'votes_funny': int # the number of users that found this review funny
    'weighted_vote_score': int # (beta) value not used
    'comment_count': int # number of comments posted on this review
    'steam_purchase': bool # true if the user purchased the game on Steam
    'received_for_free': bool # true if the user checked a box saying they got the app for free
    'written_during_early_access': bool # true if the user posted this review while the game was in Early Access
}
```

```python
#for each app follow as https://store.steampowered.com/api/appdetails/?appids=683320
{
    'data':{
    'names': str # game name
    'steam_appid': int # game id
    'required_age': int # required age
    'is_free': bool # free game or not
    'controller_support': str # support controller or not（full,part,no）
    'dlc': dict # the downable content
    'detailed_description': str # detailed decription of the game
    'about_the_game': str 
    'shor_description': str 
    'supported_languages' : list # the supported laguages
    'reviews': str # the review of some media
    'header_image': url 
    'website': url # offical website
    'pc_requirements': dict # windows requirements
    'mac_requirements': dict # mac requirements
    'linux_requirements': dict # linuxrequirements
    'legal_notice': str # copyright
    'developers': [] # developers（maybe more than 1）
    'publushers': [] # publushers（maybe more than 1）
    'price_overview': dict # price over the region
    'packages': [] # dlc list 
    'packages_groups': dict # dlcs bundles
    'platforms':{
        'windows': true,
        'mac': true,
        'linux': false
        } # platforms
    'metacritic':{
        'score': int
        'url': url
        } # metacritic score
    'categories': [{'id': int, 'description': 'single-player'},{},...] [] # game categories
    'genres': [{'id': int, 'description': 'Indie'},{},...] # game styles
    'tag': [] # tagged by users
    'screenshots': [{'id': int, 'path_thumbnail': url, 'path-full': url},{},...] # screenshots in game
    'movies': [{'id': int, 'name': str, 'thumbnail': url, 'webm': dict, 'highlight': bool},{},...] # pv of the game
    'recommendations': int # the review number of the game
    'achievements': dict # achievements in game
    'release_date': { 'coming_soon': bool, 'date': str } # release date
    'support_info': dict # extra support information of the game
    'background': url # background image
    }
}
```

## Requirements

- Python 3.6
- numpy 1.14


## Project Structure

```

    └── Crawler                    # Crawler folder
        ├── steam_products.py      # Get all the products information on steam
        ├── steam_reviews.py       # Get all the reviews of one app
        └── main.py                # Main files    

```


## Usage

1. Install all the required packages

2. Run python steam_products.py

3. Run python main.py




