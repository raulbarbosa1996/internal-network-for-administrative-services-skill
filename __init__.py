from mycroft import MycroftSkill, intent_file_handler


class InternalNetworkForAdministrativeServices(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('services.administrative.for.network.internal.intent')
    def handle_services_administrative_for_network_internal(self, message):
        self.speak_dialog('services.administrative.for.network.internal')


def create_skill():
    return InternalNetworkForAdministrativeServices()

