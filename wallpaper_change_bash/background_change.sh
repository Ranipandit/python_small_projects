echo "Hello USER"

declare -a images=("image1.jpg" "image2.jpg" "image3.jpg" "mom.jpg" "image4.jpg" "image5.jpg" "image6.jpg" "image7.jpg" "image8.jpg")

# this is for length 
array_length=${#images[@]}

######
echo ""
echo "***************You have 9(nine) Wallpapers stored*******************"
echo ""

#this is for random numbers to generate
random=$(($RANDOM % $array_length))

echo "---------Hey your lucky number of background image is $random ----------"
echo ""

#get each element from the list
random_image="${images[random]}"

#Always will come the background image randomly whenever we will open a new terminal
gsettings set org.gnome.desktop.background picture-uri file:///home/priya/Downloads/$random_image


