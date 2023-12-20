class UserService:

    def fetch_all_users(self, request, flag_enabled):
        if flag_enabled:
            return self.fetch_newly_added_whitelisted_users()
        else:
            return self.fetch_older_users()

    @staticmethod
    def fetch_newly_added_whitelisted_users():
        return ['whitelisted_user1', 'whitelisted_user2', 'whitelisted_user3']

    @staticmethod
    def fetch_older_users():
        return ['old_user1', 'old_user2', 'old_user3']
