from RiotAPI import RiotAPI
import time

'''
Function that fetches the data to test using multiple api keys.
The three parameters are a list of parameter keys, an integer for the maximum
requests in a given time interval, and the maximum amount of time in minutes
for the requests interval.
'''
def fetchData(keyList, maxRequests, maxTime):
    # variable that keeps track of the total request count
    requestCount = 0
    # beginning of function execution
    startTime = time.time()
    # number of apikeys
    keyCount = len(keyList)
    # calculate the amount of time needed between each REST call
    interval = ((maxTime * 60.0) / maxRequests) / keyCount
    print(interval)
    # list containing RiotAPI objects
    apiList = [RiotAPI(key) for key in keyList]
    # get the summoner id list for master tier
    summonerIdList = apiList[requestCount % keyCount].getSummonerListFromMasterTier()
    requestCount += 1
    time.sleep(interval)
    # get the account id for each summoner id
    accountIdList = []
    count = 0
    for summonerId in summonerIdList:
        if count > 20:
            break
        accountIdList.append(apiList[requestCount % keyCount].getAccountIdFromSummonerId(summonerId))
        requestCount += 1
        time.sleep(interval)
        count += 1
    # get a matchlist for each accountIdList
    matchListDict = {}
    for accountId in accountIdList:
        matchListDict[accountId] = apiList[requestCount % keyCount].getMatchListFromAccountId(accountId)
        requestCount += 1
        time.sleep(interval)
    # get the match info for each match
    matchInfoDict = {}
    for account in matchListDict:
        for match in matchListDict[account]:
            matchInfoDict[account] = [match, apiList[requestCount % keyCount].getMatchInfoFromMatchId(match)]
            requestCount += 1
            time.sleep(interval)

    endTime = time.time()

    print(matchInfoDict)
    print("Duration: " + str(endTime - startTime))
    print("Requests sent: " + str(requestCount))

def testSingleKey():
    apiList = ["key number 1]
    maxRequests = 500
    maxTime = 10
    fetchData(apiList, maxRequests, maxTime)

def testDoubleKey():
    apiList = ["key number 1", "key number 2"]
    maxRequests = 500
    maxTime = 10
    fetchData(apiList, maxRequests, maxTime)
