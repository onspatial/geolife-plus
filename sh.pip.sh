# pip3 install -r requirements.txt
while read -r line; do
    {
        pip3 install $line
    } || {
        echo "Error: $line"
    }
done <requirements.txt
