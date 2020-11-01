from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from ttkthemes import themed_tk as tk
import os
import sys
import webbrowser
import time
import subprocess
import Pmw
from sys import platform
import re

def specifyentrydelete(*args):
	global specifyapkwindow_entry

	specifyapkwindow_entry.delete(0, END)

def getbatterystatus(*args):
	global chosendev

	os.system("adb -s " + chosendev + " shell dumpsys battery > batterystat.log")
	with open("batterystat.log", "r") as results:
		data = results.read()

		getbatterystatuswindow = Toplevel()
		getbatterystatuswindow.title("PhoneSploitGui")

		w = 200
		h = 200

		ws = getbatterystatuswindow.winfo_screenwidth()
		hs = getbatterystatuswindow.winfo_screenheight()

		batterystatus_textbox = Text(getbatterystatuswindow, bg="white")
		batterystatus_textbox.insert(END, data)
		batterystatus_textbox.pack()
		batterystatus_btn = Button(getbatterystatuswindow, text="OK", font=("Meera", 10, "bold"), command=getbatterystatuswindow.destroy)
		batterystatus_btn.pack()

def savefile(*args):
	global specifyapkwindow_entry
	global specifyapkwindow

	specifyapkwindow.withdraw()
	path = specifyapkwindow_entry.get()


	savefile = filedialog.asksaveasfilename(title="Save as apk")
	os.system("adb -s " + chosendev + " pull " + path + " " + savefile)

def selectingapk(*args):
	global specifyapkwindow
	global specifyapkwindow_entry

	specifyapkwindow = Toplevel()
	specifyapkwindow.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = specifyapkwindow.winfo_screenwidth()
	hs = specifyapkwindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	specifyapkwindow_label = Label(specifyapkwindow, text="Specify path to apk", font=("Meera", 10, "bold"))
	specifyapkwindow_label.pack()
	specifyapkwindow_entry = Entry(specifyapkwindow, width=50, bg="white")
	specifyapkwindow_entry.insert(0, "example: /data/app/com.snapchat.android-ynA9hJ-94Fg4EQTKHu_qTA==/base.apk")
	specifyapkwindow_entry.bind("<Return>", savefile)
	specifyapkwindow_entry.bind("<ButtonRelease-1>", specifyentrydelete)
	specifyapkwindow_entry.pack()


def showip(*args):
	global chosendev

	try:
		os.system("adb -s " + chosendev + " shell ip address show wlan0 > macip.log")
		with open("macip.log", "r") as results:
			data = results.read()

			macipwindow = Toplevel()
			macipwindow.title("PhoneSploitGui")

			w = 50
			h = 50

			ws = macipwindow.winfo_screenwidth()
			hs = macipwindow.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			macipwindow_textbox = Text(macipwindow, bg="white", font=("Meera", 10, "bold"))
			macipwindow_textbox.insert(END, data)
			macipwindow_textbox.pack()
			macipwindow_btn = Button(macipwindow, text="OK", font=("Meera", 10, "bold"), command=macipwindow.destroy)
			macipwindow_btn.pack()
	except:
		err_window = Toplevel()
		err_window.title("PhoneSploitGui")

		w = 500
		h = 80

		ws = err_window.winfo_screenwidth()
		hs = err_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		err_window_icon = Label(err_window, image=showmacipicon)
		err_window_icon.place(relx=0.28)
		err_window_label = Label(err_window, text="Couldn't get IP/Mac address", font=("Meera", 10, "bold"))
		err_window_label.place(relx=0.36, rely=0.08)
		err_window_btn = Button(err_window, text="OK", font=("Meera", 10, "bold"), command=err_window.destroy)
		err_window_btn.place(relx=0.45, rely=0.59)


def removelock(*args):
	try:
		os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
		os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
		os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
		os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")

		success_window = Toplevel()
		success_window.title("PhoneSploitGui")

		w = 500
		h = 80

		ws = success_window.winfo_screenwidth()
		hs = success_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		success_window_icon = Label(success_window, image=unlockicon)
		success_window_icon.place(relx=0.28)
		success_window_label = Label(success_window, text="Successfully removed passcode", font=("Meera", 10, "bold"))
		success_window_label.place(relx=0.36, rely=0.08)
		success_window_btn = Button(success_window, text="OK", font=("Meera", 10, "bold"), command=success_window.destroy)
		success_window_btn.place(relx=0.45, rely=0.59)
	except:
		err_window = Toplevel()
		err_window.title("PhoneSploitGui")

		w = 500
		h = 80

		ws = err_window.winfo_screenwidth()
		hs = err_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		err_window_icon = Label(err_window, image=unlockicon)
		err_window_icon.place(relx=0.28)
		err_window_label = Label(err_window, text="Couldn't remove passcode", font=("Meera", 10, "bold"))
		err_window_label.place(relx=0.36, rely=0.08)
		err_window_btn = Button(err_window, text="OK", font=("Meera", 10, "bold"), command=err_window.destroy)
		err_window_btn.place(relx=0.45, rely=0.59)

def turn_off_wifi(*args):
	global chosendev
	os.system("adb -s " + chosendev + " shell svc wifi disable")

	wifioffwindow = Toplevel()
	wifioffwindow.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = wifioffwindow.winfo_screenwidth()
	hs = wifioffwindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) -(h/2)

	wifioffwindow.geometry("%dx%d+%d+%d" % (w, h, x, y))
	wifioffwindow_icon = Label(wifioffwindow, image=togwifiicon)
	wifioffwindow_icon.place(relx=0.28)
	wifioffwindow_label = Label(wifioffwindow, text="WiFi has been disabled", font=("Meera", 10, "bold"))
	wifioffwindow_label.place(relx=0.36, rely=0.08)
	wifioffwindow_btn = Button(wifioffwindow, text="OK", font=("Meera", 10, "bold"), command=wifioffwindow.destroy)
	wifioffwindow_btn.place(relx=0.45, rely=0.59)

def turn_on_wifi(*args):
	global chosendev
	os.system("adb -s " + chosendev + " shell svc wifi enable")

	wifionwindow = Toplevel()
	wifionwindow.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = wifionwindow.winfo_screenwidth()
	hs = wifionwindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) -(h/2)

	wifionwindow.geometry("%dx%d+%d+%d" % (w, h, x, y))
	wifionwindow_icon = Label(wifionwindow, image=togwifiicon)
	wifionwindow_icon.place(relx=0.28)
	wifionwindow_label = Label(wifionwindow, text="WiFi has been enabled", font=("Meera", 10, "bold"))
	wifionwindow_label.place(relx=0.36, rely=0.08)
	wifionwindow_btn = Button(wifionwindow, text="OK", font=("Meera", 10, "bold"), command=wifionwindow.destroy)
	wifionwindow_btn.place(relx=0.45, rely=0.59)

def toggle_wifi(*args):

	buttonoptionwindow = Toplevel()
	buttonoptionwindow.title("PhoneSploitGui")

	w = 100
	h = 50

	buttonoptionwindow_label = Label(buttonoptionwindow, text="Choose option", font=("Meera", 15, "bold"))
	buttonoptionwindow_label.place(rely=0.20, relx=0.21)
	buttonoptionwindow_onbtn = Button(buttonoptionwindow, text="Turn on", font=("Meera", 10, "bold"), command=turn_on_wifi)
	buttonoptionwindow_onbtn.place(relx=0.10, rely=0.80)
	buttonoptionwindow_offbtn = Button(buttonoptionwindow, text="Turn off", font=("Meera", 10, "bold"), command=turn_off_wifi)
	buttonoptionwindow_offbtn.place(relx=0.5, rely=0.80)

def shownetstat(*args):
	global chosendev

	os.system("adb -s " + chosendev + " shell netstat > nstatresults.log")

	with open ("nstatresults.log", "r") as results:
		data = results.read()
		if re.search("not found", data):
			devnotfoundwindow = Toplevel()
			devnotfoundwindow.title("PhoneSploitGui")

			w = 500
			h = 80

			ws = devnotfoundwindow.winfo_screenwidth()
			hs = devnotfoundwindow.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			devnotfoundwindow.geometry("%dx%d+%d+%d" % (w, h, x, y))
			devnotfoundwindow_icon = Label(devnotfoundwindow, image=netstaticon)
			devnotfoundwindow_icon.place(relx=0.21)
			devnotfoundwindow_label = Label(devnotfoundwindow, text="Device not found. Check to see if you're still connected it to it.", font=("Meera", 10, "bold"))
			devnotfoundwindow_label.place(relx=0.29, rely=0.08)
			devnotfoundwindow_btn = Button(devnotfoundwindow, text="OK", font=("Meera", 10, "bold"))
			devnotfoundwindow_btn.place(relx=0.45, rely=0.59)

		if re.search("w/o servers", data):
			netstatresultswindow = Toplevel()
			netstatresultswindow.title("PhoneSploitGui")

			w = 500
			h = 300

			ws = netstatresultswindow.winfo_screenwidth()
			hs = netstatresultswindow.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			netstatresultstextbox = Text(netstatresultswindow, width=80, bg="white", font=("Meera", 10, "bold"))
			netstatresultstextbox.insert(END, data)
			netstatresultstextbox.pack()
			netstatresultsbtn = Button(netstatresultswindow, text="OK", font=("Meera", 10, "bold"), command=netstatresultswindow.destroy)
			netstatresultsbtn.pack()



