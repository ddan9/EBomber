#!/bin/bash

spacing=" ---------------------------------------------------- "
sleeptime=0.4 
version=$(cat $HOME/EBomber/config/version)
name=$(cat $HOME/EBomber/config/name)
logo=$HOME/EBomber/config/logo.sh

clear

sleep $sleeptime

bash $logo

sleep $sleeptime

echo "$spacing " 
echo ""

if [[ $name = "" ]]

	then 

		read -p " What is your name? > " name
		echo $name > $HOME/EBomber/config/name
		echo ""

	else

		echo " Hello there, $name :)"
		echo ""

fi

sleep $sleeptime

if [[ $version != "Mobile" ]] && [[ $version != "Desktop" ]]

	then

		echo " Choose the version: "
		echo ""
		echo " 1 | Mobile " 
		echo ""
		echo " 2 | Desktop "
		echo ""
		read -p " What version do you use? > " choose

		case "$choose" in

			"1" )
			echo Mobile > $HOME/EBomber/config/version; clear; bash $HOME/EBomber.sh
			;;

			"2" )
			echo Desktop > $HOME/EBomber/config/version; clear; bash $HOME/EBomber.sh
			;;

		esac

	else

		echo " Using version: $version "
		echo ""
		echo " Using language: English"
		echo ""
	
		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		echo " What do you prefer to use?"
		echo ""
		echo " 0 | Exit "
		echo ""
		echo " 1 | Common version " 
		echo ""
		echo " 2 | MTS Only Version (MTS attack) "
		echo ""

		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		read -p " Choose the way > " choose

		sleep $sleeptime

		if [[ $version = "Mobile" ]]		

			then

				case "$choose" in

					"0" )
					clear exit
					;;

					"1" )
					python $HOME/EBomber/lang/en/EBomber.py
					;;

					"2" )
					python $HOME/EBomber/lang/en/MTS-EBomber.py
					;;

				esac

			else

				echo ""

		fi

		if [[ $version = "Desktop" ]]		

			then

				case "$choose" in

					"0" )
					clear exit
					;;

					"1" )
					python3 $HOME/EBomber/lang/en/EBomber.py
					;;

					"2" )
					python3 $HOME/EBomber/lang/en/MTS-EBomber.py
					;;

				esac

			else

				echo ""

		fi

		clear		

fi