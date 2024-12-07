import socket
import pyautogui
import pyperclip
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/send_message", methods=["POST"])
def handle_message():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if message:
            print(f"Received message: {message}")

            pyperclip.copy(message)
            pyautogui.hotkey("ctrl", "v")

            return (
                jsonify(
                    {"status": "success", "message": "Message received and typed."}
                ),
                200,
            )
        else:
            return jsonify({"status": "error", "message": "No message provided."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), port=6969, debug=True)
