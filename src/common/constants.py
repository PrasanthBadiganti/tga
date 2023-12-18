class FeatureFlags:
    USER_FEATURE_FLAG_ENABLED = True


class Constants:
    WHITELISTED_USERS = ['TestUser1', 'TestUser2']
    EXPEDTED_PRIVS = ['READ', 'WRITE']
    ALLOWED_USERS = ['TestUser1', 'TestUser2', 'User1', 'User2', 'User3', 'User4', 'User5']


PRIVILEGES_DICT = {
    'TestUser1': ['READ', 'WRITE'],
    'TestUser2': ['READ'],
    'User1': ['READ', 'WRITE'],
    'User2': ['READ'],
    'User3': ['READ'],
    'User4': ['READ', 'WRITE'],
    'User5': ['READ', 'WRITE']
}