def portfoward(*args):
	global enterforwardportwindow_entry
	global enterportwindow_entry
	global chosendev
	global enterforwardportwindow

	enterforwardportwindow.withdraw()

	device_port = enterportwindow_entry.get()
	forward_port = enterforwardportwindow_entry.get()

	try:
		with open ("output.txt", "w") as f:
			proc = str(subprocess.call(["adb", "-s", chosendev, "forward", "tcp:", device_port, "tcp:", forward_port], stdout=f, stderr=f))
			f.write(proc)
			with open ("output.txt", "r") as results:
				data = results.read()
				if re.search("Permission denied", data):
					permdeniedwindow = Toplevel()
					permdeniedwindow.title("PhoneSploitGui")

					w = 500
					h = 80

					permdeniedwindow.winfo_screenwidth()
					permdeniedwindow.winfo_screenheight()

					permdeniedwindow_icon = Label(permdeniedwindow, image=exitmenuicon)
					permdeniedwindow_icon.place(relx=0.21)
					permdeniedwindow_label = Label(permdeniedwindow, text="Permission was denied. Device might not be rooted.", font=("Meera", 10, "bold"))
					permdeniedwindow_label.place(relx=0.29, rely=0.08)
					permdeniedwindow_btn = Button(permdeniedwindow, text="OK", font=("Meera", 10, "bold"))
					permdeniedwindow_btn.place(relx=0.45, rely=0.59)

					enterportwindow.destroy()
					enterforwardportwindow.destroy()
	except:
		err_window = Toplevel()
		err_window.title("PhoneSploitGui")

		w = 500
		h =80

		ws = err_window.winfo_screenwidth()
		hs = err_window.winfo_screenheight()

		err_window_icon = Label(err_window, image=exitmenuicon)
		err_window_icon.place(relx=0.21)
		err_window_label = Label(err_window, text="Error executing task", font=("Meera", 10, "bold"))
		err_window_label.place(relx=0.29, rely=0.08)
		err_window_btn = Button(err_window, text="OK", font=("Meera", 10, "bold"))
		err_window_btn.place(relx=0.45, rely=0.59)

def choose_forward_port(*args):
	global enterforwardportwindow_entry
	global enterforwardportwindow
	global enterportwindow

	enterportwindow.withdraw()

	enterforwardportwindow = Toplevel()
	enterforwardportwindow.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = enterforwardportwindow.winfo_screenwidth()
	hs = enterforwardportwindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	enterforwardportwindow_label = Label(enterforwardportwindow, text="Enter a port to forward it to.", font=("Meera", 10, "bold"))
	enterforwardportwindow_label.pack()
	enterforwardportwindow_entry = Entry(enterforwardportwindow, width=50)
	enterforwardportwindow_entry.pack()

	enterforwardportwindow_entry.bind("<Return>", portfoward)


def choosedev_port(*args):
	global enterportwindow_entry
	global enterportwindow

	enterportwindow = Toplevel()
	enterportwindow.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = enterportwindow.winfo_screenwidth()
	hs = enterportwindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	enterportwindow.geometry("%dx%d+%d+%d" % (w, h, x, y))
	enterportwindow_label = Label(enterportwindow, text="Enter the port number on the device you want to forward", font=("Meera", 10, "bold"))
	enterportwindow_label.pack()
	enterportwindow_entry = Entry(enterportwindow, width=50)
	enterportwindow_entry.pack()

	#Binds
	enterportwindow_entry.bind("<Return>", choose_forward_port)



def new_device_connected(*args):
	global enterip_window

	enterip_window.destroy()

	with open("connected_devices.txt", "w") as f:
		proc = str(subprocess.call(["adb", "connect", chosendev], stdout=f, stderr=f))
		f.write(proc)
		with open("connected_devices.txt", "r") as results:
			data = results.read()
			if re.search("connected", data):

				connected_window = Toplevel()
				connected_window.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = connected_window.winfo_screenwidth()
				hs = connected_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				connected_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				connected_window_icon = Label(connected_window, image=connectbtnicon)
				connected_window_icon.place(relx=0.21)
				connected_window_label = Label(connected_window, text="Successfully connected to target device", font=("Meera", 10, "bold"))
				connected_window_label.place(relx=0.29, rely=0.08)
				connected_window_btn = Button(connected_window, text="OK", font=("Meera", 10, "bold"), command=connected_window.destroy)
				connected_window_btn.place(relx=0.45, rely=0.59)


def grabwpasup(*args):
	global chosendev

	try:
		choosedirmsg = Toplevel()
		choosedirmsg.title("PhoneSploitGui")
		w = 500
		h = 70

		ws = choosedirmsg.winfo_screenwidth()
		hs = choosedirmsg.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		choosedirmsg.geometry("%dx%d+%d+%d" % (w, h, x, y))
		choosedirmsg_icon = Label(choosedirmsg, image=grabwpasupicon)
		choosedirmsg_icon.place()
		choosedirmsg_label = Label(choosedirmsg, text="Choose where you would like to save the wpa supplicant file", font=("Meera", 10, "bold"))
		chooosedirmsg_label.place()
		choosedirmsg_button = Button(choosemsgdir, text="OK", command=choosedirmsg.destroy)
		choosedirmsg_button.place()

		location = filedialog.asksaveasfilename()
		os.system("adb -s "+ chosendev +" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
		os.system("adb -s "+ chosendev +" pull /sdcard/wpa_supplicant.conf "+location)
	except:
		err_window = Toplevel()
		err_window.title("PhoneSploitGui")

		w = 500
		h = 80

		ws = err_window.winfo_screenwidth()
		hs = err_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		err_window_icon = Label(err_window, image=exitmenuicon)
		err_window_icon.place(relx=0.18, rely=0.02)
		err_window_label = Label(err_window, text="Device is not rooted. Unable to get wpa supplicant.", font=("Meera", 10, "bold"))
		err_window_label.place(relx=0.24, rely=0.08)
		err_window_button = Button(err_window, text="OK", font=("Meera", 10, "bold"), command=err_window.destroy)
		err_window_button.place(relx=0.45, rely=0.5)

def closeattnwindow(*args):
	global Attnwindow

	Attnwindow.destroy()

def clear_runapp_example(*args):
	global runapp_window_entry

	runapp_window_entry.delete(0, END)

def runapp(*args):
	global chosendev
	global runapp_window_entry
	global runapp_window

	package_name = runapp_window_entry.get()

	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "-s", chosendev, "shell", "monkey", "-p", package_name, "-v", "1"], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as results:
			data = results.read()
			if re.search("Monkey finished", data):
				runapp_success_window = Toplevel()
				runapp_success_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = runapp_success_window.winfo_screenwidth()
				hs = runapp_success_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				runapp_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				runapp_success_window_icon = Label(runapp_success_window, image=runappbtnicon)
				runapp_success_window_icon.place(relx=0.19)
				runapp_success_window_label = Label(runapp_success_window, text="App has been successfully started", font=("Meera", 10, "bold"))
				runapp_success_window_label.place(relx=0.27, rely=0.08)
				runapp_success_window_btn = Button(runapp_success_window, text="OK", font=("Meera", 10, "bold"), command=runapp_success_window.destroy)
				runapp_success_window_btn.place(relx=0.45, rely=0.5)
				
				runapp_window.destroy()
			else:
				if re.search("monkey aborted", data):
					runapp_success_window = Toplevel()
					runapp_success_window.title("PhoneSploitGui")

					w = 500
					h = 70

					ws = runapp_success_window.winfo_screenwidth()
					hs = runapp_success_window.winfo_screenheight()

					x = (ws/2) - (w/2)
					y = (hs/2) - (h/2)

					runapp_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
					runapp_success_window_icon = Label(runapp_success_window, image=runappbtnicon)
					runapp_success_window_icon.place(relx=0.19)
					runapp_success_window_label = Label(runapp_success_window, text="There was an error trying to start the specified application. \nEither the package name has been mispelled, the client has left the network, or the host has disconnected from the client. \nIf that's the case, you'll need to reconnect to the device", font=("Meera", 10, "bold"))
					runapp_success_window_label.place(relx=0.27, rely=0.08)
					runapp_success_window_btn = Button(runapp_success_window, text="OK", font=("Meera", 10, "bold"), command=runapp_success_window.destroy)
					runapp_success_window_btn.place(relx=0.45, rely=0.5)
					runapp_window.destroy()

def selpack_run():
	global chosendev
	global runapp_window_entry
	global runapp_window

	runapp_window = Toplevel()
	runapp_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = runapp_window.winfo_screenwidth()
	hs = runapp_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	runapp_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	runapp_window_label = Label(runapp_window, text="Enter the package name of the app you want to run", font=("Meera", 10, "bold"))
	runapp_window_label.pack()
	runapp_window_entry = Entry(runapp_window, width=50, bg="white", font=("Meera", 10, "bold"))
	runapp_window_entry.bind("<Return>", runapp)
	runapp_window_entry.bind("<ButtonRelease-1>", clear_runapp_example)
	runapp_window_entry.insert(0, "example: com.snapchat.android")
	runapp_window_entry.pack()

def showapps():
	global chosendev
	with open("apps.txt", "w") as a:
		proc = str(subprocess.call(["adb", "-s", chosendev, "shell", "pm", "list", "packages", "-f"], stdout=a, stderr=a))
		a.write(proc)
		with open("apps.txt", "r") as results:
			applist_window = Toplevel()
			applist_window.title("PhoneSploitGui")

			w = 800
			h = 1000

			ws = applist_window.winfo_screenwidth()
			hs = applist_window.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			applist_window.geometry("%dx%d+%d+%d" % (w, h, x, y))

			applist_text = Text(applist_window, width=150, height=50, bg="white", font=("Meera", 10, "bold"))
			applist_text.insert(END, results.read())
			applist_text.pack()
			applist_btn = Button(applist_window, text="OK", font=("Meera", 10, "bold"), command=applist_window.destroy)
			applist_btn.pack(pady=5)

