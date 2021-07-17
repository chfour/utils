import requests, json

def id2ping(userid):
    return f"<@{userid}>"

class Webhook():
    def __init__(self, url: str, username: str, avatar_url=""):
        self.url = url
        self.username = username
        self.avatar_url = avatar_url

    def get_payload(self, data: dict):
        template = {
            "username": self.username,
            "avatar_url": self.avatar_url
        }
        return {**template, **data}

    def send_raw(self, data: dict):
        return requests.post(self.url, self.get_payload(data))

    def send_message(self, content: str):
        return send_raw({
            "content": content
        })

    def send_mention(self, userid, content: str):
        return self.send_message(id2ping(userid) + " " + content)

if __name__ == "__main__":
    from python_dotenv import load_dotenv
    import os
    load_dotenv()

    wh = Webhook(os.environ["WH_URL"], os.environ["WH_USERNAME"], os.environ["WH_AVATAR"])

    wh.send_message(sys.stdin.read())
