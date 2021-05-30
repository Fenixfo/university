#Importaciones que se realizan
import socket
import tweepy

#Hashtags que se utilizarán
hashtags=['#OnePiece','#Luffy','#Zoro','#Namy','#Ussop','#Chopper','#Robin','#Franky','#Brook','#Jimbe']
#API y Token de twitter
apikey="Iz5iMwwgbu8K7f6BKk8pkgoQW"
apisecret="avypXpdc1bZl8mIYw85ybo1AWATK6UC5KwGnm8k44cXRlpXGAs"
a3 ="AAAAAAAAAAAAAAAAAAAAAC%2FpOgEAAAAAtxY%2F25Y1NyLo2aNrMPAGM5Z1Jag%3D0pxGty7X7QNurG0fJRy8WSsEAfW3kjW4h1MpKybYk2rBqZatST"
access_token="534573957-WTuz4awU2qTSPxsaMfYWpWKC0aHLZjgVPLSkcUeL"
access_token_secret="w7oloRcTDpqrYiUkQFMducaXBRPVs9DjNPRGIROhPVgEe"

#Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9898))
s.listen()
conn,addr=s.accept()
print(f'conectado con {addr}')

#Funcion
class TwitterListener(tweepy.StreamListener):
    def on_status(self, status):
        diccionario=status.entities['hashtags']
        print(30*'*')
        for hashtag in diccionario:
          if '#'+str(hashtag['text']) in hashtags:
            conn.sendall(bytes(hashtag['text']+'\n',encoding='utf-8'))
            print(hashtag['text'])

#Codigo para accedes
auth=tweepy.OAuthHandler(apikey,apisecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
streamListener = TwitterListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=hashtags)

