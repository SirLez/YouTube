import os
from googleapiclient.discovery import build
# My Channel ID >> UCNI3mQ6wnyBPf1mJRM0JnNQ
# Switch channel ID
channelId = input('channel ID : ')
# API
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Pls peak Your API KEY Here
apiKey = 'API_KEY_HERE'
# Do Not Edit This information
api_service_name = "youtube"
api_version = "v3"
# Parts
context = 'contentDetails'
snip = 'snippet'
# Lists
playListNames = []
playListIds = []
vidIds = []
vidNames = []

# Switch YT Data API Version
YouTube = build(
        api_service_name, api_version, developerKey=apiKey
)

# Get Play Lists
playLists = YouTube.playlists().list(
    part=snip,
    channelId=channelId,
    maxResults=100
)
responseL = playLists.execute()

# Switch The Play List By The USER
for listId in responseL['items']:
    playListNames.append(listId[snip]['title'])
    playListIds.append(listId['id'])
r = 0
for i in range(len(playListIds)):
    print(f"{r} PlayList Name : {playListNames[r]}")
    r = r + 1


def switchS():
    global listSwitchS
    listSwitchS = int(input('\nswitch the video number : '))
    if len(playListIds) - 1 < listSwitchS:
        raise TypeError(f"nope!, the number not in PLAY LISTS try from 0 to {len(playListIds) - 1}")
    global change
    change = input(
        f"\nyou have switched >>> {playListNames[listSwitchS]} <<< do you want to change it? \033[1;33m(y-n) : \033[1;0m"
    )

switchS()
if 'y' in change:
    switchS()
# Get Play Lists Items
playId = playListIds[listSwitchS]
playListItems = YouTube.playlistItems().list(
    part=snip,
    playlistId=playId
)
responseI = playListItems.execute()

# Get Video Info
for item in responseI['items']:
    vidIds.append(item[snip]['resourceId']['videoId'])
    vidNames.append(item[snip]['title'])

# Switch The Video By The USER
r = 0
for i in range(len(vidIds)):
    print(f"{r} video Name : {vidNames[r]}")
    r = r + 1


def switch():
    global listSwitch
    listSwitch = int(input('\nswitch the video number : '))
    if len(vidIds) - 1 < listSwitch:
        raise TypeError(f"nope!, the number not in VIDEOS try from 0 to {len(vidIds) - 1}")
    global change
    change = input(
        f"\nyou have switched >>> {vidNames[listSwitch]} <<< do you want to change it? \033[1;33m(y-n) : \033[1;0m"
    )


switch()
if 'y' in change:
    switch()

# Get The Comments
vidId = vidIds[listSwitch]
comments = YouTube.commentThreads().list(
    part=snip,
    videoId=vidId,
    maxResults=100
)
responseC = comments.execute()

# Print The Comments
for comments in responseC['items']:
    comment = comments[snip]['topLevelComment'][snip]['textDisplay']
    print('\n\n\n',comment)
