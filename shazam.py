import asyncio
from shazamio import Shazam

async def get_song_info(file):
    shazam = Shazam()
    out = await shazam.recognize(file)
    
    if 'track' not in out:
        return None, None, None
        
    track = out['track']
    title = track.get('title')
    subtitle = track.get('subtitle') 
    artist = track.get('subtitle') # Artist name is typically in the subtitle field
    
    return title, subtitle, artist


