#!/bin/bash
daemonconfigfile=/etc/argononed.conf
echo "--------------------------------------"
echo "Argon One Fan Speed Configuration Tool"
echo "--------------------------------------"
echo "WARNING: This will remove existing configuration."
echo -n "Press Y to continue:"
read -n 1 confirm
echo
if [ "$confirm" = "y" ]
then
	confirm="Y"
fi

if [ "$confirm" != "Y" ]
then
	echo "Cancelled"
	exit
fi
echo "Thank you."
get_number () {
	read curnumber
	re="^[0-9]+$"
	if [ -z "$curnumber" ]
	then
		echo "-2"
		return
	elif [[ $curnumber =~ ^[+-]?[0-9]+$ ]]
	then
		if [ $curnumber -lt 0 ]
		then
			echo "-1"
			return
		elif [ $curnumber -gt 100 ]
		then
			echo "-1"
			return
		fi	
		echo $curnumber
		return
	fi
	echo "-1"
	return
}

loopflag=1
while [ $loopflag -eq 1 ]
do
	echo
	echo "Select fan mode:"
	echo "  1. Always on"
	echo "  2. Adjust to temperatures (55C, 60C, and 65C)"
	echo "  3. Customize behavior"
	echo "  4. Cancel"
	echo "NOTE: You can also edit $daemonconfigfile directly"
	echo -n "Enter Number (1-4):"
	newmode=$( get_number )
	if [[ $newmode -ge 1 && $newmode -le 4 ]]
	then
		loopflag=0
	fi
done
echo
if [ $newmode -eq 4 ]
then
	echo "Cancelled"
	exit
elif [ $newmode -eq 1 ]
then
	echo "#" > $daemonconfigfile
	echo "# Argon One Fan Speed Configuration" >> $daemonconfigfile
	echo "#" >> $daemonconfigfile
	echo "# Min Temp=Fan Speed" >> $daemonconfigfile
	echo 1"="100 >> $daemonconfigfile
	sudo systemctl restart argononed.service
	echo "Fan always on."
	exit
elif [ $newmode -eq 2 ]
then
	echo "Please provide fan speeds for the following temperatures:"
	echo "#" > $daemonconfigfile
	echo "# Argon One Fan Speed Configuration" >> $daemonconfigfile
	echo "#" >> $daemonconfigfile
	echo "# Min Temp=Fan Speed" >> $daemonconfigfile
	curtemp=55
	while [ $curtemp -lt 70 ]
	do
		errorfanflag=1
		while [ $errorfanflag -eq 1 ]
		do
			echo -n ""$curtemp"C (0-100 only):"
			curfan=$( get_number )
			if [ $curfan -ge 0 ]
			then
				errorfanflag=0
			fi
		done
		echo $curtemp"="$curfan >> $daemonconfigfile
		curtemp=$((curtemp+5))
	done
	sudo systemctl restart argononed.service
	echo "Configuration updated."
	exit
fi
echo "Please provide fan speeds and temperature pairs"
echo
loopflag=1
paircounter=0
while [ $loopflag -eq 1 ]
do
	errortempflag=1
	errorfanflag=1
	while [ $errortempflag -eq 1 ]
	do
		echo -n "Provide minimum temperature (in Celsius) then [ENTER]:"
		curtemp=$( get_number )
		if [ $curtemp -ge 0 ]
		then
			errortempflag=0
		elif [ $curtemp -eq -2 ]
		then
			errortempflag=0
			errorfanflag=0
			loopflag=0
		fi
	done
	while [ $errorfanflag -eq 1 ]
	do
		echo -n "Provide fan speed for "$curtemp"C (0-100) then [ENTER]:"
		curfan=$( get_number )
		if [ $curfan -ge 0 ]
		then
			errorfanflag=0
		elif [ $curfan -eq -2 ]
		then
			errortempflag=0
			errorfanflag=0
			loopflag=0
		fi
	done
	if [ $loopflag -eq 1 ]
	then
		if [ $paircounter -eq 0 ]
		then
			echo "#" > $daemonconfigfile
			echo "# Argon One Fan Speed Configuration" >> $daemonconfigfile
			echo "#" >> $daemonconfigfile
			echo "# Min Temp=Fan Speed" >> $daemonconfigfile
		fi
		echo $curtemp"="$curfan >> $daemonconfigfile
		
		paircounter=$((paircounter+1))
		
		echo "* Fan speed will be set to "$curfan" once temperature reaches "$curtemp" C"
		echo
	fi
done

echo
if [ $paircounter -gt 0 ]
then
	echo "Thank you!  We saved "$paircounter" pairs."
	sudo systemctl restart argononed.service
	echo "Changes should take effect now."
else
	echo "Cancelled, no data saved."
fi
