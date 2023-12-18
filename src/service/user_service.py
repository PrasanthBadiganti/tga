from src.common.constants import FeatureFlags, Constants


class UserService:

    def fetch_all_users(self, request):
        if self.is_feature_enabled(request):
            return self.fetch_newly_added_whitelisted_users()
        else:
            return self.fetch_older_users()

    def is_feature_enabled(self, request):
        current_user = self.get_current_user(request)
        return FeatureFlags.USER_FEATURE_FLAG_ENABLED and current_user in Constants.WHITELISTED_USERS

    @staticmethod
    def fetch_newly_added_whitelisted_users():
        return ['new_user1', 'new_user2', 'new_usr3']

    @staticmethod
    def fetch_older_users():
        return ['old_user1', 'old_user2', 'old_user3']

    @staticmethod
    def get_current_user(request):
        auth_header = request.headers.get("Authorization")
        token = auth_header.split("Bearer ")[1].strip()
        return token
