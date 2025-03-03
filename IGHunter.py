import instaloader
import argparse

# Banner
def banner():
    print("""
    Instagram Username Info Finder
    Coded by C. Jasvanth
    ---------------------------------
    """)

# Fetch Instagram Profile Info
def get_instagram_info(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"Username       : {profile.username}")
        print(f"Full Name      : {profile.full_name}")
        print(f"Bio            : {profile.biography}")
        print(f"Followers      : {profile.followers}")
        print(f"Following      : {profile.followees}")
        print(f"Posts Count    : {profile.mediacount}")
        print(f"Is Private     : {profile.is_private}")

        # Download Profile Picture
        loader.download_profilepic(profile)
        print(f"Profile Picture Downloaded: {profile.username}_profile_pic.jpg")

    except Exception as e:
        print(f"Error: {e}")

# Main Function
if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="Instagram Username Information Finder")
    parser.add_argument("-u", "--username", help="Target Instagram Username", required=True)
    args = parser.parse_args()

    get_instagram_info(args.username)

