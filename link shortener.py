import pyshorteners 

link = input("Enter the link you want to shorten: ")
shorten = pyshorteners.Shortener()
shortened_url = shorten.tinyurl.short(link)

print(f"Your link has been shortened: {shortened_url}")