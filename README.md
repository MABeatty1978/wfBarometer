# wfBarometer

This program utilizes the tempest api to get your weather station's barometric trend.  It then utilizes an HTTP put to send the request plus a "trend" parameter. You can use this to activate any variety of events.  In my case, I'm running this via crontab every minute to send the status to SharpTools.  I have a SharpTools rule that reads the parameter and turns on a "rising" or "falling" virtual switch, or turns the both off if steady.  I have these switches displayed (using ActionTiles) on my wall mounted home automation tablets for a barometric indication that is easy to see in the house.

All of the variables that include "secrect" data such as tokens and authorization are sourced in using an .env file.  You will need to create a .env file in the same directory as this program with the data required.
