# Typo Driver

Typo Driver is the Windows desktop companion for [Typo](https://github.com/masterweb801/Typo). It receives text and key commands from the Android app over the local network and sends them to the active desktop application.

## How it works

1. Start Typo Driver on the Windows computer.
2. Configure the connection details and shared authorization token in the local environment.
3. Connect the Typo Android app to the desktop receiver over the same network.
4. Text and supported key commands are delivered to the computer.

The current receiver exposes a Flask endpoint at /send_message. Requests must include the matching auth token and a non-empty message. The special messages <-RETURN-> and <-BACKSPACE-> trigger the corresponding keys; other messages are pasted using the system clipboard.

## Technology

- Python
- Flask
- PyAutoGUI
- Pyperclip
- python-dotenv
- Waitress (production WSGI server)

## Requirements

- Windows
- Python 3
- The [Typo Android app](https://github.com/masterweb801/Typo)

## Setup

1. Clone or download this repository.
2. Install the Python dependencies with pip install -r requirements.txt.
3. Create a .env file beside Typo.py:

       SECRET=replace_with_a_long_random_token
       PORT=5000

4. If Waitress is not installed by the dependency file, install it separately with pip install waitress.
5. Run the receiver with python Typo.py.

Keep the Android app and desktop receiver configured with the same secret. Do not commit the .env file or share the token publicly.

## Security and network notes

- Use Typo Driver only on a trusted local network.
- Choose a long, random authorization token.
- Restrict the receiver's network access with Windows Firewall.
- The receiver can type or paste text into the currently focused application. Keep it stopped when it is not in use.

## Related project

- [Typo for Android](https://github.com/masterweb801/Typo)

---

Built by [Mobashshirul Karim](https://github.com/masterweb801).
