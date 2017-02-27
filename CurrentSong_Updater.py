# Import relevent modules.
import html
import sys,os,time
from stat import *

# Name of the file to check.
fName = 'C:/Path/To/CurrentSong.txt' # The path to the txt file ankhbot/snip writes in
hName = 'C:/Path/To/CurrentSong_Customize.html' # The path to the HTML file you wish to use for customizing the text

# Get the time the file was last modified.
fInfo = os.stat(fName)
mTime = fInfo[ST_MTIME]

# Start an 'infinite' loop.
while True:
    # Get the modification time again and compare
    # to the one we stored previously.
    # If it's changed act accordingly.
    fInfo = os.stat(fName)
    if mTime != fInfo[ST_MTIME]:

        # Opens the txt file and reads the content as a string called "currentsong"
        writethis = open(fName, 'r')
        currentsong = writethis.read()

        # Reads the content in the html as a string called "contents"
        with open(hName, 'r') as f:
            contents = f.read()

        # Replaces special characters like quotation marks so that it doesn't mess with the html code
        currentsong = html.escape(currentsong)

        # Defines the content between starting_text and ending_text it wants to replace with to_replace
        starting_div = '<div data-text="'
        ending_div = '" id="divbox">'
        starting_p = '<p>'
        ending_p = '</p>'
        to_replace = contents[contents.find(starting_p)+len(starting_p):contents.rfind(ending_p)]
        to_replace = contents[contents.find(starting_div)+len(starting_div):contents.rfind(ending_div)]

        # to_replace in contents is replaced with currentsong
        contents = contents.replace(to_replace, currentsong)

        # Writes the new content to the html file
        with open(hName, 'w') as text_file:
            print(contents, file=text_file)

        mTime = fInfo[ST_MTIME]

    # Delay of 10 second so it doesn't take that much processing power.
    time.sleep(10)