def folder_save():
	global folder_pull_popup
	global chosendev
	global folder_location_entry

	folder_pull_popup.destroy()

	try:
		if platform == "win32":
			print("Whatever")

		else:
			if platform == "linux":
				save_location = filedialog.askdirectory()
				folder_path = folder_location_entry.get()
				os.system("adb -s " + chosendev + " pull " + folder_path + " " + save_location)
				folder_pull_success_window = Toplevel()
				folder_pull_success_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = folder_pull_success_window.winfo_screenwidth()
				hs = folder_pull_success_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				folder_pull_success_window.geometry("%dx%d+%d+%d" % (w, h, x ,y))
				folder_pull_success_icon = Label(folder_pull_success_window, image=dloadfromdevbtnicon)
				folder_pull_success_icon.place(relx=0.19)
				folder_pull_success_label = Label(folder_pull_success_window, text="Folder has been successfully downloaded", font=("Meera", 10, "bold"))
				folder_pull_success_label.place(relx=0.27, rely=0.08)
				folder_pull_success_btn = Button(folder_pull_success_window, text="OK", font=("Meera", 10, "bold"), command=folder_pull_success_window.destroy)
				folder_pull_success_btn.place(relx=0.45, rely=0.5)

				folder_location_window.destroy()

	except:
		folder_pull_err_window = Toplevel()
		folder_pull_err_window.title("PhoneSploitGui")

		w = 500
		h = 70

		ws = folder_pull_err_window.winfo_screenwidth()
		hs = folder_pull_err_window.winfo_screenheight()

		x = (ws/2) - (h/2)
		y = (hs/2) - (w/2)

		folder_pull_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		folder_pull_err_icon = Label(folder_pull_err_window, image=dloadfromdevbtnicon)
		folder_pull_err_icon.place(relx=0.19)
		folder_pull_err_label = Label(folder_pull_err_window, text="There was an error copying the folder from the target to the computer. \nMake sure you are connected to the device and try again.", font=("Meera", 10, "bold"))
		folder_pull_err_label.place(relx=0.27, rely=0.08)
		folder_pull_err_btn = Button(folder_pull_err_window, text="OK", command=folder_pull_err_window.destroy)
		folder_pull_err_btn.place(relx=0.45, rely=0.5)

def dumpsys():
	global chosendev
	global dumpsys_save_location_window

	dumpsys_save_location_window.destroy()

	try:
		save_location = filedialog.asksaveasfilename(defaultextension=".log")
		with open(save_location, "w"):
			os.system("adb -s " + chosendev + " shell dumpsys > " + save_location)
			dumpsys_err_window = Toplevel()
			dumpsys_err_window.title("PhoneSploitGui")

			w = 500
			h = 70

			ws = dumpsys_err_window.winfo_screenwidth()
			hs = dumpsys_err_window.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			dumpsys_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
			dumpsys_err_icon = Label(dumpsys_err_window, image=dsibtnicon)
			dumpsys_err_icon.place(relx=0.21)
			dumpsys_err_label = Label(dumpsys_err_window, text="System dump has been completed!", font=("Meera", 10, "bold"))
			dumpsys_err_label.place(relx=0.29, rely=0.08)
			dumpsys_err_btn = Button(dumpsys_err_window, text="OK", font=("Meera", 10, "bold"), command=dumpsys_err_window.destroy)
			dumpsys_err_btn.place(relx=0.45, rely=0.5)
	except:
		dumpsys_done_window = Toplevel()
		dumpsys_done_window.title("PhoneSploitGui")

		w = 500
		h = 70

		ws = dumpsys_done_window.winfo_screenwidth()
		hs = dumpsys_done_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		dumpsys_done_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		dumpsysicon = Label(dumpsys_done_window, image=dsibtnicon)
		dumpsysicon.place(relx=0.21)
		dumpsys_done_msg = Label(dumpsys_done_window, text="There was an error dumping the system information to the text file. It's possible the device may have disconnected from the network.", font=("Meera", 10, "bold"))
		dumpsys_done_msg.place(relx=0.29, rely=0.08)
		dumpsys_done_btn = Button(dumpsys_done_window, text="OK", font=("Meera", 10, "bold"), command=dumpsys_done_window.destroy)
		dumpsys_done_btn.place(relx=0.45, rely=0.5)
		readfile()

def dumpsys_save_location():
	global dumpsys_save_location_window

	dumpsys_save_location_window = Toplevel()
	dumpsys_save_location_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = dumpsys_save_location_window.winfo_screenwidth()
	hs = dumpsys_save_location_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	dumpsys_save_location_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	dumpsysicon = Label(dumpsys_save_location_window, image=dsibtnicon)
	dumpsysicon.place(relx=0.19)
	dumpsys_save_location_window_label = Label(dumpsys_save_location_window, text="Choose where you would like to save the file", font=("Meera", 10, "bold"))
	dumpsys_save_location_window_label.place(relx=0.27, rely=0.08)
	dumpsys_save_location_window_btn = Button(dumpsys_save_location_window, text="OK", font=("Meera", 10, "bold"), command=dumpsys)
	dumpsys_save_location_window_btn.place(relx=0.45, rely=0.5)
	readfile()

def clear_save_example():
	global save_path_entry

def folder_pull(*args):
	global folder_pull_popup
	global chosendev
	global folder_location_entry
	global folder_location_window

	folder_location_window.withdraw()

	folder_pull_popup = Toplevel()
	folder_pull_popup.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = folder_pull_popup.winfo_screenwidth()
	hs = folder_pull_popup.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	folder_pull_popup.geometry("%dx%d+%d+%d" % (w, h, x, y))
	folder_pull_icon = Label(folder_pull_popup, image=dloadfromdevbtnicon)
	folder_pull_icon.place(relx=0.19)
	folder_pull_label = Label(folder_pull_popup, text="Choose where you would like to save the folder to", font=("Meera", 10, "bold"))
	folder_pull_label.place(relx=0.27, rely=0.08)
	folder_pull_btn = Button(folder_pull_popup, text="OK", font=("Meera", 10, "bold"), command=folder_save)
	folder_pull_btn.place(relx=0.45, rely=0.5)

def clear_pull_example(*args):
	global folder_location_entry

	folder_location_entry.delete(0, END)

def download_folders():
	global folder_location_entry
	global folder_location_window

	folder_location_window = Toplevel()
	folder_location_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = folder_location_window.winfo_screenwidth()
	hs = folder_location_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	folder_location_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	folder_location_label = Label(folder_location_window, text="Enter the path of the folder you want to download from the device", font=("Meera", 10, "bold"))
	folder_location_label.pack()
	folder_location_entry = Entry(folder_location_window, width=50, bg="white", font=("Meera", 10, "bold"))
	folder_location_entry.insert(0, "example: /sdcard/")
	folder_location_entry.bind("<ButtonRelease-1>", clear_pull_example)
	folder_location_entry.bind("<Return>", folder_pull)
	folder_location_entry.pack()

def screenshot():
	global listbox
	global chosendev

	os.system("adb -s" + chosendev + " shell screencap /sdcard/screen.png")
	scrnshot_success_window = Toplevel()
	scrnshot_success_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = scrnshot_success_window.winfo_screenwidth()
	hs = scrnshot_success_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	scrnshot_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	scrnshot_success_icon = Label(scrnshot_success_window, image=screenshotbtnicon)
	scrnshot_success_icon.place()
	scrnshot_success_label = Label()
	messagebox.showinfo("PhoneSploitGui", "Screenshot has been taken. Choose where you would like to save the screenshot.")

	if platform == "win32":
		filedialog.asksaveasfilename()
	else:
		if platform == "linux":
			with open("output.txt", "w") as f:
				save_loc = filedialog.asksaveasfilename(title="Save screenshot", filetypes=(("PNG", "*.png"),("All Files", "*.*")))
				proc = str(subprocess.call(["adb", "-s", chosendev, "pull", "/sdcard/screen.png", save_loc], stdout=f, stderr=f))
				f.write(proc)
				with open("output.txt", "r") as results:
					data = results.read()
					if re.search(r"%", data):
						scrnshot_save_window = Toplevel()
						scrnshot_save_window.title("PhoneSploitGui")

						w = 500
						h = 70

						ws = scrnshot_save_window.winfo_screenwidth()
						hs = scrnshot_save_window.winfo_screenheight()

						x = (hs/2) - (w/2)
						y = (ws/2) - (w/2)

						scrnshot_save_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
						scrnshot_save_window_icon = Label(scrnshot_save_window, image=screenshotbtnicon)
						scrnshot_save_window_icon.place(relx=0.19)
						scrnshot_save_window_label = Label(scrnshot_save_window, text="Screenshot has been saved", font=("Meera", 10, "bold"))
						scrnshot_save_window_label.place(relx=0.27, rely=0.08)
						scrnshot_save_window_btn = Button(scrnshot_save_window, text="OK", font=("Meera", 10, "bold"), command=scrnshot_save_window.destroy)
						scrnshot_save_window_btn.place(relx=0.45, rely=0.5)
					else:
						scrnshot_save_err_window = Toplevel()
						scrnshot_save_err_window.title("PhoneSploitGui")

						w = 500
						h = 70

						ws = scrnshot_save_err_window.winfo_screenwidth()
						hs = scrnshot_save_err_window.winfo_screenheight()

						x = (hs/2) - (w/2)
						y = (ws/2) - (w/2)

						scrnshot_save_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
						scrnshot_save_err_window_icon = Label(scrnshot_save_err_window, image=screenshotbtnicon)
						scrnshot_save_err_window_icon.place(relx=0.19)
						scrnshot_save_err_window_label = Label(scrnshot_save_err_window, text="Unable to take screenshot. \nEither the user has an app that prevents screenshots or there's connectivity issues", font=("Meera", 10, "bold"))
						scrnshot_save_err_window_label.place(relx=0.27, rely=0.08)
						scrnshot_save_err_window_btn = Button(scrnshot_save_err_window, text="OK", font=("Meera", 10, "bold"), command=scrnshot_save_err_window.destroy)
						scrnshot_save_err_window_btn.place(relx=0.45, rely=0.5)

