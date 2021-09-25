{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  },
  "orig_nbformat": 2
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import speech_recognition as sr \n",
    "\n",
    "mic_name = \"USB Device 0x46d:0x825: Audio (hw:1, 0)\"\n",
    "\n",
    "sample_rate = 48000\n",
    "\n",
    "chunk_size = 2048\n",
    "r = sr.Recognizer() \n",
    "\n",
    "mic_list = sr.Microphone.list_microphone_names() \n",
    "\n",
    "for i, microphone_name in enumerate(mic_list): \n",
    "\tif microphone_name == mic_name: \n",
    "\t\tdevice_id = i \n",
    "\n",
    "with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source: \n",
    "\t \n",
    "\tr.adjust_for_ambient_noise(source) \n",
    "\tprint (\"Say Something\")\n",
    "\t#listens for the user's input \n",
    "\taudio = r.listen(source) \n",
    "\t\t\n",
    "\ttry: \n",
    "\t\ttext = r.recognize_google(audio) \n",
    "\t\tprint (\"you said: \" + text )\n",
    "\t\n",
    "\t#error occurs when google could not understand what was said \n",
    "\t\n",
    "\texcept sr.UnknownValueError: \n",
    "\t\tprint(\"Google Speech Recognition could not understand audio\") \n",
    "\t\n",
    "\texcept sr.RequestError as e: \n",
    "\t\tprint(\"Could not request results from Google Speech Recognition service; {0}\".format(e)) \n"
   ]
  }
 ]
}