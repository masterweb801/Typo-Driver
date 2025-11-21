from sys import exit
from os import getenv
from ctypes import windll
from pyperclip import copy
from dotenv import load_dotenv
from pyautogui import press, hotkey
from flask import Flask, request, jsonify
from socket import gethostbyname, gethostname, socket, AF_INET, SOCK_STREAM
from pathlib import Path


env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)
token = getenv("SECRET")
port = getenv("PORT")
host = gethostbyname(gethostname())

app = Flask(__name__)


def check_single_instance(port: int):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
    except OSError:
        windll.user32.MessageBoxW(0, "App is already running!", "Warning", 0)
        exit(0)

    return s


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
    lock_socket = check_single_instance(int(port))

    from waitress import serve

    print(f"Server Started On: http://{host}:{port}")
    serve(app=app, host=host, port=port)
