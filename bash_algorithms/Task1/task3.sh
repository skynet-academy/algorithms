read a
read b
read c

if [ $(expr $a + $b) -gt $c ] && [ $(expr $b + $c) -gt $a ] && [ $(expr $a + $c) -gt $b ];then
    if [ $a -eq $b ] && [ $b -eq $c ];then
        echo "EQUILATERAL"
    elif [ [ $a -eq $b ] && [ $c -ne $b ] ] || [ [ $a -eq $c ] && [ $c -ne $b ] ] ||  [ [ $b -eq $c ] && [ $a -ne $b ] ];then
       echo "ISOSCELES"
    elif [ $a -ne $b && $a -ne $c && $b -ne $c ];then
        "SCALENE"
fi
