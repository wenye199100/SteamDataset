import requests
import json

def get(printProgress=False):
    '''Request reviews from the Steam Web API and return them as a list. This is a blocking call that may take some time, depending on how many reviews there are.\n
    **appid** -- The Steam App ID as a string obtained from the game's store page URL\n
    **progress** -- Set to true to print the progress of each request.
    '''

    def _makeRequest():
        '''Helper function that sends a request to the Steam Web API and returns the response object.\n
        **appid** -- The Steam App ID obtained from the game's Store page URL\n
        **params** -- An object used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
        '''
        response = requests.get(url=ENDPOINT)  # get the data from the endpoint
        return response.json()  # return data extracted from the json response

    ENDPOINT = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
    results = []

    data = _makeRequest()
    done = False

    with open("./products.json", 'w') as json_file:
        json.dump(data, json_file)

    if printProgress:
        print("Found all products.")
    return results