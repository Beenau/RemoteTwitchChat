# RemoteTwitchChat
Connects to the Twitch.tv API and streams chat messages into a GUI, the terminal, and a log file

Code requires the users log-in name and a authentication token obtainable through twitch to access the API.  

Stream name requires '#streamname' format where all characters should be lowercase

# Simple GUI Display
Created to provided an stream of messages outside the terminal in which all extra information recieved from twitch API is striped away and only the messsage itself remains.  The full content of the twitch respons can be viewed in the chat.log and terminal. Information removed from the GUI display includes the time stamp, user name, and stream name sent back by twitch.

![TwitchChatGUI](https://user-images.githubusercontent.com/73450165/150878483-9886432f-6859-473b-b554-67709625a27b.PNG)
