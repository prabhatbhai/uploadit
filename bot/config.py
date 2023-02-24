import os


class Config:

    BOT_TOKEN = os.environ.get("1406539752:AAHQPinUR5yfd-cv-BLFkeV9wUJ2-ERAats")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("2071738"))

    API_HASH = os.environ.get("d8ab985751872891ce273ed65060a19f")

    CLIENT_ID = os.environ.get("199772217134-kug8e0idkpa16tu8okpl6p99sgv2d3bv.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("SINqPejVv_IYNo90y5-Q7Fhv")

    BOT_OWNER = int(os.environ.get("588014450"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
