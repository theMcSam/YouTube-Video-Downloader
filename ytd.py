from pytube import YouTube
from pytube.cli import on_progress
import colorama
from colorama import Fore
from colorama import Style
import time
import sys
import getpass
import socket
import urllib

colorama.init()
banner = f'''{Fore.RED}
Y88b    /                   ~~~888~~~          888                   ▄███████████▄                        
 Y88b  /   e88~-_  888  888    888    888  888 888-~88e   e88~~8e    █████░▀██████                       
  Y88b/   d888   i 888  888    888    888  888 888  888b d888  88b   █████░░░▀████                       
   Y8Y    8888   | 888  888    888    888  888 888  8888 8888__888   █████░░░▄████                       
    Y     Y888   ' 888  888    888    888  888 888  888P Y888    ,   █████░▄██████                       
   /       "88_-~  "88_-888    888    "88_-888 888-_88"   "88___/    █████████████
                                                                     ─▀▀▀▀▀▀▀▀▀▀▀─
{Style.RESET_ALL}
'''                        

lower_prt_of_banner = f'''{Fore.YELLOW}
888~-_                                    888                          888                  
888   \   e88~-_  Y88b    e    / 888-~88e 888  e88~-_    /~~~8e   e88~\888  e88~~8e  888-~\ 
888    | d888   i  Y88b  d8b  /  888  888 888 d888   i       88b d888  888 d888  88b 888    
888    | 8888   |   Y888/Y88b/   888  888 888 8888   |  e88~-888 8888  888 8888__888 888    
888   /  Y888   '    Y8/  Y8/    888  888 888 Y888   ' C888  888 Y888  888 Y888    , 888    
888_-~    "88_-~      Y    Y     888  888 888  "88_-~   "88_-888  "88_/888  "88___/  888{Style.RESET_ALL}     
==========================================================================================                                                                                                                       
'''

videoQuality = ['144p','360p','480p', '720p']

success = Fore.BLUE + "[+]" + Style.RESET_ALL
fail = Fore.RED + "[-]" + Style.RESET_ALL

def main():
	global success, fail, videoQuality
	print(banner+lower_prt_of_banner)

	def insertURL():
		global youTubeUrl
		print("Enter the YouTube url here.")
		youTubeUrl = str(input(" :> "))
		if "youtube.com" not in youTubeUrl:
			print(fail+" Invalid URL!!" )
			insertURL()

	def insertPath():
		global path
		print("\nEnter the path to save video.(Default: Downloads)")
		path = str(input(" :> "))

		if path == "":
			path = "C:/Users/" + str(getpass.getuser()) + "/Downloads"
		else:
			pass
	
	def selectQuality():
		global quality
		counter = 1
		try:
			print("\nSelect Video QUality: ")
			for i in videoQuality:
				print(str(counter)+". "+i)
				counter += 1
			quality = int(input("\n :> ")) - 1

		except ValueError:
			selectQuality()

		if quality>3 or quality<0:
			print(fail + " Invalid Number chosen.")
			selectQuality()
		else:
			pass
	insertURL()
	insertPath()
	selectQuality()
	download_video(youTubeUrl,path)
	

def download_video(url,path):
	try:
		print("\n" + success + " Downloading .....")
		yt = YouTube(url, on_progress_callback = on_progress) 
		video = yt.streams.filter(mime_type = "video/mp4", res = videoQuality[quality]).first()
		start_time = time.time()
		video.download(path)
		end_time = time.time()
		print(success + "Successfully Downloaded Video.")
		print(f'''
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
	 	YouTube Video: {yt.title}                                                      
	 	Time Started: {start_time} seconds                                                    
	 	Time Ended: {end_time} seconds                                                        
	 	Download Location: {path}                                                      
	 	File Size: {video.filesize} KB                                                    
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			''')

	except socket.gaierror:
		print(fail+" You do not have a stable intenet connection.")

	except urllib.error.URLError:
		print(fail+" You do not have a stable intenet connection.")

	except KeyboardInterrupt:
		print(fail+" Exiting......")
		sys.exit()


if __name__ == '__main__':
	try :
		main()
	except KeyboardInterrupt:
		print("\n"+fail + " Exiting.........")
		sys.exit()