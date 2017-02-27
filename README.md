# Current-song-customization-for-twitch
If you're using ankhbot or snip or any kind of software that lets you play a song playlist and it writes the current song into a .txt file, you can use this to customize your text even further in OBS rather than using the boring old text source.

# How to use
1. You'll need Python which you can download at https://www.python.org/ , I used Python 3.6.0.
2. Download the CurrentSong_Updater.py and CurrentSong_Customize.html
3. Edit CurrentSong_Updater.py by right-clicking and edit with IDLE and copy/paste the filepaths for the CurrentSong_Customize.html and the .txt that AnkhBot or Snip writes in inside the single quotation marks of fName and hName.
4. Open up OBS and add a Browser Source, name it whatever you want and press OK. Browse for the CurrentSong_Customize.html and press Open.
5. To make the text autoupdate, run the CurrentSong_Updater.py by double-clicking it.

To customize the text, simply edit the CurrentSong_Customize.html and change the CSS code to your liking using WordPad or any editing program you like.

## Note
I did not write all the code by myself, I am in no way capable of coming up with/writing scripts larger than a line or two. I did alot of googling and copy/paste to achieve this.
