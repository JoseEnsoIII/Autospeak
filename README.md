Autospeak
Autospeak is a Python script that uses the pyttsx library to convert text to speech and read out loud any new messages in a given folder. It is useful for individuals who want to keep track of new messages without having to constantly check their email or messaging apps.

Installation
To use Autospeak, you will need to install the following libraries:

pyttsx: A Python library for text-to-speech conversion. You can install this library using pip: pip install pyttsx
Once you have installed the library, you can download the autospeak.py script and run it in your command line or terminal.

Usage
To use Autospeak, first navigate to the directory where the autospeak.py script is located in your terminal. Then, run the script using the command python autospeak.py. This will start the script and begin monitoring the folder for new messages.

By default, Autospeak monitors the messages folder located in the same directory as the script. You can change the folder being monitored by modifying the FOLDER_PATH variable at the top of the script.

Autospeak uses the pyttsx.init() method to create an instance of the pyttsx.Engine class and set the voice and rate (speed) of the speech. By default, the script uses the en-us voice and a rate of 150 words per minute. You can customize these settings by modifying the VOICE and RATE variables in the script.

When a new message is detected in the monitored folder, Autospeak uses the pyttsx.say() method to convert the message text to speech and play it through the default system audio output device. The script then moves the message to the read_messages folder to indicate that it has been read.

Limitations
Autospeak is a simple script that uses the pyttsx library to read out loud new messages in a given folder. It has several limitations:

The script only monitors a single folder for new messages. It does not support monitoring multiple folders or email accounts.

The script does not provide advanced features such as pause, resume, or stop functionality during speech playback.

The script may not support all voices and languages on all platforms.

License
Autospeak is released under the MIT License. See the LICENSE file for details.