def helpwindow(*args):
	helpwindow = Tk()
	helpwindow.title("Help")
	tabcontrol = ttk.Notebook(helpwindow)
	tab1 = ttk.Frame(tabcontrol)
	tabcontrol.add(tab1, text="Rooted Devices")
	tabcontrol.place(relx=0.0)

def github_page(*args):
	webbrowser.open("https://github.com/sketchyboi14/")

def destoptnlistwind(*args):
	global dispoptionswindow
	global root
	global Attnwindow

	dispoptionswindow.destroy()
	Attnwindow.destroy()

def page1(*args):
	global dispoptionswindow
	global showdevs
	global connectbtn
	global disconnectbtn
	global adbshellbtn
	global instapkbtn
	global screenrecbtn
	global screenshotbtn
	global restservbtn
	global pullfoldersbtn
	global turnoffdevbtn
	global uninstappbtn
	global rtlbtn
	global dsibtn
	global showappsbtn
	global runappbtn
	global downarrowbtn
	global uparrowbtn
	global portforwardbtn
	global grabwpasupbtn
	global showmacipbtn
	global ext_apkbtn
	global netstatbtn
	global togwifibtn
	global unlockbtn
	global batstatbtn
	global options
	global dispoptionswindow
	global enterip_window

	showdevs = Button(dispoptionswindow, text=options[0], compound=TOP, font=("Meera", 10, "bold"), image=showdevsbtnicon, command=showdevsconnected)
	showdevs.place(relx=0.0)
	connectbtn = Button(dispoptionswindow, text=options[1], compound=TOP, font=("Meera", 10, "bold"), image=connectbtnicon, command=connect_no_new_window)
	connectbtn.place(relx=0.25)
	disconnectbtn = Button(dispoptionswindow, text=options[2], compound=TOP, font=("Meera", 10, "bold"), image=disconnectbtnicon, command=disconnect_devices)
	disconnectbtn.place(relx=0.45)
	adbshellbtn = Button(dispoptionswindow, text=options[3], compound=TOP, font=("Meera", 10, "bold"), image=shellbtnicon, command=openshell)
	adbshellbtn.place(relx=0.69, relheight=0.197)
	instapkbtn = Button(dispoptionswindow, text=options[4], compound=TOP, font=("Meera", 10, "bold"), image=instapkbtnicon, command=apkinstpath)
	instapkbtn.place(relx=0.890, relheight=0.197)
	screenrecbtn = Button(dispoptionswindow, text=options[5], compound=TOP, font=("Meera", 10, "bold"), image=screenrecbtnicon, command=screenrecord)
	screenrecbtn.place(rely=0.27)
	screenshotbtn = Button(dispoptionswindow, text=options[6], compound=TOP, font=("Meera", 10, "bold"), image=screenshotbtnicon, command=screenshot)
	screenshotbtn.place(rely=0.27, relx=0.25, relheight=0.197)
	restservbtn = Button(dispoptionswindow, text=options[7], compound=TOP, font=("Meera", 10, "bold"), image=restservbtnicon, command=restartadbserver)
	restservbtn.place(rely=0.27, relx=0.45)
	pullfoldersbtn = Button(dispoptionswindow, text=options[8], compound=TOP, font=("Meera", 10, "bold"), image=dloadfromdevbtnicon, command=download_folders)
	pullfoldersbtn.place(rely=0.27, relx=0.69, relheight=0.197)
	turnoffdevbtn = Button(dispoptionswindow, text=options[9], compound=TOP, font=("Meera", 10, "bold"), image=poweroffbtnicon, command=turnoffphone)
	turnoffdevbtn.place(rely=0.27, relx=0.865)
	uninstappbtn = Button(dispoptionswindow, text=options[10], compound=TOP, font=("Meera", 10, "bold"), image=uninstappbtnicon, command=package_sel)
	uninstappbtn.place(rely=0.54)
	rtlbtn = Button(dispoptionswindow, text=options[11], compound=TOP, font=("Meera", 10, "bold"), image=logbtnicon, command=logmsg)
	rtlbtn.place(rely=0.54, relx=0.25)
	dsibtn = Button(dispoptionswindow, text=options[12], compound=TOP, font=("Meera", 10, "bold"), image=dsibtnicon, command=dumpsys_save_location)
	dsibtn.place(rely=0.54, relx=0.45)
	showappsbtn = Button(dispoptionswindow, text=options[13], compound=TOP, font=("Meera", 10, "bold"), image=showappsbtnicon, command=showapps)
	showappsbtn.place(rely=0.54, relx=0.69)
	runappbtn = Button(dispoptionswindow, text=options[14], compound=TOP, font=("Meera", 10, "bold"), image=runappbtnicon, command=runapp)
	runappbtn.place(rely=0.54, relx=0.890)
	downarrowbtn = Label(dispoptionswindow, image=downarrowicon)
	downarrowbtn.place(rely=0.92, relx=0.50)

	portforwardbtn.place_forget()
	grabwpasupbtn.place_forget()
	showmacipbtn.place_forget()
	ext_apkbtn.place_forget()
	netstatbtn.place_forget()
	togwifibtn.place_forget()
	unlockbtn.place_forget()
	batstatbtn.place_forget()

	#Binds
	downarrowbtn.bind("<ButtonRelease-1>", page2)
	dispoptionswindow.bind("<Control-c>", destoptnlistwind)
	dispoptionswindow.bind("<Control-h>", helpwindow)
	dispoptionswindow.bind("<Control-g>", github_page)

	#Pmw Balloons
	balloon = Pmw.Balloon(dispoptionswindow)
	balloon.bind(showdevs, "Show the amount of devices connected to the adb server")
	balloon.bind(connectbtn, "Connect a phone by internal or external ip address to the adb server")
	balloon.bind(disconnectbtn, "Disconnect all phones connected to the adb server")
	balloon.bind(adbshellbtn, "Use the command prompt to navigate through the android filesystem")
	balloon.bind(instapkbtn, "Install an apk to the desired phone")
	balloon.bind(screenrecbtn, "Record the screen and save the video to your computer")
	balloon.bind(screenshotbtn, "Take a screenshot and save the picture to your computer")
	balloon.bind(restservbtn, "Restart the adb server")
	balloon.bind(pullfoldersbtn, "Download folders from the android filesystem and save them to your computer")
	balloon.bind(turnoffdevbtn, "Send a command that turns off the device")
	balloon.bind(uninstappbtn, "Uninstall an app from the device")
	balloon.bind(rtlbtn, "View a real time log of the events happening on the device")
	balloon.bind(dsibtn, "Dump the system info of the device which will be saved as a text file on your computer")
	balloon.bind(showappsbtn, "Show apps that are installed on the device")
	balloon.bind(runappbtn, "Run an app that's installed on the device")
	balloon.bind(downarrowbtn, "View the next page of options")

