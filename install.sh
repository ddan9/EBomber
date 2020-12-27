#!/bin/bash

spacing=" ---------------------------------------------------- "
lang=$(cat $HOME/EBomber/config/lang)
sleeptime=0.4
logo=$HOME/EBomber/config/logo.sh
version=$(cat $HOME/EBomber/config/version)
name=$(cat $HOME/EBomber/config/name)

clear

sleep $sleeptime

bash $logo

sleep $sleeptime

echo "$spacing"
echo ""

sleep $sleeptime

if [[ $lang = "" ]]

	then

		echo " Select language: "
		echo ""
		echo " 0 | English "
		echo ""
		echo " 1 | Russian "
		echo ""

		sleep $sleeptime

		echo "$spacing "
		echo ""

		sleep $sleeptime

 		read -p " What language do you speak? > " choose

		case "$choose" in

			"0" )
			echo en > $HOME/EBomber/config/lang; clear; bash $HOME/EBomber/install.sh
			;;

			"1" )
			echo ru > $HOME/EBomber/config/lang; clear; bash $HOME/EBomber/install.sh
			;;

		esac


	else

		while [[ $lang = "en" ]]

			do

				echo " Using language: English "
				echo ""

				sleep $sleeptime

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
						echo " 0 | Mobile " 
						echo ""
						echo " 1 | Desktop "
						echo ""
						read -p " What version do you use? > " choose

						case "$choose" in

							"0" )
							echo Mobile > $HOME/EBomber/config/version; clear; bash $HOME/EBomber/install.sh
							;;

							"1" )
							echo Desktop > $HOME/EBomber/config/version; clear; bash $HOME/EBomber/install.sh
							;;

						esac

					else

						echo ""

				fi

				sleep $sleeptime

				if [[ $version = "Mobile" ]]		

					then

						echo " Preparing to install Mobile version..."
						echo ""
						echo " If given a choice during installation, select and enter: y"
						echo ""

						sleep 5

						clear

						apt-get update

						apt-get upgrade -y

						apt-get install -y python

						pip install -r $HOME/EBomber/config/requirements

						ln -s $HOME/EBomber/start.sh $HOME/EBomber.sh

					else

						echo ""

				fi

				if [[ $version = "Desktop" ]]		

					then

						echo " Preparing to install Desktop version..."
						echo ""
						echo " If given a choice during installation, select and enter: y"
						echo ""

						sleep 5

						clear

						sudo apt-get update

						sudo apt-get upgrade -y

						sudo apt-get install -y python3

						pip3 install -r $HOME/EBomber/config/requirements

						ln -s $HOME/EBomber/start.sh $HOME/EBomber.sh

					else

						echo ""

				fi

				sleep $sleeptime

				clear

				exit

			done

		while [[ $lang = "ru" ]]

			do

				echo " Используемый язык: Русский "
				echo ""

				sleep $sleeptime

				if [[ $name = "" ]]

					then 

						read -p " Как вас зовут? > " name
						echo $name > $HOME/EBomber/config/name
						echo ""

					else

						echo " Добро пожаловать, $name :)"
						echo ""

				fi

				sleep $sleeptime

				if [[ $version != "Mobile" ]] && [[ $version != "Desktop" ]]

					then

						echo " Выберите тип устройства: "
						echo ""
						echo " 0 | Телефон " 
						echo ""
						echo " 1 | Компьютер "
						echo ""
						read -p " Какой тип устройства вы используете? > " choose

						case "$choose" in

							"0" )
							echo Mobile > $HOME/EBomber/config/version; clear; bash $HOME/EBomber/install.sh
							;;

							"1" )
							echo Desktop > $HOME/EBomber/config/version; clear; bash $HOME/EBomber/install.sh
							;;

						esac

					else

						echo ""

				fi

				sleep $sleeptime

				if [[ $version = "Mobile" ]]		

					then

						echo " Подготовка к установке мобильной версии..."
						echo ""
						echo " Если во время установки вам будут давать выбор, выбирайте и вводите: y"
						echo ""

						sleep 5

						clear

						apt-get update

						apt-get upgrade -y

						apt-get install -y python

						pip install -r $HOME/EBomber/config/requirements

						ln -s $HOME/EBomber/start.sh $HOME/EBomber.sh

					else

						echo ""

				fi

				if [[ $version = "Desktop" ]]		

					then

						echo " Подготовка к установке компьютерной версии..."
						echo ""
						echo " Если во время установки вам будут давать выбор, выбирайте и вводите: y"
						echo ""

						sleep 5

						clear

						sudo apt-get update

						sudo apt-get upgrade -y

						sudo apt-get install -y python3

						pip3 install -r $HOME/EBomber/config/requirements

						ln -s $HOME/EBomber/start.sh $HOME/EBomber.sh

					else

						echo ""

				fi

				sleep $sleeptime

				clear

				exit

			done

fi