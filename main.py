import os, sys, random, time, json, requests
import uberduck
import tornado.web
import asyncio
with open('config.json', 'r') as handle:
    config = json.load(handle)

apikey = (config["apikey"])
apisecret = (config["apisecret"])
voice_stranger = "linustt"
voice = "Chills" #unused
voice_user = "Chills"
client = uberduck.UberDuck(apikey, apisecret)
voices = uberduck.get_voices(return_only_names = True)

class tts_stranger(tornado.web.RequestHandler):
    def get(self):
        self.write("")
        message = self.get_argument("message")
        print(message)
        client.speak(message[1:-1], voice_stranger, play_sound = True)

class tts_user(tornado.web.RequestHandler):
    def get(self):
        self.write("")
        message = self.get_argument("message")
        print(message)
        client.speak(message[1:-1], voice_user, play_sound = True)

def make_app():
    return tornado.web.Application([
        (r"/tts_stranger", tts_stranger),
        (r"/tts_user", tts_user),
    ])

async def main():
    app = make_app()
    app.listen(1337)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

