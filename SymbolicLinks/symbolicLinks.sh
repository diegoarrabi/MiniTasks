#!/bin/zsh


FILES_TO_SYMLINK=(
    "/Users/diegoibarra/Developer/1_myProjects/MiniProjects/NestControl/nest"
    "/Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/workdir"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/RandomText/randomText"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/FontScriptName/fontScriptName"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/CreateIconSet/createIconSet"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/TestDialog/testDialog"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/Preview256Colors/preview256colors"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/Touchd/touchd"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/Datetimed/datetimed"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/EchoEachPath/echoPath"
    "/Users/diegoibarra/Developer/1_myProjects/MiniTasks/Figletd/figletd"
)


ERROR_LIST=()
destination_path="/usr/local/bin"
term_rows=$(tput lines)

echo "\x1b[2J""\x1b[H"
for cmd_path in $FILES_TO_SYMLINK; do
    
    # IF PATH EXISTS
    if [ -e "$cmd_path" ]; then
        # printf "%-25s %s\n" "Source Path Exists: " "${cmd_path}"
        set_permissions="$(chmod u+x $cmd_path)"
        makeSymLink="$(ln -s ${cmd_path} ${destination_path})"
        command_name="${destination_path}/${cmd_path##*/}"
        
        # printf "%-25s %s\n" "Command Symlink: " "${command_name}"
        readlink_output="$(readlink -f ${command_name})"
        # printf "%-25s %s\n" "Command Absolute link: " "${readlink_output}"
        echo "$readlink_output"
        echo "  ┖━━━━▶  $command_name\n"
        sleep 1
    else  
        printf "%-25s %s\n" "DOES NOT EXIST: " "${cmd_path}"
        ERROR_LIST+=$cmd_path
        echo "\x1b[5B"
        read -qs "?Continue? $p? (n/y)"
        read_exit_status=$?
        
        # EXIT STATUS -> 1 IF NO
        if [ $read_exit_status -eq 1 ]; then
            echo "\x1b[5A"
            break
        fi
    fi
done

if [ ${#ERROR_LIST} -ne 0 ]; then
    echo "\x1b[2J""\x1b[H"
    echo $ERROR_LIST | pbcopy
    echo "ITEMS THAT DID NOT EXIST COPIED TO PASTEBOARD: "
    for item in $ERROR_LIST; do
        echo "\t${item}"
    done
    exit
fi






###################################################################################################

# /Users/diegoibarra/Developer/1_myProjects/MiniProjects/NestControl/nest /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniProjects/OpenWorkDirectory/workdir /usr/local/bin


# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/RandomText/randomText /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/FontScriptName/fontScriptName /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/CreateIconSet/createIconSet /usr/local/bin

# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/TestDialog/testDialog /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/Preview256Colors/preview256colors /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/Touchd/touchd /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/Datetimed/datetimed /usr/local/bin


# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/EchoEachPath/echoPath /usr/local/bin
# /Users/diegoibarra/Developer/1_myProjects/MiniTasks/Figletd/figletd /usr/local/bin
