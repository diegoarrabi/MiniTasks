#!/bin/zsh

APP_NAME="MarkEdit"
APP_PARAMETERS="/Users/diegoibarra/Desktop/ADHD Tasks.md"

pkill -i $APP_NAME
sleep 1
open -a $APP_NAME $APP_PARAMETERS


# osascript <<EOF
# on run {}
# 	set counter to 0
# 	tell application "System Events"
# 		if (name of processes) contains "Typora" then
# 			tell process "Typora"
# 				repeat until exists (title of window 1)
# 					set counter to (counter + 1)
# 					if counter is greater than 300 then
# 						error number -128
# 					end if
# 				end repeat
# 				log "Step 1"
				
				
# 				set counter to 0
# 				repeat until (title of window 1) is equal to ""
# 					set counter to (counter + 1)
# 					if counter is greater than 300 then
# 						error number -128
# 					end if
# 				end repeat
# 				log "Step 2"
				
# 				set all_ui_elements to entire contents of window 1
# 				repeat with ui_element in all_ui_elements
# 					set ui_identifier to (title of ui_element) contains "Not Now"
# 					if ui_identifier then
# 						log ui_element
# 						click ui_element
# 					end if
# 				end repeat
# 				log "Step 3"
				
# 				set all_ui_elements to entire contents of window 2
# 				repeat with ui_element in all_ui_elements
# 					set ui_identifier to (title of ui_element) contains "UNREGISTERED"
# 					if ui_identifier then
# 						log ui_element
# 						click ui_element
# 					end if
# 				end repeat
# 				log "Step 4"
				
# 				set counter to 0
# 				repeat until (title of window 1) is equal to ""
# 					set counter to (counter + 1)
# 					if counter is greater than 300 then
# 						error number -128
# 					end if
# 				end repeat
# 				log "Step 5"
				
# 				set all_ui_elements to entire contents of window 1
# 				repeat with ui_element in all_ui_elements
# 					set ui_identifier to (title of ui_element) contains "Not Now"
# 					if ui_identifier then
# 						log ui_element
# 						click ui_element
# 					end if
# 				end repeat
# 				log "END"
# 			end tell
# 		end if
# 	end tell
# end run
# EOF





