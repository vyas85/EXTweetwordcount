import tweepy

consumer_key = "2NdkFghWXtdbk9oJuf2AIN5WG";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "euyBjnJoaAqKLFsBxWD64fHqhG7aA4Kv7UAQVH2aoSvKxSSb4M";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "798024904486420480-J5FpZvbPjwaNntcCBVVltAfpDsWcwYi";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "ahlKgnIW9vKqo2EkE4ErF9nPXue3XV9lOuyf9SK26ZZLj";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



