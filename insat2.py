import instaloader

mod=instaloader.Instaloader()
a=input("enter a profile name")
mod.download_profile(a,profile_pic_only=True)
