import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json


# Set up your credentials
consumer_key='OElJSTRmVlYtamNMSFFYVzg0SUE6MTpjaQ'
consumer_secret='Hm6Gk6FWCVb8gJsUubc-QMm7R7JSzDeYpMQCK5LlzNk4OsOiaP'
access_token ='1782068897794908160-ZDrvFRUGCJJd2hfjoKG95DcNvc4HI8'
access_secret='61gSrFNvbqYKsevrpjjU6pOcbWr6BIdJcBkjbxIeEtnIK'


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket
      print("location 1\n")

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          print("location 2\n")
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
          print("location 3\n")
      return True

  def on_error(self, status):
      print(status)
      print("location 4\n")
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['cricket'])
  print("location 5\n")

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 9915                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )
  print("location 6\n")

  sendData( c )
