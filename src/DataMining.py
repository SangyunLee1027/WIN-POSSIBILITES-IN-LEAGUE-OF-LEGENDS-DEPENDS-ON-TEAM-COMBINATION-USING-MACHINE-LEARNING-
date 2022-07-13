import pandas as pd
from riotwatcher import LolWatcher, ApiError


def arrdata(m):
    tempdata = {}
    tempdata['top1'] = ''
    tempdata['jungle1'] = ''
    tempdata['mid1'] = ''
    tempdata['bottom1'] = ''
    tempdata['support1'] = ''
    tempdata['top2'] = ''
    tempdata['jungle2'] = ''
    tempdata['mid2'] = ''
    tempdata['bottom2'] = ''
    tempdata['support2'] = ''
    win = False
    for i in range(10):
        if m['info']['participants'][i]['individualPosition'] == 'TOP':
            if m['info']['participants'][i]['teamId'] == 100:
                tempdata['top1'] = m['info']['participants'][i]['championName']
                if m['info']['participants'][i]['win'] == True:
                    win = True
            else:
                tempdata['top2'] = m['info']['participants'][i]['championName']
        if m['info']['participants'][i]['individualPosition'] == 'JUNGLE':
            if m['info']['participants'][i]['teamId'] == 100:
                tempdata['jungle1'] = m['info']['participants'][i]['championName']
            else:
                tempdata['jungle2'] = m['info']['participants'][i]['championName']
        if m['info']['participants'][i]['individualPosition'] == 'MIDDLE':
            if m['info']['participants'][i]['teamId'] == 100:
                tempdata['mid1'] = m['info']['participants'][i]['championName']
            else:
                tempdata['mid2'] = m['info']['participants'][i]['championName']
        if m['info']['participants'][i]['individualPosition'] == 'BOTTOM':
            if m['info']['participants'][i]['teamId'] == 100:
                tempdata['bottom1'] = m['info']['participants'][i]['championName']
            else:
                tempdata['bottom2'] = m['info']['participants'][i]['championName']
        if m['info']['participants'][i]['individualPosition'] == 'UTILITY':
            if m['info']['participants'][i]['teamId'] == 100:
                tempdata['support1'] = m['info']['participants'][i]['championName']
            else:
                tempdata['support2'] = m['info']['participants'][i]['championName']
    if win == True:
        tempdata['win'] = 1;
    else:
        tempdata['win'] = 0;
    return tempdata


api_key = 'RGAPI-a7989eef-1d46-4246-955a-890c37e8e38e'
watcher = LolWatcher(api_key)

lists = ['Ablazeolive','Shrimp Cpt', 'ling xiao lu', 'wechat Hc9999na','tang yuan ya']
my_region = 'na1'

data = []

for n in lists:
    sample = watcher.summoner.by_name(my_region, n)
    sample_match = watcher.match.matchlist_by_puuid(my_region, sample['puuid'])
    for c in range(20):
        last_match = sample_match[c]
        match_detail = watcher.match.by_id(my_region, last_match)
        if match_detail['info']['gameMode'] == 'CLASSIC':
            data.append(arrdata(match_detail))

df = pd.DataFrame(data)
df.to_csv('./Data/MatchData.csv', mode='a', index=False, header=True)