def page2(*args):
	global dispoptionswindow
	global showdevs
	global connectbtn
	global disconnectbtn
	global adbshellbtn
	global instapkbtn
	global screenrecbtn
	global screenshotbtn
	global restservbtn
	global pullfoldersbtn
	global turnoffdevbtn
	global uninstappbtn
	global rtlbtn
	global dsibtn
	global showappsbtn
	global runappbtn
	global downarrowbtn
	global uparrowbtn
	global portforwardbtn
	global grabwpasupbtn
	global showmacipbtn
	global ext_apkbtn
	global netstatbtn
	global togwifibtn
	global unlockbtn
	global batstatbtn
	global options
	global dispoptionswindow

	#Hiding Objects
	showdevs.place_forget()
	connectbtn.place_forget()
	disconnectbtn.place_forget()
	adbshellbtn.place_forget()
	instapkbtn.place_forget()
	screenrecbtn.place_forget()
	screenshotbtn.place_forget()
	restservbtn.place_forget()
	pullfoldersbtn.place_forget()
	turnoffdevbtn.place_forget()
	uninstappbtn.place_forget()
	rtlbtn.place_forget()
	dsibtn.place_forget()
	showappsbtn.place_forget()
	runappbtn.place_forget()
	downarrowbtn.place_forget()

	#New Objects
	portforwardbtn = Button(dispoptionswindow, text=options[15], compound=TOP, font=("Meera", 10, "bold"), image=portfotwardicon, command=choosedev_port)
	portforwardbtn.place(relx=0.0)
	grabwpasupbtn = Button(dispoptionswindow, text=options[16], compound=TOP, font=("Meera", 10, "bold"), image=grabwpasupicon, command=grabwpasup)
	grabwpasupbtn.place(relx=0.19)
	showmacipbtn = Button(dispoptionswindow, text=options[17], compound=TOP, font=("Meera", 10, "bold"), image=showmacipicon, command=showip)
	showmacipbtn.place(relx=0.42)
	ext_apkbtn = Button(dispoptionswindow, text=options[18], compound=TOP, font=("Meera", 10, "bold"), image=ext_apkicon, command=selectingapk)
	ext_apkbtn.place(relx=0.66)
	batstatbtn = Button(dispoptionswindow, text=options[19], compound=TOP, font=("Meera", 10, "bold"), image=batstaticon, command=getbatterystatus)
	batstatbtn.place(relx=0.837)
	netstatbtn = Button(dispoptionswindow, text=options[20], compound=TOP, font=("Meera", 10, "bold"), image=netstaticon, command=shownetstat)
	netstatbtn.place(rely=0.25)
	togwifibtn = Button(dispoptionswindow, text=options[21], compound=TOP, font=("Meera", 10, "bold"), image=togwifiicon, command=toggle_wifi)
	togwifibtn.place(rely=0.25, relx=0.19)
	unlockbtn = Button(dispoptionswindow, text=options[22], compound=TOP, font=("Meera", 10, "bold"), image=unlockicon, command=removelock)
	unlockbtn.place(rely=0.25, relx=0.42)
	uparrowbtn = Label(dispoptionswindow, image=uparrowicon)
	uparrowbtn.place(rely=0.92, relx=0.50)
	#rootcheckerbtn = Button(dispoptionswindow, text=options[25], font=("Meera", 10, "bold"), command=rootchecker)
	#rootcheckerbtn.place(rely=0.92, relx=0.55)

	#Binds
	uparrowbtn.bind("<ButtonRelease-1>", page1)
	dispoptionswindow.bind("<Control-c>", destoptnlistwind)
	dispoptionswindow.bind("<Control-h>", helpwindow)
	dispoptionswindow.bind("<Control-g>", github_page)

	#Pmw
	Pmw.initialise(dispoptionswindow)
	balloon = Pmw.Balloon(dispoptionswindow)
	balloon.bind(uparrowbtn, "View the previous page of options")
	balloon.bind(portforwardbtn, "Port forward")
	balloon.bind(grabwpasupbtn, "Download a file which holds all the wifi names and passwords that the phone currently remembers")
	balloon.bind(showmacipbtn, "Reveal the ip or mac address of the device")
	balloon.bind(ext_apkbtn, "Extract an apk with the current user data in it save to your computer")
	balloon.bind(batstatbtn, "Get the status of the devices battery charge and overall condition")
	#balloon.bind(netstatbtn,)
	balloon.bind(togwifibtn, "Toggle the devices wifi interface on and off")
	balloon.bind(unlockbtn, "Remove the lockscreen passcode from the device.")

def logmsg():
	global chosendev
	global proc
	global listbox
	global logmsg_window

	logmsg_window = Toplevel()
	logmsg_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = logmsg_window.winfo_screenwidth()
	hs = logmsg_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	logmsg_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	logmsg_window_icon = Label(logmsg_window, image=logbtnicon)
	logmsg_window_icon.place(relx=0.21)
	logmsg_window_label = Label(logmsg_window, text="Press OK to start the log. \nWhen you're finished, press Ctrl + C to stop the log generation", font=("Meera", 10, "bold"))
	logmsg_window_label.place(relx=0.29, rely=0.08)
	logmsg_window_btn = Button(logmsg_window, text="OK", font=("Meera", 10, "bold"), command=startlog)
	logmsg_window_btn.place(relx=0.45, rely=0.5)

def startlog():
	global chosendev
	global proc
	global listbox
	global devip
	global logmsg_window

	logmsg_window.destroy()

	try:
		save_location = filedialog.asksaveasfilename(title="Save log", defaultextension=".log")
		with open(save_location, "w"):
			os.system("adb logcat > " + save_location)
			startlog_success_window = Toplevel()
			startlog_success_window.title("PhoneSploitGui")

			w = 500
			h = 70

			ws = startlog_success_window.winfo_screenwidth()
			hs = startlog_success_window.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			startlog_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
			startlog_success_window_icon = Label(startlog_success_window, image=logbtnicon)
			startlog_success_window_icon.place(relx=0.21)
			startlog_success_window_label = Label(startlog_success_window, text="Log has been generated and saved", font=("Meera", 10, "bold"))
			startlog_success_window_label.place(relx=0.29, rely=0.08)
			startlog_success_window_btn = Button(startlog_success_window, text="OK", font=("Meera", 10, "bold"))
			startlog_success_window_btn.place(relx=0.45, rely=0.5)
	except:
		startlog_err_window = Toplevel()
		startlog_err_window.title("PhoneSploitGui")

		w = 500
		h = 70

		ws = startlog_err_window.winfo_screenwidth()
		hs = startlog_err_window.winfo_screenheight()

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		startlog_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
		startlog_err_window_icon = Label(startlog_err_window, image=logbtnicon)
		startlog_err_window_icon.place(relx=0.21)
		startlog_err_window_label = Label(startlog_err_window, text="There was an error generating the log file. Check to see if the target has disconnected from the host.", font=("Meera", 10, "bold"))
		startlog_err_window_label.place(relx=0.29, rely=0.08)
		startlog_err_window_btn = Button(startlog_err_window, text="OK", font=("Meera", 10, "bold"), command=startlog_err_window.destroy)
		startlog_err_window_btn.place(relx=0.45, rely=0.5)

def clear_package_example(*args):
	global uninstpath_entry
	uninstpath_entry.delete(0, END)

def uninstallapp(*args):
	global chosendev
	global uninstpath_entry
	global uninstpath_window

	uninstpath = uninstpath_entry.get()
	uninstpath_window.destroy()
	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "-s", chosendev, "uninstall", uninstpath], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as result:
			data = result.read()
			if re.search(r"Unknown", data):
				uninstallapp_err_window = Toplevel()
				uninstallapp_err_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = uninstallapp_err_window.winfo_screenwidth()
				hs = uninstallapp_err_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				uninstallapp_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				uninstallapp_err_window_icon = Label(uninstallapp_err_window, image=uninstappbtnicon)
				uninstallapp_err_window_icon.place(relx=0.21)
				uninstallapp_err_window_label = Label(uninstallapp_err_window, text="The package specified wasn't found on the target device. \nIt's possible that it has been mispelled.", font=("Meera", 10, "bold"))
				uninstallapp_err_window_label.place(relx=0.29, rely=0.08)
				uninstallapp_err_window_btn = Button(uninstallapp_err_window, text="OK", command=uninstallapp_err_window.destroy)
				uninstallapp_err_window_btn.place(relx=0.45, rely=0.5)
			else:
				uninstallapp_success_window = Toplevel()
				uninstallapp_success_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = uninstallapp_success_window.winfo_screenwidth()
				hs = uninstallapp_success_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				uninstallapp_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				uninstallapp_success_icon = Label(uninstallapp_success_window, image=uninstappbtnicon)
				uninstallapp_success_icon.place(relx=0.10)
				uninstallapp_success_label = Label(uninstallapp_success_window, text="App has been successfully uninstalled from the target device", font=("Meera", 10, "bold"))
				uninstallapp_success_label.place(relx=0.18, rely=0.08)
				uninstallapp_success_btn = Button(uninstallapp_success_window, text="OK", font=("Meera", 10, "bold"), command=uninstallapp_success_window.destroy)
				uninstallapp_success_btn.place(relx=0.43, rely=0.5)

def package_sel():
	global chosendev
	global uninstpath_entry
	global uninstpath_window

	uninstpath_window = Toplevel()
	uninstpath_window.title("PhoneSploitGui")
	uninstpath_label = Label(uninstpath_window, text="Enter the package name of the app")
	uninstpath_label.pack()
	uninstpath_entry = Entry(uninstpath_window, width=50, bg="white", font=("Meera", 10, "bold"))
	uninstpath_entry.pack()
	uninstpath_entry.insert(0, "example: com.snapchat.android")
	uninstpath_entry.bind("<ButtonRelease-1>", clear_package_example)
	uninstpath_entry.bind("<Return>", uninstallapp)

	w = 500
	h = 50

	ws = uninstpath_window.winfo_screenwidth()
	hs = uninstpath_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	uninstpath_window.geometry("%dx%d+%d+%d" % (w, h, x, y))

def turnoffphone():
	global chosendev

	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "-s", chosendev, "reboot"], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as results:
			data = results.read()
			if re.search("error", data):
				poweroff_err = Toplevel()
				poweroff_err.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = poweroff_err.winfo_screenwidth()
				hs = poweroff_err.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				poweroff_err.geometry("%dx%d+%d+%d" % (w, h, x, y))
				poweroff_err_icon = Label(poweroff_err, image=poweroffbtnicon)
				poweroff_err_icon.place(relx=0.21)
				poweroff_err_label = Label(poweroff_err, text="There was an error attempting to turn off the device. Did it disconnect from the network?", font=("Meera", 10, "bold"))
				poweroff_err_label.place(relx=0.29, rely=0.08)
				poweroff_err_btn = Button(poweroff_err, text="OK", font=("Meera", 10, "bold"))
				poweroff_err_btn.place(relx=0.45, rely=0.5)
			else:
				poweroff_success = Toplevel()
				poweroff_success.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = poweroff_success.winfo_screenwidth()
				hs = poweroff_success.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				poweroff_success.geometry("%dx%d+%d+%d" % (w, h, x, y))
				poweroff_success_icon = Label(poweroff_success, image=poweroffbtnicon)
				poweroff_success_icon.place(relx=0.21)
				poweroff_success_label = Label(poweroff_success, text="Target device has been shutdown", font=("Meera", 10, "bold"))
				poweroff_success_label.place(relx=0.29, rely=0.08)
				poweroff_success_btn = Button(poweroff_success, text="OK", font=("Meera", 10, "bold"))
				poweroff_success_btn.place(relx=0.45, rely=0.5)

