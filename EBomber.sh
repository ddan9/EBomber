#!/bin/bash

spacing=" ---------------------------------------------------- "
sleeptime=0.4 
version=$(cat ./EBomber/config/version)
name=$(cat ./EBomber/config/name)

clear

sleep $sleeptime

echo ""
echo "  _____  _____  _____  _    _  _____  _____  _____   "
echo " |  ___||  _  ||  _  || \  / ||  _  ||  ___||  _  |  "
echo " | |__  | |_| )| | | ||  \/  || |_| )| |__  | |_| )  "
echo " |  __| |  _ ( | | | || \  / ||  _ ( |  __| |  _ (   "
echo " | |___ | |_| )| |_| || |\/| || |_| )| |___ | | \ \  "
echo " |_____||_____||_____||_|  |_||_____||_____||_|  \_\ "
echo ""

sleep $sleeptime

echo "$spacing " 
echo ""

if [[ $name = "" ]]

	then 

		read -p " What is your name?: " name
		echo $name > ./EBomber/config/name
		echo ""

	else

		echo " Hello there, $name ! :)"
		echo ""

fi

echo "$spacing " 
echo ""

sleep $sleeptime

echo " Using version: $version "

if [[ $version != "Mobile" ]] && [[ $version != "Desktop" ]]

	then

		echo ""
		echo " Choose the version: "
		echo ""
		echo " 1 | Mobile " 
		echo ""
		echo " 2 | Desktop "
		echo ""
		read -p " What version do you use?: " choose

		case "$choose" in

			"1" )
			echo Mobile > ./EBomber/config/version; clear; bash ./EBomber.sh
			;;

			"2" )
			echo Desktop > ./EBomber/config/version; clear; bash ./EBomber.sh
			;;

		esac

	else

		echo ""
	
		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		echo " What do you prefer to use?"
		echo ""
		echo " 0 | Exit "
		echo ""
		echo " 1 | EBomber.py (common version) " 
		echo ""
		echo " 2 | MTS-EBomber.py (MTS Only Edition) "
		echo ""

		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		read -p " Choose the way: " choose

		sleep $sleeptime

		if [[ $version = "Mobile" ]]		

			then

				case "$choose" in

					"0" )
					clear exit
					;;

					"1" )
					python ./EBomber/EBomber.py
					;;

					"2" )
					python ./EBomber/MTS-EBomber.py
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
					python3 ./EBomber/EBomber.py
					;;

					"2" )
					python3 ./EBomber/MTS-EBomber.py
					;;

				esac

			else

				echo ""

		fi

		clear		

fi