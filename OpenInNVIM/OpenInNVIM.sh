file_path="$1"
directory_name="$(dirname $file_path)"
file_name="$(basename $file_path)"

osascript -  "$directory_name" "$file_name"  <<EOF

    on run argv -- argv is a list of strings
        tell application "Terminal"
            activate
            do script ("cd " & quoted form of item 1 of argv & "&& clear && nvim " & quoted form of item 2 of argv)
        end tell
    end run

EOF
	