def closerestservpopup():
	global restserv_window
	restserv_window.destroy()

def restartadbserver():
	global restserv_window
	
	restserv_window = Toplevel()
	restserv_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = restserv_window.winfo_screenwidth()
	hs = restserv_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	restserv_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	restserv_iconlabel = Label(restserv_window, image=restservbtnicon)
	restserv_iconlabel.place(relx=0.27)
	restserv_labelmsg = Label(restserv_window, text="Adb server has been restarted", font=("Meera", 10, "bold"))
	restserv_labelmsg.place(relx=0.35, rely=0.1)
	restserv_button = Button(restserv_window, text="OK", font=("Meera", 10, "bold"), command=closerestservpopup)
	restserv_button.place(relx=0.48, rely=0.5)
	os.system("adb kill-server && adb start-server")

def clear_path_example(*args):
	global save_loc_window_entry

	save_loc_entry.delete(0, END)

def screenrec_save():
	global chosendev
	global screenrec_window

	save_location = filedialog.asksaveasfilename(title="Save video", defaultextension="mp4")
	os.system("adb -s " + chosendev + " pull /sdcard/screenrec.mp4 " + save_location)
	
	screenrec_save_window = Toplevel()
	screenrec_save_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = screenrec_save_window.winfo_screenwidth()
	hs = screenrec_save_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	screenrec_save_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	screenrec_save_window_icon = Label(screenrec_save_window, image=screenshotbtnicon)
	screenrec_save_window_icon.place(relx=0.21)
	screenrec_save_window_label = Label(screenrec_save_window, text="Video has been successfully saved", font=("Meera", 10, "bold"))
	screenrec_save_window_label.place(relx=0.29, rely=0.08)
	screenrec_save_window_btn = Button(screenrec_save_window, text="OK", font=("Meera", 10, "bold"))
	screenrec_save_window_btn.place(relx=0.45, rely=0.5)

def screenrec_proc():
	global chosendev
	global screenrec_window

	screenrec_window.destroy()
	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "-s", chosendev, "shell", "screenrecord", "/sdcard/screenrec.mp4"], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as results:
			data = results.read()
			if re.search("device offline", data):
				screenrec_devoffline_window = Toplevel()
				screenrec_devoffline_window.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = screenrec_devoffline_window.winfo_screenwidth()
				hs = screenrec_devoffline_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				screenrec_devoffline_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				screenrec_devoffline_window_icon = Label(screenrec_devoffline_window, image=screenrecbtnicon)
				screenrec_devoffline_window_icon.place(relx=0.17)
				screenrec_devoffline_window_label = Label(screenrec_devoffline_window, text="Device is offline. Disconnect and reconnect to it to see \nif that solves the problem", font=("Meera", 10, "bold"))
				screenrec_devoffline_window_label.place(relx=0.23, rely=0.08)
				screenrec_devoffline_window_btn = Button(screenrec_devoffline_window, text="OK", font=("Meera", 10, "bold"), command=screenrec_devoffline_window.destroy)
				screenrec_devoffline_window_btn.place(relx=0.45, rely=0.55)
			elif re.search("output buffers", data):
				screenrec_OB_window = Toplevel()
				screenrec_OB_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = screenrec_OB_window.winfo_screenwidth()
				hs = screenrec_OB_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				screenrec_OB_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				screenrec_OB_window_icon = Label(screenrec_OB_window, image=screenrecbtnicon)
				screenrec_OB_window_icon.place(relx=0.21)
				screenrec_OB_window_label = Label(screenrec_OB_window, text="Unable to get output buffers. \nThis means you need to reduce the resolution of the screen recording. \nClick the adb shell button and type in the terminal adb -s [ip address] shell screenrecord /sdcard/screenrec.mp4 --size 1280x720", font=("Meera", 10, "bold"))
				screenrec_OB_window_label.place(relx=0.29, rely=0.08)
				screenrec_OB_window_btn = Button(screenrec_OB_window, text="OK", font=("Meera", 10, "bold"), command=screenrec_OB_window.destroy)
				screenrec_OB_window_btn.place(relx=0.45, rely=0.5)
			elif re.search("not found", data):
				screenrec_NF_window = Toplevel()
				screenrec_NF_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = screenrec_NF_window.winfo_screenwidth()
				hs = screenrec_NF_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				screenrec_NF_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				screenrec_NF_window_icon = Label(screenrec_NF_window, image=screenrecbtnicon)
				screenrec_NF_window_icon.place(relx=0.21)
				screenrec_NF_window_label = Label(screenrec_NF_window, text="Device not found. The session may have either timed \nout, the user left the network, or \nthe user changed network interfaces", font=("Meera", 10, "bold"))
				screenrec_NF_window_label.place(relx=0.29, rely=0.08)
				screenrec_NF_window_btn = Button(screenrec_NF_window, text="OK", font=("Meera", 10, "bold"), command=screenrec_NF_window.destroy)
				screenrec_NF_window_btn.place(relx=0.45, rely=0.5)
			else:
				screenrec_window = Toplevel()
				screenrec_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = screenrec_window.winfo_screenwidth()
				hs = screenrec_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				screenrec_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				screenrec_window_icon = Label(screenrec_window, image=screenrecbtnicon)
				screenrec_window_icon.place(relx=0.21)
				screenrec_window_label = Label(screenrec_window, text="Recording is done. Choose where you want to save the video", font=("Meera", 10, "bold"))
				screenrec_window_label.place(relx=0.29, rely=0.08)
				screenrec_window_btn = Button(screenrec_window, text="OK", font=("Meera", 10, "bold"), command=screenrec_window.destroy)
				screenrec_window_btn.place(relx=0.45, rely=0.5)

def screenrecord():
	global chosendev
	global save_loc_window_entry
	global screenrec_window

	screenrec_window = Toplevel()
	screenrec_window.title("PhoneSploitGui")

	w = 500
	h = 70

	ws = screenrec_window.winfo_screenwidth()
	hs = screenrec_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	screenrec_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	screenrec_window_icon = Label(screenrec_window, image=screenrecbtnicon)
	screenrec_window_icon.place(relx=0.21)
	screenrec_window_label = Label(screenrec_window, text="Click OK to start screen recording", font=("Meera", 10, "bold"))
	screenrec_window_label.place(relx=0.29, rely=0.08)
	screenrec_window_btn = Button(screenrec_window, text="OK", font=("Meera", 10, "bold"), command=screenrec_proc)
	screenrec_window_btn.place(relx=0.45, rely=0.5)

def instapk(*args):
	global chosendev
	global instpath_window
	global instpath_entry
	global apkpath

	apkpath = instpath_entry.get()
	instpath_window.destroy()
	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "-s", chosendev, "install", apkpath], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as results:
			data = results.read()
			if re.search(r"error", data):
				instapk_err_window = Toplevel()
				instapk_err_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = instapk_err_window.winfo_screenwidth()
				hs = instapk_err_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				instapk_err_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				instapk_err_window_icon = Label(instapk_err_window, image=instapkbtnicon)
				instapk_err_window_icon.place(relx=0.29)
				instapk_err_window_label = Label(instapk_err_window, text="Unable to install apk. Target might have disconnected from the network. \nClick Show Devices to see if you're still connected to the intended target", font=("Meera", 10, "bold"))
				instapk_err_window_label.place(relx=0.35, rely=0.1)
				instapk_err_window_btn = Button(instapk_err_window, text="OK", font=("Meera", 10, "bold"), command=instapk_err_window.destroy)
				instapk_err_window_btn.place(relx=0.48, rely=0.5)
			else:
				instapk_success_window = Toplevel()
				instapk_success_window.title("PhoneSploitGui")

				w = 500
				h = 70

				ws = instapk_success_window.winfo_screenwidth()
				hs = instapk_success_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				instapk_success_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				instapk_success_window_icon = Label(instapk_success_window, image=instapkbtnicon)
				instapk_success_window_icon.place(relx=0.29)
				instapk_success_window_label = Label(instapk_success_window, text="Apk has been installed to target device", font=("Meera", 10, "bold"))
				instapk_success_window_label.place(relx=0.35, rely=0.1)
				instapk_success_window_btn = Button(instapk_success_window, text="OK", font=("Meera", 10, "bold"), command=instapk_err_window.destroy)
				instapk_success_window_btn.place(relx=0.48, rely=0.5)

def apkinstpath():
	global chosendev
	global instpath_window
	global instpath_entry

	instpath_window = Toplevel()
	instpath_window.title("PhoneSploitGui")

	w = 500
	h = 50

	ws = instpath_window.winfo_screenwidth()
	hs = instpath_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	instpath_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	instpath_label = Label(instpath_window, text="Enter the path of where you want the apk installed", font=("Meera", 10, "bold"))
	instpath_label.pack()

	instpath_entry = Entry(instpath_window, width=50, bg="white", font=("Meera", 10, "bold"))
	instpath_entry.bind("<Return>", instapk)
	instpath_entry.pack()

def openshell():
	global chosendev
	os.system("adb -s " + chosendev + " shell")

def disconnect_devices():
	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "disconnect"], stdout=f, stderr=f))
		f.write(proc)
		readfile()

