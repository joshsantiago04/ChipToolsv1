# ChipTools, created by Josh Santiago
# Originally intended as a personal project, Crimson Code Hackathon gave Josh an
# actual reason to work on this coding project

# "Can't say I've worked with Python too much before, let alone CustomTKinter.
# I will continue to improve upon this application as I please." - Josh S.

# Created on February 17, 2024
# Current implementations:
# - Basic GUI Desisn
# - YouTube Video Downloader# - YouTube Video to .mp3 Converter
# -----------------------------------------------------------------------
import customtkinter
from menus import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

loginWindow = loginScreen()
loginWindow.mainloop()
