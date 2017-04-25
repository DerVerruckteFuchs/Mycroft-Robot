# import directory that create_python2.py is in
import sys
sys.path.append('/opt/mycroft/skills/iRobotSkill')

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

# import the create.py module and time module
import create_python2
import time

__author__ = 'group-name'

LOGGER = getLogger(__name__)

class iRobotSkill(MycroftSkill):

    def __init__(self):
        # put necessary attributes here
        super(iRobotSkill, self).__init__(name="iRobotSkill")

    def initialize(self):
        # put necessary movement stuffs here

        # necessary for loading files in skills folder
        self.load_data_files(dirname(__file__))

        # put intents here
        go_forward_intent = IntentBuilder("GoForwardIntent").\
            require("GoForwardKeyword").build()
        self.register_intent(go_forward_intent, self.handle_go_forward_intent)

        go_backward_intent = IntentBuilder("GoBackwardIntent").\
            require("GoBackwardKeyword").build()
        self.register_intent(go_backward_intent, self.handle_go_backward_intent)


        go_right_intent = IntentBuilder("GoRightIntent").\
            require("GoRightKeyword").build()
        self.register_intent(go_right_intent, self.handle_go_right_intent)


        go_left_intent = IntentBuilder("GoLeftIntent").\
            require("GoLeftKeyword").build()
        self.register_intent(go_left_intent, self.handle_go_left_intent)
        #
        #go_tile_one_intent = IntentBuilder("GoTileOne").\
        #    require("GoTileOneKeyword").build()
        #self.register_intent(go_tile_One_intent, self.handle_go_tile_one_intent)
        #
        #go_tile_two_intent = IntentBuilder("GoTileTwo").\
        #    require("GoTileTwoKeyword").build()
        #self.register_intent(go_tile_two_intent, self.handle_go_tile_two_intent)
        #
        #go_tile_three_intent = IntentBuilder("GoTileThree").\
        #    require("GoTileThirdKeyword").build()
        #self.register_intent(go_tile_three_intent, self.handle_go_tile_three_intent)
        #
        #go_tile_four_intent = IntentBuilder("GoTileFour").\
        #    require("GoTileFourKeyword").build()
        #self.register_intent(go_tile_four_intent, self.handle_go_tile_four_intent)
        #
        #go_tile_five_intent = IntentBuilder("GoTileFive").\
        #    require("GoTileFiveKeyword").build()
        # self.register_intent(go_tile_five_intent, self.handle_go_tile_five_intent)
        #
        #go_tile_six_intent = IntentBuilder("GoTileSix").\
        #    require("GoTileSixKeyword").build()
        #self.register_intent(go_tile_six_intent), self.handle_go_tile_six_intent)
        #
        #go_tile_seven_intent = IntentBuilder("GoTileSeven").\
        #    require("GoTileSevenKeyword").build()
        #self.register_intent(go_tile_seven_intent), self.handle_go_tile_seven_intent)
        #
        #go_tile_eight_intent = IntentBuilder("GoTileEight").\
        #    require("GoTileEightKeyword").build()
        #self.register_intent(go_tile_eight_intent), self.handle_go_tile_eight_intent)
        #
        #go_tile_nine_intent = IntentBuilder("GoTileNine").\
        #     require("GoTileNineKeyword").build()
        #self.register_intent(go_tile_nine_intent), self.handle_go_tile_nine_intent)

        dance_intent = IntentBuilder("DanceIntent").\
            require("DanceKeyword").build()
        self.register_intent(dance_intent, self.handle_dance_intent)


    def handle_go_forward_intent(self, message):
        self.speak_dialog("going.forward")
        #self.robot.move(100, 20)
        #time.sleep(1)
        robot = create_python2.Create('/dev/ttyUSB0')
        robot.go(200, 0)
        time.sleep(2)
        robot.stop()

    def handle_go_backward_intent(self, message):
        self.speak_dialog("going.backward")
        #self.robot.move(-100, 20)
        robot = create_python2.Create('/dev/ttyUSB0')
        robot.go(-200, 0)
        time.sleep(2)
        robot.stop()


    def handle_go_right_intent(self, message):
        self.speak_dialog("going.right")
        #self.robot.turn(90)
        #self.robot.move(100, 20)
        robot = create_python2.Create('/dev/ttyUSB0')
        robot.go(0, -45)
        time.sleep(2)
        robot.stop()
        robot.go(200, 0)
        time.sleep(2)
        robot.stop()


    def handle_go_left_intent(self, message):
        self.speak_dialog("going.left")
        #self.robot.turn(-90)
        #self.robot.move(100, 20)
        robot = create_python2.Create('/dev/ttyUSB0')
        robot.go(0, 45)
        time.sleep(2)
        robot.stop()
        robot.go(200, 0)
        time.sleep(2)
        robot.stop()

    def handle_dance(self, message):
        self.speak_dialog("dance")
        robot = create_python2.Create('/dev/ttyUSB0')
        #robot.playSong( [(60,8),(64,8),(67,8),(72,8)] )
        robot.go(200, 90)
        time.sleep(10)
        robot.stop()
        robot.go(-200, 90)
        time.sleep(10)
        robot.stop()

    #def handle_go_tile_one_intent(self, message):
    #    self.speak_dialog("going.tile.one")
    #    robot = create_python2.Create('/dev/ttyUSB0')
    #    goToTile = 9



    #def handle_some_voice_intent(self, message):
        #self.speak_dialog("some dialog")

    #def handle_some_intent(self)
        # do thing

    def stop(self):
        # stop when finished
        pass


def create_skill():
    return iRobotSkill()
