# camera-detector
AI-Powered Smart Parking & Prohibited Zone Detector

An AI-powered smart system for detecting vehicles parked in restricted areas (such as disabled parking spaces or in front of gates) and sending instant alerts to a Telegram bot.

 Features
- **Accurate Vehicle Detection:** Uses the lightweight and fast **YOLO11** model to identify cars, trucks, and buses.

- **Restricted Zone Identification (ROI):** Allows drawing a specific zone (polygon) within the camera frame for monitoring only.

- **Instant Telegram Alerts:** The bot sends an instant notification to the administrator whenever a vehicle enters the restricted zone.

- **Anti-Spam Prevention:** The code includes a timer to prevent duplicate messages for the same parked vehicle.

- **Docker Ready:** The entire project is packaged within Docker for easy operation on any operating system (Linux/Windows).

 Tools Used (Tech Stack)
- Python 3.11
- OpenCV (Video Processing and Graphics)
- Ultralytics YOLO11 (Artificial Intelligence and Monitoring)
- Telegram Bot API (Alert System)
- Docker & Docker Compose (Isolated Environment)
---------------------------------------------------------------------------------------------------------------------------------------------------------
How to Run

Firstly: Setting up a Telegram bot and obtaining its token and chat ID 
1. Steps to Create the Bot and Obtain the Token

* Open the Telegram app and search for the official account of **`@BotFather`** (make sure there's a blue verification badge next to the name).

* Tap the **Start** button to activate the chat with them.

* Send them the following command to create a new bot:

/newbot

* You will now be asked to choose a name for the bot. Write any name you like 

* Next, you will be asked to choose a username for the bot. It must be in English and end with the word `bot`.

* Once you choose an available username, you will receive a congratulatory message containing the **HTTP API Token**, which is a long string of numbers and letters (similar to this: `8949424119:AAEIuo1...`). Copy it to save it in your code.


2. Steps to Activate the Bot and Get the Chat ID

The Chat ID is the unique identifier for your personal account, allowing the bot to recognize which user it is sending notifications to.

* **Very Important First Step:** Click on the bot's link that you just created (ending in `_bot`) and click the **Start** button. Send it a welcome message to activate it.

* Now, search Telegram for a bot to extract IDs, such as **`@userinfobot`**.

* Click the **Start** button inside the bot.

* You will receive an immediate reply containing your personal information. You will find a long number next to the words **`Id:`** (similar to this: `1111111111`).

* This number is your Chat ID, which you enter into the code so the bot can message you directly.
---------------------------------------------------------------------------------------------------------------------------------------------------------
Secondly: put your vedio file and name it "Vedio.mp4"
---------------------------------------------------------------------------------------------------------------------------------------------------------
Then: Running it on your laptop 
1. Install the libraries:

```bash

pip install -r requirements.txt
2. Place your video file, named video.mp4, in the project folder.

3. Run the code:
```bash

python3 main.py
or 
Using Docker Compose:
```bash

docker compose up --build