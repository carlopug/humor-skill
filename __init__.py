from mycroft import MycroftSkill, intent_file_handler


class Humor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('humor.intent')
    def handle_humor(self, message):
        self.speak_dialog('humor')


def create_skill():
    return Humor()

