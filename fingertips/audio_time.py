from mutagen.mp3 import MP3

# Path to your MP3 file
audio = MP3('JD_americano.mp3')

# Get duration in seconds
duration = audio.info.length

# Convert to minutes and seconds
minutes = int(duration // 60)
seconds = int(duration % 60)

print(f"Duration: {minutes} minutes and {seconds} seconds")