def showdevsconnected():
	with open("connected_devices.log", "w") as f:
		proc = str(subprocess.call(["adb", "devices", "-l"], stdout=f, stderr=f))
		f.write(proc)
		with open("connected_devices.log", "r") as results:
			showdevsconnected_window = Toplevel()
			showdevsconnected_window.title("PhoneSploitGui")

			w = 400
			h = 310

			ws = showdevsconnected_window.winfo_screenwidth()
			hs = showdevsconnected_window.winfo_screenheight()

			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)

			showdevsconnected_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
			showdevsconnected_textbox = Text(showdevsconnected_window, width=80, height=15, bg="white", font=("Meera", 10, "bold"))
			showdevsconnected_textbox.insert(END, results.read())
			showdevsconnected_textbox.pack()
			showdevsconnected_btn = Button(showdevsconnected_window, text="OK", font=("Meera", 10, "bold"), command=showdevsconnected_window.destroy)
			showdevsconnected_btn.pack()

def clear_ip_example(*args):
	global devip
	devip.delete(0, END)

def clear_connect_no_new_window_example(*args):
	global enterip_window_entry
	enterip_window_entry.delete(0, END)

def connect_no_new_window(*args):
	global devip
	global listbox
	global chooseip
	global root
	global chosendev
	global enterip_window
	global enterip_window_entry

	enterip_window = Toplevel()
	enterip_window.title("PhoneSploitGui")

	w = 500
	h = 80

	ws = enterip_window.winfo_screenwidth()
	hs = enterip_window.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	enterip_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
	enterip_window_label = Label(enterip_window, text="Enter an internal or external ip address of a phone.", font=("Meera", 10, "bold"))
	enterip_window_label.pack()
	enterip_window_entry = Entry(enterip_window, width=50, bg="white", font=("Meera", 10, "bold"))
	enterip_window_entry.pack()
	enterip_window_entry.insert(0, "example: 192.168.1.1")
	enterip_window_entry.bind("<Return>", new_device_connected)
	enterip_window_entry.bind("<ButtonRelease-1>", clear_connect_no_new_window_example)

	with open("connected_devices.txt", "w") as f:
		proc = str(subprocess.call(["adb", "connect", chosendev], stdout=f, stderr=f))
		f.write(proc)
		with open("connected_devices.txt", "r") as results:
			data = results.read()
			if re.search("Connected", data):

				connected_window = Toplevel()
				connected_window.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = connected_window.winfo_screenwidth()
				hs = connected_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				connected_window_icon = Label(connected_window, image=connected_dev_btn)
				connected_window_icon.place(relx=0.29)
				connected_window_label = Label(connected_window, text="Successfully connected to device")
				connected_window_label.place(relx=0.35, rely=0.1)
				connected_window_btn = Button(conected_window, text="OK", font=("Meera", 10, "bold"))
				connected_window_btn.place(relx=0.48, rely=0.5)






def displayoptions(*args):
	global dispoptionswindow
	global chosendev
	global instpath_window
	global instpath_entry
	global apkpath
	global showdevs
	global connectbtn
	global disconnectbtn
	global adbshellbtn
	global instapkbtn
	global screenrecbtn
	global screenshotbtn
	global restservbtn
	global pullfoldersbtn
	global turnoffdevbtn
	global uninstappbtn
	global rtlbtn
	global dsibtn
	global showappsbtn
	global runappbtn
	global downarrowbtn
	global options
	global dispoptionswindow
	global enterip_window

	dispoptionswindow = Toplevel()
	dispoptionswindow.title("Options")
	Pmw.initialise(dispoptionswindow)

	w = 870
	h = 350

	ws = dispoptionswindow.winfo_screenwidth()
	hs = dispoptionswindow.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	dispoptionswindow.geometry("%dx%d+%d+%d" % (w, h, x, y))

	options = ["Show connected devices", "Connect a phone", "Disconnect a phone", "Enter adb shell", 
	"Install apk \nto phone", "Screen record", "Screenshot", "Restart adb server", 
	"Download folders \nfrom phone", "Turn off phone", "Uninstall an app", "Real time log", "Dump System Info",
	"Show apps on phone", "Run an app", "Port Forwarding", "Grab wpa supplicant \n*Device must be rooted*", "Show Mac/IP Address", "Extract an apk", 
	"Get battery status", "Netstat", "Turn WiFi On/Off", "Remove lockscreen \n passcode \n*Device must be rooted*", "Use keycode", "Get current activity",
	"Root Checker"]

	menu = Menu(dispoptionswindow)
	submenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="File", menu=submenu, font=("Meera", 12, "bold"))
	submenu.add_command(label="Close", font=("Meera", 12, "bold"), compound=LEFT, command=destoptnlistwind, image=exitmenuicon, accelerator="Ctrl+C")

	submenu = Menu(menu, tearoff=False)
	menu.add_cascade(label="Help", menu=submenu, font=("Meera", 12, "bold"))
	submenu.add_command(label="Info", font=("Meera", 12, "bold"), compound=LEFT, image=infomenuicon, command=helpwindow, accelerator="Ctrl+H")
	submenu.add_command(label="Report Issues", compound=LEFT, font=("Meera", 12, "bold"), image=issuesmenuicon, accelerator="Ctrl+R")
	submenu.add_command(label="Visit my github page", compound=LEFT, font=("Meera", 12, "bold"), command=github_page, image=githubicon, accelerator="Ctrl+G")

	dispoptionswindow.config(menu=menu)

	showdevs = Button(dispoptionswindow, text=options[0], compound=TOP, font=("Meera", 10, "bold"), image=showdevsbtnicon, command=showdevsconnected)
	showdevs.place(relx=0.0)
	connectbtn = Button(dispoptionswindow, text=options[1], compound=TOP, font=("Meera", 10, "bold"), image=connectbtnicon, command=connect_no_new_window)
	connectbtn.place(relx=0.25)
	disconnectbtn = Button(dispoptionswindow, text=options[2], compound=TOP, font=("Meera", 10, "bold"), image=disconnectbtnicon, command=disconnect_devices)
	disconnectbtn.place(relx=0.45)
	adbshellbtn = Button(dispoptionswindow, text=options[3], compound=TOP, font=("Meera", 10, "bold"), image=shellbtnicon, command=openshell)
	adbshellbtn.place(relx=0.69, relheight=0.197)
	instapkbtn = Button(dispoptionswindow, text=options[4], compound=TOP, font=("Meera", 10, "bold"), image=instapkbtnicon, command=apkinstpath)
	instapkbtn.place(relx=0.890, relheight=0.197)
	screenrecbtn = Button(dispoptionswindow, text=options[5], compound=TOP, font=("Meera", 10, "bold"), image=screenrecbtnicon, command=screenrecord)
	screenrecbtn.place(rely=0.27)
	screenshotbtn = Button(dispoptionswindow, text=options[6], compound=TOP, font=("Meera", 10, "bold"), image=screenshotbtnicon, command=screenshot)
	screenshotbtn.place(rely=0.27, relx=0.25, relheight=0.197)
	restservbtn = Button(dispoptionswindow, text=options[7], compound=TOP, font=("Meera", 10, "bold"), image=restservbtnicon, command=restartadbserver)
	restservbtn.place(rely=0.27, relx=0.45)
	pullfoldersbtn = Button(dispoptionswindow, text=options[8], compound=TOP, font=("Meera", 10, "bold"), image=dloadfromdevbtnicon, command=download_folders)
	pullfoldersbtn.place(rely=0.27, relx=0.69, relheight=0.197)
	turnoffdevbtn = Button(dispoptionswindow, text=options[9], compound=TOP, font=("Meera", 10, "bold"), image=poweroffbtnicon, command=turnoffphone)
	turnoffdevbtn.place(rely=0.27, relx=0.865)
	uninstappbtn = Button(dispoptionswindow, text=options[10], compound=TOP, font=("Meera", 10, "bold"), image=uninstappbtnicon, command=package_sel)
	uninstappbtn.place(rely=0.54)
	rtlbtn = Button(dispoptionswindow, text=options[11], compound=TOP, font=("Meera", 10, "bold"), image=logbtnicon, command=logmsg)
	rtlbtn.place(rely=0.54, relx=0.25)
	dsibtn = Button(dispoptionswindow, text=options[12], compound=TOP, font=("Meera", 10, "bold"), image=dsibtnicon, command=dumpsys_save_location)
	dsibtn.place(rely=0.54, relx=0.45)
	showappsbtn = Button(dispoptionswindow, text=options[13], compound=TOP, font=("Meera", 10, "bold"), image=showappsbtnicon, command=showapps)
	showappsbtn.place(rely=0.54, relx=0.69)
	runappbtn = Button(dispoptionswindow, text=options[14], compound=TOP, font=("Meera", 10, "bold"), image=runappbtnicon, command=selpack_run)
	runappbtn.place(rely=0.54, relx=0.890)
	downarrowbtn = Label(dispoptionswindow, image=downarrowicon)
	downarrowbtn.place(rely=0.92, relx=0.50)

	#Binds
	downarrowbtn.bind("<ButtonRelease-1>", page2)
	dispoptionswindow.bind("<Control-c>", destoptnlistwind)
	dispoptionswindow.bind("<Control-h>", helpwindow)
	dispoptionswindow.bind("<Control-g>", github_page)

	#Pmw Balloons
	balloon = Pmw.Balloon(dispoptionswindow)
	balloon.bind(showdevs, "Show the amount of devices connected to the adb server")
	balloon.bind(connectbtn, "Connect a phone by internal or external ip address to the adb server")
	balloon.bind(disconnectbtn, "Disconnect all phones connected to the adb server")
	balloon.bind(adbshellbtn, "Use the command prompt to navigate through the android filesystem")
	balloon.bind(instapkbtn, "Install an apk to the desired phone")
	balloon.bind(screenrecbtn, "Record the screen and save the video to your computer")
	balloon.bind(screenshotbtn, "Take a screenshot and save the picture to your computer")
	balloon.bind(restservbtn, "Restart the adb server")
	balloon.bind(pullfoldersbtn, "Download folders from the android filesystem and save them to your computer")
	balloon.bind(turnoffdevbtn, "Send a command that turns off the device")
	balloon.bind(uninstappbtn, "Uninstall an app from the device")
	balloon.bind(rtlbtn, "View a real time log of the events happening on the device")
	balloon.bind(dsibtn, "Dump the system info of the device which will be saved as a text file on your computer")
	balloon.bind(showappsbtn, "Show apps that are installed on the device")
	balloon.bind(runappbtn, "Run an app that's installed on the device")
	balloon.bind(downarrowbtn, "View the next page of options")

