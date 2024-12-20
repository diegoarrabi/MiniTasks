on run {}
	activate application "Finder"
	tell application "System Events" to tell process "Finder"
		
		--View as Columns
		click menu item "as Columns" of menu "View" of menu bar 1
		
		--Check If Groups Activated
		set use_groups to ((value of attribute "AXMenuItemMarkChar" of menu item "Use Groups" of menu "View" of menu bar 1) is not missing value)
		
		--Turn Groups Off OR Continue
		if use_groups is true then
			click menu item "Use Groups" of menu "View" of menu bar 1
			log "Toggled Groups OFF"
		end if
		
		--Sort UnGrouped by Name
		my sortName()
		
		--Turn Groups On
		click menu item "Use Groups" of menu "View" of menu bar 1
		log "Toggled Groups ON"
		
		--Sort Groups by Kind
		my groupKind()
		
	end tell
end run


on sortName()
	set counter to 0
	tell application "System Events" to tell process "Finder"
		--Sort by Name (Repeat in place for when waiting for menu items to update then Groups Toggled to Off)
		repeat until (title of menu item 1 of menu 1 of menu item 7 of menu "View" of menu bar 1) is "Name"
			set counter to (counter + 1)
			if counter is equal to 1 then log "Waiting until Menu Items Update"
			if counter is greater than 100 then error number -128
		end repeat
		click menu item "Name" of menu "Sort By" of menu item "Sort By" of menu "View" of menu bar 1
		log "Sorted by Name"
	end tell
end sortName


on groupKind()
	set counter to 0
	tell application "System Events" to tell process "Finder"
		--Group by Kind (Repeat in place for when waiting for menu items to update then Groups Toggled to On)
		repeat until (title of menu item 1 of menu 1 of menu item 7 of menu "View" of menu bar 1) is "None"
			set counter to (counter + 1)
			if counter is equal to 1 then log "Waiting until Menu Items Update"
			if counter is greater than 100 then error number -128
		end repeat
		click menu item "Kind" of menu "Group By" of menu item "Group By" of menu "View" of menu bar 1
		log "Grouped by Kind"
	end tell
end groupKind