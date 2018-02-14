from emotions import Emotion

URL = "https://api.telegram.org/bot344998733:AAF0R901Ilq43PH-MSYAnoDHMYrh5yaK3eg/getUpdates"

# Emotion = {'angry': "( ` ω ´ )", 'cool': "(◕‿◕)", 'positive': "٩(◕‿◕｡)۶", 'happy': "(〃＾▽＾〃)"}


def handle_message(message, nickname="user"):
    key = ''
    key = message
    return Emotion.get(key, 'Смайлика не существует :(')


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
