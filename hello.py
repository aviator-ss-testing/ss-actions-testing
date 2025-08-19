print("Hello, Aviator! Ok I saw webhook arrive but nothing happened?")

def authenticate_user(username, password):
    """Simple authentication function for testing"""
    return username == "admin" and password == "secret"
