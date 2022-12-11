YEAR=2022
if [[ $# = 0 ]] ; then DAY=`date | tr -s " " | cut -d " " -f 3`; else DAY="${1}"; fi
mkdir -p $YEAR/day_$DAY
cp -i sol.py $YEAR/day_$DAY
cp get_input.sh $YEAR/day_$DAY
touch $YEAR/day_$DAY/input.test
cd $YEAR/day_$DAY