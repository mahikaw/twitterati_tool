from flask import Flask,render_template
from pymongo import MongoClient
client = MongoClient()
db = client.tweets
modi=db.narendra_modi
kejriwal=db.kejriwal

app = Flask(__name__)

modi_tweet_locations={}
modi_hastgas={}
retweet_modi_count=0
tweet_modi_count=0
favorite_count=0
for i in modi.find({}):

	tweet_modi_count+=1

	retweet_modi_count+=i['retweet_count']

	favorite_count=favorite_count+i['favorite_count']

	if i['user']['time_zone'] not in modi_tweet_locations:
		# if(i['user']['time_zone'])=='Eastern Time (US & Canada)':
		# 	modi_tweet_locations['Unites states']=1
		# else:
		modi_tweet_locations[i['user']['time_zone']]=1
	else:
		modi_tweet_locations[i['user']['time_zone']]=modi_tweet_locations[i['user']['time_zone']]+1

	# print("entities data\n"+str(i['entities']))
	# print("^^^^^^^^"+i['entities']['hashtags'][0]['text'])
	# if i['entities']['hashtags'] not in modi_tweet_locations:
	# 	 modi_tweet_locations[i['user']['time_zone']]=1
	# else:
	# 	modi_tweet_locations[i['user']['time_zone']]=modi_tweet_locations[i['user']['time_zone']]+1


print("LOCATIONS"+str(modi_tweet_locations))

arvind_tweet_locations={}
retweet_arvind_count=0
tweet_arvind_count=0
for j in kejriwal.find({}):
	tweet_arvind_count+=1
	retweet_arvind_count+=i['retweet_count']
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


@app.route('/')
def hello_world():
    return render_template('index.html',tweet_arvind_count=tweet_arvind_count,tweet_modi_count=tweet_modi_count,
    	tweets_Total=tweets_Total,retweet_total=retweet_total,favorite_count=favorite_count,m_location=modi_tweet_locations)

if __name__ == '__main__':
	app.run(debug=True,use_reloader=True)