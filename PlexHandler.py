from plexapi.myplex import MyPlexAccount


class PlexHandler:
    def init(self, user, password, server_name):
        self.plex = MyPlexAccount(
            user, password).resource(server_name).connect()

    def get_all_used_filepaths(self):
        sections = self.plex.library.sections()
        return [section.locations for section in sections]

    def scan_all_sections(self):
        for section in self.plex.library.sections():
            section.update()

    def add_new_section(self, name, folder_location):
        self.plex.library.add(name=name, type='other videos',
                              language='en', location=folder_location)
