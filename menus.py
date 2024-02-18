import customtkinter
import tkinter
from PIL import ImageTk, Image

from ytdownloader import DownloadMP4, DownloadMP3

class loginScreen(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("300x400")
        self.title("ChipTools by Josh")
        self.resizable(False, False)

        self.frame = customtkinter.CTkFrame(master=self, width=340, height=380, corner_radius=20, border_color="#307CDC", border_width=3)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label = customtkinter.CTkLabel(self.frame, text="ChipTools", font=("Century Gothic", 24))
        self.label.pack(pady=12, padx=10)

        
        self.creatorName = customtkinter.CTkLabel(self.frame, text="By Josh Santiago", font=("Century Gothic", 10))
        self.creatorName.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(self.frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry = customtkinter.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.entry.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(self.frame, hover_color= '#0096CA', text="Login", command=self.openMainWindow)
        self.button.pack(pady=12, padx=10)
    
    def openMainWindow(self):

        self.destroy()

        main = mainScreen()
        main.mainloop()

# Main Screen, holds a bunch of the main stuff
class mainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        self.title("ChipTools by Josh")
        self.resizable(False, False)

        # Left Sidebar

        self.leftSidebar = customtkinter.CTkFrame(self, height = 800, width = 200, corner_radius=20)
        self.leftSidebar.pack(side="left", fill="both" ,padx=10, pady = 12)

        self.logoFrame = customtkinter.CTkFrame(self.leftSidebar, height=100, width = 200, corner_radius=20, border_width=3, border_color="#307CDC")
        self.logoFrame.pack(side="top", padx = 10, pady=12)

        self.logoSidebar = customtkinter.CTkLabel(self.logoFrame, text="ChipTools", font=("Century Gothic", 24))
        self.logoSidebar.pack(side="top", padx=10, pady=12)

        self.buttonMenu = customtkinter.CTkFrame(self.leftSidebar, height = 350, width = 150, corner_radius = 20)
        self.buttonMenu.pack(side="top", padx=10, pady=8)

        self.ytDownloadButton = customtkinter.CTkButton(self.buttonMenu, state="normal",fg_color='#424242', hover_color = '#0096CA', text="YouTube to .mp3/.mp4", command=self.openYTDownloader)
        self.ytDownloadButton.pack(side="top", padx=10, pady=12)

        self.mp3Button = customtkinter.CTkButton(self.buttonMenu, state="normal",fg_color='#424242', hover_color = '#0096CA', text=".mp3 to .mp4 (WIP)", command=self.openMP3Extractor)
        self.mp3Button.pack(side="top", padx=10, pady=12)

        self.converterButton = customtkinter.CTkButton(self.buttonMenu, state="normal",fg_color='#424242', hover_color = '#0096CA', text="File Converter (WIP)", command=self.openConverter)
        self.converterButton.pack(side="top", padx=10, pady=12)

        self.logoutButton = customtkinter.CTkButton(self.leftSidebar, hover_color= '#0096CA',text="Logout", command=self.logout)
        self.logoutButton.pack(side="bottom", padx=10, pady=12)

        # YT Downloader mp3/mp4 widget

        self.ytDframeMaster = customtkinter.CTkFrame(master=self, height=1000, width=500,bg_color="transparent", corner_radius=20)
    
        self.ytDframe = customtkinter.CTkFrame(self.ytDframeMaster, height=500, width=300, corner_radius=20, border_width=3, border_color="#424242")
        self.ytDframe.pack(side="top", padx=10, pady=12)

        self.ytDlabel = customtkinter.CTkLabel(self.ytDframe, text="YouTube to .mp3/.mp4 Downloader", font=("Century Gothic", 30))
        self.ytDlabel.pack(side="top", padx=10, pady=12)

        self.ytLinkEntry = customtkinter.CTkEntry(self.ytDframe, placeholder_text="Link", width= 300)
        self.ytLinkEntry.pack(side="left", padx=10, pady=12)

        self.downloadmp3 = customtkinter.CTkButton(self.ytDframe, text=".mp3", width= 100, hover_color = '#0096CA', command=self.downloadLinkMP3)
        self.downloadmp3.pack(side="left", padx=10, pady=12)

        self.downloadmp4 = customtkinter.CTkButton(self.ytDframe, text=".mp4", width= 100, hover_color = '#0096CA', command=self.downloadLinkMP4)
        self.downloadmp4.pack(side="left", padx=10, pady=12)

        self.ytDOutputFrame = customtkinter.CTkFrame(self.ytDframeMaster, height=200, width=500, corner_radius=20, border_width=3, border_color="#424242")
        self.ytDOutputFrame.pack(side="bottom", padx=10, pady=12)

        self.ytDOutputText = customtkinter.CTkLabel(self.ytDOutputFrame, text='"Haven\'t gotten a responsive result printer finished in time, but I assure you it works! Check the project folder for the downloads!" - Josh S.', text_color="yellow", font=("Century Gothic", 10))
        self.ytDOutputText.pack(side="top", padx = 10, pady = 12)
        # mp4 to mp3 widget

        self.mp3FrameMaster = customtkinter.CTkFrame(master=self, height=1000, width=500,bg_color="transparent", corner_radius=20)
    
        self.mp3Frame = customtkinter.CTkFrame(self.mp3FrameMaster, height=500, width=300, corner_radius=20, border_width=3, border_color="#424242")
        self.mp3Frame.pack(side="top", padx=10, pady=12)

        self.mp3Label = customtkinter.CTkLabel(self.mp3Frame, text=".mp3 to .mp4 Converter (WIP)", font=("Century Gothic", 30))
        self.mp3Label.pack(side="top", padx=10, pady=12)

        self.mp3Entry = customtkinter.CTkEntry(self.mp3Frame, placeholder_text="Link", width= 300)
        self.mp3Entry.pack(side="left", padx=10, pady=12)

        self.mp3DownloadButton = customtkinter.CTkButton(self.mp3Frame, text=".mp3", width= 100, hover_color = '#0096CA', command=self.downloadLinkMP3)
        self.mp3DownloadButton.pack(side="left", padx=10, pady=12)

        self.mp3OutputFrame = customtkinter.CTkFrame(self.mp3FrameMaster, height=200, width=500, corner_radius=20, border_width=3, border_color="#424242")
        self.mp3OutputFrame.pack(side="bottom", padx=10, pady=12)

        # converter widget

        self.converterFrameMaster = customtkinter.CTkFrame(master=self, height=1000, width=500,bg_color="transparent", corner_radius=20)
    
        self.converterFrame = customtkinter.CTkFrame(self.converterFrameMaster, height=500, width=300, corner_radius=20, border_width=3, border_color="#424242")
        self.converterFrame.pack(side="left", padx=10, pady=12)

        self.converterLabel = customtkinter.CTkLabel(self.converterFrame, text="File Converter (WIP)", font=("Century Gothic", 30))
        self.converterLabel.pack(side="top", padx=10, pady=12)

        self.fileEntry = customtkinter.CTkEntry(self.converterFrame, placeholder_text="File", width= 300)
        self.fileEntry.pack(side="left", padx=10, pady=12)

        self.convertButton = customtkinter.CTkButton(self.converterFrame, text="Convert", width= 100, hover_color = '#0096CA')
        self.convertButton.pack(side="left", padx=10, pady=12)

        self.converterOutputFrame = customtkinter.CTkFrame(self.converterFrameMaster, height=200, width=500, corner_radius=20, border_width=3, border_color="#424242")
        self.converterOutputFrame.pack(side="bottom", padx=10, pady=12)

    # functions to control opening widgets found from the buttons on the left sidebar
    # each function changes the button states and widget menu states accordingly
    def openYTDownloader(self):

        # closes any windows that may be open
        self.converterFrameMaster.pack_forget()
        self.mp3FrameMaster.pack_forget()

        if self.ytDownloadButton.cget("state") == "normal":
            self.ytDframeMaster.pack(side="left", anchor=tkinter.CENTER ,padx=10, pady=12)
            self.ytDownloadButton.configure(state="disabled")
        else:
            self.ytDframeMaster.pack_forget()

        self.converterButton.configure(state="normal")
        self.mp3Button.configure(state="normal")

    def openMP3Extractor(self):

        self.converterFrameMaster.pack_forget()
        self.ytDframeMaster.pack_forget()

        if self.mp3Button.cget("state") == "normal":
            self.mp3FrameMaster.pack(side="left", anchor=tkinter.CENTER ,padx=10, pady=12)
            self.mp3Button.configure(state="disabled")
        else:
            self.mp3FrameMaster.pack_forget()

        self.ytDownloadButton.configure(state="normal")
        self.converterButton.configure(state="normal")

    def openConverter(self):

        self.ytDframeMaster.pack_forget()
        self.mp3FrameMaster.pack_forget()

        if self.converterButton.cget("state") == "normal":

            self.ytDframeMaster.pack_forget()

            self.converterFrameMaster.pack(side="left", anchor=tkinter.CENTER ,padx=10, pady=12)
            self.converterButton.configure(state="disabled")
        else:
            self.converterFrameMaster.pack_forget()
        
        self.ytDownloadButton.configure(state="normal")
        self.mp3Button.configure(state="normal")
            
    # downloads a high-quality mp4 file from a given YouTube Link            
    def downloadLinkMP4(self):

        link = self.ytLinkEntry.get()
        DownloadMP4(link)

    # downloads an mp3 file from the audio of a given YouTube Link
    def downloadLinkMP3(self):

        link = self.ytLinkEntry.get()
        DownloadMP3(link)

    def outputDownloadResult(self):
        pass


    # switch back to login window
    def logout(self):

        self.destroy()
        login = loginScreen()
        login.mainloop()