from flask import Flask,render_template
from pymongo import MongoClient
import json
client = MongoClient()
db = client.tweets
modi=db.narendra_modi
kejriwal=db.kejriwal

app = Flask(__name__)

modi_tweet_locations={}
modi_hastgas={}
trending={}
retweet_modi_count=0
tweet_modi_count=0
favorite_count=0
image_count=0
video_count=0
text_count=0
for i in modi.find({}):

        tweet_modi_count+=1
        if "media" in i['entities']:
                if i['entities']['media'][0]['type']=="photo":
                        image_count+=1
                elif    i['entities']['media'][0]['type']=="video":
                        video_count+=1
        if "extended_tweet" in i:
                if "media" in i['extended_tweet']:
                        if i['extended_tweet']['media'][0]['type']=="photo":
                                image_count+=1
                        elif    i['entities']['media'][0]['type']=="video":
                                video_count+=1
        else:
                text_count+=1
        if "retweeted_status" in i:
                retweet_modi_count+=i['retweeted_status']['retweet_count']

                favorite_count=favorite_count+i['retweeted_status']['favorite_count']

        if i['user']['time_zone'] not in modi_tweet_locations and i['user']['time_zone']!="null":

                modi_tweet_locations[i['user']['time_zone']]=1
        else:
                modi_tweet_locations[i['user']['time_zone']]=modi_tweet_locations[i['user']['time_zone']]+1

        if i['entities']['hashtags']!=[]:
                access_hash=i['entities']['hashtags'][0]['text']
                if access_hash not in trending:
                        trending[access_hash]=1
                else:
                        trending[access_hash]=trending[access_hash]+1
c=sorted(trending, key=trending.get,reverse=True)
d=[]
flag=0
i=0
arvind_tweet_locations={}
retweet_arvind_count=0
tweet_arvind_count=0
for j in kejriwal.find({}):
        tweet_arvind_count+=1
        # retweet_arvind_count+=i['retweet_count']
        favorite_count=favorite_count+j['favorite_count']
        if j['user']['time_zone'] not in arvind_tweet_locations:
                arvind_tweet_locations[j['user']['time_zone']]=1
        else:
                arvind_tweet_locations[j['user']['time_zone']]=arvind_tweet_locations[j['user']['time_zone']]+1
tweets_Total=tweet_arvind_count+tweet_modi_count
print("arvind count"+str(tweet_arvind_count))
print(">>>>>>>"+str(tweets_Total))
retweet_total=retweet_modi_count+retweet_arvind_count
print(">>>>>>>"+str(retweet_total))
# print modi_tweet_locations

@app.route('/')
def hello_world():
    return render_template('index.html',tweet_arvind_count=tweet_arvind_count,tweet_modi_count=tweet_modi_count,
        tweets_Total=tweets_Total,retweet_total=retweet_total,favorite_count=favorite_count,m_location=json.dumps(modi_tweet_locations),trending=d,image_count=image_count,text_count=text_count)

if __name__ == '__main__':
        app.run(debug=True,use_reloader=True)