def readfile():
	with open("output.txt", "r") as f:
		listbox.insert(0, f.read())

def connect_device(*args):
	global devip
	global listbox
	global chooseip
	global root
	global chosendev
	global connected_dev_icon

	chosendev = devip.get()
	with open("output.txt", "w") as f:
		proc = str(subprocess.call(["adb", "connect", chosendev], stdout=f, stderr=f))
		f.write(proc)
		with open("output.txt", "r") as result:
			data = result.read()
			if re.search("Connection refused", data):
				no_connect_window = Toplevel()
				no_connect_window.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = no_connect_window.winfo_screenwidth()
				hs = no_connect_window.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				no_connect_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				no_connect_icon = Label(no_connect_window, image=disconnectbtnicon)
				no_connect_icon.place(relx=0.21)
				no_connect_label = Label(no_connect_window, text="Unable to connect to the target device. \nMake sure the ip address is typed in correctly.", font=("Meera", 10, "bold"))
				no_connect_label.place(relx=0.29, rely=0.08)
				no_connect_btn = Button(no_connect_window, text="OK", command=no_connect_window.destroy)
				no_connect_btn.place(relx=0.45, rely=0.59)
			elif re.search("connected", data):
				connected_dev = Toplevel()
				connected_dev.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = connected_dev.winfo_screenwidth()
				hs = connected_dev.winfo_screenheight()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				connected_dev.geometry("%dx%d+%d+%d" % (w, h, x, y))
				connected_dev_icon = Label(connected_dev, image=connectbtnicon)
				connected_dev_icon.place(relx=0.21)
				connected_dev_label = Label(connected_dev, text="Sucessfully connected to target device", font=("Meera", 10, "bold"))
				connected_dev_label.place(relx=0.29, rely=0.08)
				connected_dev_btn = Button(connected_dev, text="OK", font=("Meera", 10, "bold"), command=connected_dev.destroy)
				connected_dev_btn.place(relx=0.45, rely=0.59)
				chooseip.destroy()
				displayoptions()
			elif re.search("No route", data):
				netnoroute_window = Toplevel()
				netnoroute_window.title("PhoneSploitGui")

				w = 500
				h = 80

				ws = netnoroute_window.winfo_screenheight()
				hs = netnoroute_window.winfo_screenwidth()

				x = (ws/2) - (w/2)
				y = (hs/2) - (h/2)

				netnoroute_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
				netnoroute_window_icon = Label(netnoroute_window, image=disconnectbtnicon)
				netnoroute_window_icon.place(relx=0.18)
				netnoroute_window_label = Label(netnoroute_window, text="No route to host. Check if you've typed in the \ncorrect IP address.", font=("Meera", 10, "bold"))
				netnoroute_window_label.place(relx=0.25, rely=0.08)
				netnoroute_window_btn = Button(netnoroute_window, text="OK", font=("Meera", 10, "bold"), command=netnoroute_window.destroy)
				netnoroute_window_btn.place(relx=0.45, rely=0.59)
			else:
				if re.search("is unreachable", data):
					netunreach_window = Toplevel()
					netunreach_window.title("PhoneSploitGui")

					w = 500
					h = 80

					ws = netunreach_window.winfo_screenwidth()
					hs = netunreach_window.winfo_screenheight()

					x = (ws/2) - (w/2)
					y = (hs/2) - (h/2)

					netunreach_window.geometry("%dx%d+%d+%d" % (w, h, x, y))
					netunreach_window_icon = Label(netunreach_window, image=disconnectbtnicon)
					netunreach_window_icon.place(relx=0.14)
					netunreach_window_label = Label(netunreach_window, text="Device is unreachable.", font=("Meera", 10, "bold"))
					netunreach_window_label.place(relx=0.22, rely=0.08)
					netunreach_window_btn = Button(netunreach_window, text="OK", font=("Meera", 10, "bold"), command=netunreach_window.destroy)
					netunreach_window_btn.place(relx=0.45, rely=0.6)

def withdraw_attn_window(*args):
	global devip
	global listbox
	global chooseip
	global root
	global chosendev

	Attnwindow.withdraw()
	os.system("adb tcpip 5555")
	
	chooseip = Toplevel()

	w = 500
	h = 50

	ws = chooseip.winfo_screenwidth()
	hs = chooseip.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	chooseip.geometry("%dx%d+%d+%d" % (w, h, x, y))
	chooseip.title("PhoneSploitGui")
	chooseip.deiconify()
	ipmsg = ttk.Label(chooseip, text="Enter an internal or external ip address of a phone.", font=("Meera", 10, "bold"))
	ipmsg.pack()
	devip = Entry(chooseip, width=50, bg="white", font=("Meera", 10, "bold"))
	devip.insert(0, "example: 192.168.1.1")
	devip.pack()
	devip.bind("<Return>", connect_device)
	devip.bind("<ButtonRelease-1>", clear_ip_example)

Attnwindow = tk.ThemedTk()
Attnwindow.get_themes()
Attnwindow.set_theme("clam")

#icons
phonesploitguiicon = PhotoImage(file="icons/phonesploitguilogo.png")
disconnectbtnicon = PhotoImage(file="icons/disconnect.png")
connectbtnicon = PhotoImage(file="icons/connect.png")
shellbtnicon = PhotoImage(file="icons/shell.png")
showdevsbtnicon = PhotoImage(file="icons/phone.png")
instapkbtnicon = PhotoImage(file="icons/apkfile.png")
screenrecbtnicon = PhotoImage(file="icons/screenrecord.png")
screenshotbtnicon = PhotoImage(file="icons/screenshot.png")
restservbtnicon = PhotoImage(file="icons/restartserver.png")
dloadfromdevbtnicon = PhotoImage(file="icons/downloadfromphone.png")
poweroffbtnicon = PhotoImage(file="icons/poweroff.png")
uninstappbtnicon = PhotoImage(file="icons/uninstallapp.png")
logbtnicon = PhotoImage(file="icons/log.png")
showappsbtnicon = PhotoImage(file="icons/phoneapps.png")
dsibtnicon = PhotoImage(file="icons/dumpsysinfo.png")
runappbtnicon = PhotoImage(file="icons/runapp.png")
infomenuicon = PhotoImage(file="icons/info.png")
exitmenuicon = PhotoImage(file="icons/exit.png")
issuesmenuicon = PhotoImage(file="icons/issues.png")
downarrowicon = PhotoImage(file="icons/downarrow.png")
uparrowicon = PhotoImage(file="icons/uparrow.png")
portfotwardicon = PhotoImage(file="icons/portforward.png")
grabwpasupicon = PhotoImage(file="icons/grabwpasup.png")
showmacipicon = PhotoImage(file="icons/ip.png")
ext_apkicon = PhotoImage(file="icons/extract.png")
batstaticon = PhotoImage(file="icons/batterystatus.png")
githubicon = PhotoImage(file="icons/githubicon.png")
netstaticon = PhotoImage(file="icons/netstaticon.png")
togwifiicon = PhotoImage(file="icons/wifiicon.png")
unlockicon = PhotoImage(file="icons/unlock.png")

#Menu
menu = Menu(Attnwindow)
submenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=submenu, font=("Meera", 12, "bold"))
submenu.add_command(label="Close", font=("Meera", 12, "bold"), image=exitmenuicon, compound=LEFT, command=Attnwindow.destroy, accelerator="Ctrl+C")

submenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=submenu, font=("Meera", 12, "bold"))
submenu.add_command(label="Info", font=("Meera", 12, "bold"), compound=LEFT, command=helpwindow, image=infomenuicon, accelerator="Ctrl+H")
submenu.add_command(label="Report Issues", compound=LEFT, font=("Meera", 12, "bold"), image=issuesmenuicon, accelerator="Ctrl+R")
submenu.add_command(label="Visit my github page", compound=LEFT, font=("Meera", 12, "bold"), command=github_page, image=githubicon, accelerator="Ctrl+G")

#Binds
Attnwindow.bind("<Control-c>", closeattnwindow)
Attnwindow.bind("<Control-h>", helpwindow)
Attnwindow.bind("<Control-g>", github_page)

#Attention Window
Attnwindow.title("ATTENTION!")
Attnwindow.geometry("1920x1080")
Attntitle = Label(Attnwindow, text="WARNING", font=("Meera", 14, "bold"))
Attntitle.pack()
Attnwindow.iconphoto(True, phonesploitguiicon)
Attntext = Label(Attnwindow, text="\n\nThis program is to be used for educational or personal uses only. \nI do not promote or condone unethical hacking of any sort. If you get in trouble using this program, I'm not responsible. \nClick OK to continue.", font=("Meera", 20, "bold"))
Attntext.pack()
attnimgopen = PhotoImage(file="icons/attention.png")
attnimg = Label(image=attnimgopen)
attnimg.pack()
OKBtn = ttk.Button(Attnwindow, text="OK", command=withdraw_attn_window,)
OKBtn.pack(ipadx=50)

Attnwindow.config(menu=menu)
Attnwindow.mainloop()