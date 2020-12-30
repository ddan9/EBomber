#!/bin/bash

spacing=" ---------------------------------------------------- "
sleeptime=0.4 
version=$(cat $HOME/EBomber/config/version)
name=$(cat $HOME/EBomber/config/name)
logo=$HOME/EBomber/config/logo.sh
number=$(cat $HOME/EBomber/config/number)

clear

sleep $sleeptime

bash $logo

sleep $sleeptime

echo "$spacing " 
echo ""

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
			echo Mobile > $HOME/EBomber/config/version; clear; bash $HOME/EBomber.sh
			;;

			"1" )
			echo Desktop > $HOME/EBomber/config/version; clear; bash $HOME/EBomber.sh
			;;

		esac

	else

		echo " Используемая версия: $number $version "
		echo ""
		echo " Используемый язык: Русский"
		echo ""
	
		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		echo " Что хотите использовать?"
		echo ""
		echo " 0 | Выход "
		echo ""
		echo " 1 | Обычный бомбер " 
		echo ""
		echo " 2 | МТС Версия (атака только из-под МТС) "
		echo ""

		sleep $sleeptime

		echo "$spacing " 
		echo ""

		sleep $sleeptime

		read -p " Выберите вариант > " choose

		sleep $sleeptime

		if [[ $version = "Mobile" ]]		

			then

				case "$choose" in

					"0" )
					clear exit
					;;

					"1" )
					python $HOME/EBomber/lang/ru/EBomber.py
					;;

					"2" )
					python $HOME/EBomber/lang/ru/MTS-EBomber.py
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
					python3 $HOME/EBomber/lang/ru/EBomber.py
					;;

					"2" )
					python3 $HOME/EBomber/lang/ru/MTS-EBomber.py
					;;

				esac

			else

				echo ""

		fi

		clear		

fi
