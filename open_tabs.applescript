tell application "Google Chrome"
	
	set myFile to open for access (choose file name) with write permission
	set windowNumber to 1
	repeat the number of windows times
		set myTabs to every tab of window windowNumber
		write "----- Window Number " & windowNumber & " -----

" to myFile
		set tabNumber to 0
		repeat with aTab in myTabs
			
			set tabTitle to title of aTab & "
"
			write tabTitle to myFile
			set tabURL to URL of aTab & "

"
			write tabURL to myFile
			set tabNumber to tabNumber + 1
			
		end repeat
		
		write "Window Number: " & windowNumber & " Number of tabs: " & tabNumber & "

" to myFile
		set windowNumber to windowNumber + 1
	end repeat
	close access myFile
	
end tell