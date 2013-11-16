ignoring application responses
	tell application "System Events" to tell process "SystemUIServer"
		tell (menu bar item 1 of menu bar 1 whose description is "text input")
			click
			click menu item "Swedish - Pro" of menu 1
		end tell
	end tell
end ignoring

