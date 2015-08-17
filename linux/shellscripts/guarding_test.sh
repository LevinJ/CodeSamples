#!/bin/sh
#

echo -e  "\n\t \t\tLet's start the cerberus testing"


generaterandom(){
     OUTPUT="$(awk -vmin=1 -vmax=7 'BEGIN{srand();  print int(min+rand()*(max-min+1))}')"
      return $OUTPUT
}

doOneTest(){
generaterandom
NUM=$?
echo "Option: $NUM"

case $NUM in
	1) service pacman stop ;;
	2) service sda stop ;;
	3) service coordinator stop ;;
	4) service pacman stop; service sda stop; ;;
	5) service pacman stop; service coordinator stop; ;;
	6) service pacman stop; service coordinator stop; service sda stop; ;;
	7) service sda  stop; service coordinator stop; ;;
	*) echo "INVALID NUMBER!" ;;
esac

}

#doOneTest


#nunmber of loops to perform
max=2000
for i in `seq 1 $max`
do
    echo "this is the loop $i ouf of total $max"
     doOneTest
        sleep  300
done


exit 0

