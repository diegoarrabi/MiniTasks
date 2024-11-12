#!/bin/zsh

LPM_ON=" lowpowermode         1"
LPM_OFF=" lowpowermode         0"

lpm_current_status="$(pmset -g | grep lowpowermode)"

if [ "$lpm_current_status" = "$LPM_ON" ] 
then
    sudo -S pmset -a lowpowermode 0
    battery_toggle="false"
    echo "LPM Turned Off"

elif [ "$lpm_current_status" = "$LPM_OFF" ]
then 
    sudo -S pmset -a lowpowermode 1
    battery_toggle="true"
    echo "LPM Turned ON"
fi

current_user=`who | grep console | awk '{ print $1 }'`

sudo -u $current_user defaults write /Users/$current_user/Library/Preferences/ByHost/com.apple.controlcenter.plist BatteryShowPercentage -bool $battery_toggle



