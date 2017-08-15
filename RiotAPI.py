import requests

'''
Class that is used to make calls out to the Riot Games API.
For the purpose of this draft only the RANKED_SOLO_5x5 is concerned.
'''
class RiotAPI:

    def __init__(self, key):
        self.key = key
        self.requestCounter = 0

    def getRequestCounter():
        return self.requestCounter

    '''
    Pull back all players in a tier
    '''
    def getSummonerListFromMasterTier(self):
        # url for HTTP GET Request
        url = "https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5";
        # parameters for the HTTP GET Request
        params = {"api_key":self.key}
        # function that handles the HTTP GET REQUEST
        response = requests.get(url=url, params=params).json()
        # increment the counter by 1
        self.requestCounter += 1
        # list that will collect all of the summoner IDs
        summonerIds = []
        # loop through each entry and collect all summoner IDs
        for entry in response["entries"]:
            summonerIds.append(entry["playerOrTeamId"])
        # return the list of summoner IDs
        return summonerIds

    '''
    Pull back an account id using the summoner ids
    '''
    def getAccountIdFromSummonerId(self, summonerId):
        # url for HTTP GET Request
        url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/" + str(summonerId);
        # parameters for the HTTP GET Request
        params = {"api_key":self.key}
        # function that handles the HTTP GET REQUEST
        response = requests.get(url=url, params=params).json()
        # increment the counter by 1
        self.requestCounter += 1
        # return the account id
        return response["accountId"];

    '''
    Pull back a list of matches for a particular account id
    '''
    def getMatchListFromAccountId(self, accountId):
        # url for HTTP GET Request
        url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/"+str(accountId)+"/recent";
        # parameters for the HTTP GET Request
        params = {"api_key":self.key}
        # function that handles the HTTP GET REQUEST
        response = requests.get(url=url, params=params).json()
        # increment the counter by 1
        self.requestCounter += 1
        # list that will collect all of the match IDs
        matchIds = []
        # loop through each entry and collect all match IDs
        for entry in response["matches"]:
            matchIds.append(entry["gameId"])
        # return the list of match IDs
        return matchIds

    '''
    Pull back a JSON containing match info from a match id
    '''
    def getMatchInfoFromMatchId(self, matchId):
        # url for HTTP GET Request
        url = "https://na1.api.riotgames.com/lol/match/v3/matches/"+str(matchId);
        # parameters for the HTTP GET Request
        params = {"api_key":self.key}
        # function that handles the HTTP GET REQUEST
        response = requests.get(url=url, params=params).json()
        # increment the counter by 1
        self.requestCounter += 1
        # return the account id
        return response;
