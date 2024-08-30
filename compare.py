import json

# replace with path
with open('/Users/agastya/InstaRatio/following.json', 'r') as f:
    following_data = json.load(f)
with open('/Users/agastya/InstaRatio/followers.json', 'r') as f:
    followers_data = json.load(f)

following_usernames = {account['string_list_data'][0]['value'] for account in following_data['relationships_following']}
followers_usernames = {account['string_list_data'][0]['value'] for account in followers_data}

not_following_back = following_usernames - followers_usernames
not_following = followers_usernames - following_usernames

print(f"Accounts not following you back ({len(not_following_back)}):")
for username in sorted(not_following_back):
    print(username)

print('---')

print(f"Accounts you are not following back ({len(not_following)}):")
for username in sorted(not_following):
    print(username)
