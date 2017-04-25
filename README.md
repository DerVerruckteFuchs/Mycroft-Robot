# [GROUP NAME]'s CS 101 project
The project consists the usage of an iRobot and Mycroft deployed on a Raspberry Pi.
Mycroft will take a variety of commands and in turn send necessary commands to the iRobot via pySerial.

## Getting up and running
* 	Mycroft runs on a variety of devices
	- Raspberry Pi
	- Linux based PCs
	- Android
	- Also available via Ubuntu snaps and docker 


## Installation
- Raspberry Pi:
	
	> Picroft Installation image [get it here](https://github.com/MycroftAI/enclosure-picroft)

	> [Instructions](https://github.com/MycroftAI/enclosure-picroft/wiki/Gettting-Started-Guide) for putting Picroft onto an SD card
	
	> Picroft automatically starts apt-get update and apt-get upgrade to update mycroft-core, mimic, and msm to the latest version.

	> It is possible to disable the automatic update if it is slow, but it is recommended to keep mycroft-core, mimic, and msm up to date.
	
	> To disable the automatic update on boot, comment out all of the lines related to apt-get in /home/pi/auto_run.sh

	> You can also configure audio output in /home/pi/auto_run.sh. By default the audio output uses the audio jack.

	> It can be switched to HDMI output if desired. At the top of auto_start.sh uncomment the amixer line for HDMI,

	> then comment out the one for the audio jack.

	
- Linux PCs

	
	> You will need a mycroft-core and mimic for text-to-speech

	> Instructions for installing mycroft-core from [GitHub](https://github.com/MycroftAI/mycroft-core)

	> Instructions for installing mimic from [GitHub](https://github.com/MycroftAI/mimic)

	> Arch has both mycroft-core and mimic in the AUR. Don't confuse mycroft-core with mycroft, both packages are very different.
	> If you get a permissions error trying to start Mycroft, you may need to add yourself to the mycroft-core group to be able to use Mycroft. 
	> Use "sudo usermod -a -G mycroft-core YOUR-USER-NAME" to add yourself to the group.

	> Info can be added for installing on Android, Ubuntu snaps, or docker if anyone is interested in using any of them

## Working with Mycroft skills
* 	Rasberry Pi
	
	> On the Picroft installation image, a shortcut/symlink to the skills folder is found in /home/pi/skills/.

	> The symlink will point to /opt/mycroft/skills/, which is where custom made skills should go.

	> The default skills are found in /home/mycroft/.mycroft/skills/.

* 	Linux PCs

	> Mycroft uses virtualenv for everything python related

	> The skills directory should also be /opt/mycroft/skills/.

	> If you install from the AUR, the skills directory is in /usr/share/mycroft-core/mycroft/skills/.

	> You _might_ need to "force" Mycroft to use python 2 if you have python 3 installed.

	> If you use Picroft you probably won't need to, unless you installed python 3 and it can be started with "python" in a terminal.
	
	> If you are using a system that does have python 3 installed and can be started with "python", using a bash alias can start python 2 instead of 3 so that Mycroft can start properly.

	> The Picroft bashrc is in /home/pi/.bashrc.

	> Tweak the ~/.bashrc file for the user you will be using to start Mycroft.

# Working with the iRobot skill
* 	Skill creation [tutorial](https://docs.mycroft.ai/skill.creation)
	
	> This will show the basics in creating skills.

	> Please use the guide as a comparison, looking for anything missed or coded incorrectly.


* 	The skill is intended to start with 4 basic movements: forward, backward, left, and right.
	
	> The files in iRobotSkill/vocab/en-us/ are the phrases that should trigger Mycroft to respond with voice and move the iRobot.
	
	>The files in iRobotSkill/dialog/en-us/ are the responses that Mycroft will say.

	> In both sets of files, every line is a separate phrase for instructions/responses. Multiple instructions and responses can be used.
	
	> The main chunk of a skill is in iRobotSkill/\_\_init_\_\.py.

	> In the same directory is the create.py file from Piazza, this connects the robot via pySerial in a python terminal.

	> It is how we will be sending commands to the iRobot. There is also a guide on Piazza for various commands for the iRobot.

	> The create.py module requires python 3 and pySerial (python-serial) while Mycroft requires python 2.

* 	Creating new movements, and doing things in general:
	
	> Odemetry can be used with robot.getPose(), robot.setPose(), robot.resetPose, robot._integrateNextOdemetricStepCreate().

	> cm and mm can both be used as variables for the odemetric functions, as well as degrees and radians.

	> robot.setWheelVelocites() can take different, indidiual speeds for each wheel, useful for turns, spinning, just going fast, etc.

	> robot.stop() stops the robot, robot.go() takes both speed and degrees, so you can make the robot go straight or in a curve, forward or backward.

	> robot,_start() changes the robot from OFF_MODE to PASSIVE_MODE, robo-coffee basically.

	> robot.close() shuts the robot down

	> robot._closeSer() disconnects the serial port while robot._openSer() opens the port again

	> robot._drive() implements the drive command as specified the turn_dir should be either 'CW' or 'CCW' for clockwise or 
	
	> counterclockwise - this is only used if roomba_radius_mm == 0 (or rounds down to 0) 
	
	> other drive-related calls are available

	> robot.setLEDs() lets you play with the three LEDS (power, play, and status), colors can be changed as well as intensity.

	> robot._getRawSensorFrameAsList() gets back a raw string of sensor data which then can be used to create a SensorFrame

	> robot._getRawSensorDataAsList gets the chosen sensors and returns the raw bytes, as a string need to be converted to integers

	> robot.seekDock() sends the force-seeking-dock signal (we don't have one, please don't use this unless you get one)

	> robot.demo() lets you play with the various built-in iRobot demos

	> robot.setSong() store a song to be played later, robot.playSong() will play back song stored with robot.setSong()

	> robot.playSongNumber() plays back a song based on its assigned number

	> robot.playNote() plays a single note because you have no talent whatsoever. Mr Tentacles has all the talent. If you're lucky,
	
	> Mr. Talent will rub his tentacles on your l33t script kiddie hax.

	> There are a bunch of bit/byte/data frame/raw data functions if you find anything like that useful 

	> robot.sensors() this function updates the robot's currently maintained state of its robot sensors for those sensors requested
        
	> If none are requested, then all of the sensors are updated (which takes a bit more time...)

	> robot.printSensors() convenience function to show sensed data in d if d is None, the current self.sensord is used instead

	> robot._readSensorList() this returns the latest values from the particular sensors requested in the listofvalues

	> robot.toSafeMode() puts the robot in safe mode while robot.toFullMode() puts the robot in full mode 

	> You can use robot.getMode() to get the current mode the robot is in 

	> robot._setBaudRate() if you change this, I will hate you. Don't touch it.

	> robot._interpretSensorString() This returns a sensorFrame object with its fields filled in from the raw sensor return string, r, which
        
	> has to be the full 3-packet (26-byte) string. r is obtained by writing [142][0] to the serial port.

	> robot.turn() for turning the robot at different speeds, while robot.move() can set a specific distance and speed

	> robot.senseFunc() Returns a function which, when called, updates and returns information for a specified sensor (sensorName).
        
	> e.g. cliffState = robot.senseFunc(create.CLIFF_FRONT_LEFT_SIGNAL) info = cliffState()

	> robot.sleepTill() Have the robot continue what it's doing until some halting criterion is met, determined by a repeated polling of
        
	> sensorFunc until it's comparison (a function) to value is true. e.g. greater = lambda a,b: a > b


## ~~Potential software usage~~
* 	~~GNU Screen~~
	
	> ~~useful for keeping a pySerial sessing open.~~

	> ~~Commands can be sent to a running screen session so only one session needs to be run.~~

* 	~~systemd/cron service~~
	
	> ~~useful for starting a GNU Screen session on boot and starting a pySerial sessing within the Screen session~~
	
	> ~~cron is a bit easier to use, but may require installation if not part of a normal Raspbian installation~~
	
	> ~~systemd _might_ be slightly better, needs investigation~~
