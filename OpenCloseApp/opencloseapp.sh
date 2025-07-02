#!/bin/zsh

APP_NAME="MarkEdit"

osascript_str=$(cat<<EOD
tell application "$APP_NAME" to quit
EOD
)
osascript -e $osascript_str
sleep 1


osascript_str=$(cat <<EOD
on appFrontmost(app_name)
	tell application "System Events" to name of (first application process whose frontmost is true) is app_name
end appFrontmost

on repositionApp(app_name)
	tell application "System Events"
		tell application "Finder" to set screen_size to bounds of window of desktop
		set _WINDOW to front window of (first application process whose frontmost is true)
		set finalPosition to {0, 0}
		tell _WINDOW to set {position} to {finalPosition}
	end tell
end repositionApp

on run {}
	set app_name to "${APP_NAME}"
	launch application app_name
	(*
	set app_id to (get id of application app_name)
	
	set cycle_delay to 0.5
	set total_cycle to 10
	set num to 0
	
	repeat
		if appFrontmost(app_name) then
			my repositionApp(app_name)
			exit repeat
		else
			set total_cycle to (total_cycle + 1)
			delay cycle_delay
		end if
		if total_cycle < 0 then
			exit repeat
		end if
	end repeat
	*)
end run
EOD
)
osascript -e $osascript_str

# osascript <<EOD
#     set script_path to quoted form of "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/ES-DS Setup/es-de.py"
#     set app_name to "ES-DE"
# 	set previous_app to (path to frontmost application as text)
# 	activate application app_name
# 	delay 0.5
#     do shell script script_path
# 	activate application previous_app
# EOD