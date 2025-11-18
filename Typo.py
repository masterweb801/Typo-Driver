from os import getenv
from pyperclip import copy
from dotenv import load_dotenv
from pyautogui import press, hotkey
from flask import Flask, request, jsonify
from socket import gethostbyname, gethostname


load_dotenv()
app = Flask(__name__)
token = getenv("SECRET")


@app.route("/send_message", methods=["POST"])
def handle_message():
    try:
        data = request.get_json()
        auth = data.get("auth", "")

        if auth == token:
            message = data.get("message", "")

            if message:
                if message == "<-RETURN->":
                    press("enter")
                    print("Pressed Enter")

                elif message == "<-BACKSPACE->":
                    press("backspace")
                    print("Pressed Backspace")

                else:
                    copy(message)
                    hotkey("ctrl", "v")
                    print("Message written")

                return (
                    jsonify(
                        {
                            "status": "success",
                            "message": "Message received and typed.",
                        }
                    ),
                    200,
                )
            else:
                print("Got Empty Message!")
                return (
                    jsonify({"status": "error", "message": "No message provided."}),
                    400,
                )
        else:
            print("Authorization Error!")
            return (
                jsonify({"status": "error", "message": "Authorization Error!"}),
                403,
            )
    except Exception as e:
        print(str(e))
        return (jsonify({"status": "error", "message": str(e)}), 500)


if __name__ == "__main__":
    from waitress import serve

    print("Server Started ...")
    serve(app=app, host=gethostbyname(gethostname()), port=6969)
