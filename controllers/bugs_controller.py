from services.bug_service import BugService

class BugsController:
    def __init__(self, bug_service: BugService):
        self.bug_service = bug_service

    def save_bug(self, bug_data):
        """Handles saving a bug."""
        return self.bug_service.save_bug(bug_data)

    def get_all_bugs(self):
        """Fetches all bugs."""
        return self.bug_service.get_all_bugs()
