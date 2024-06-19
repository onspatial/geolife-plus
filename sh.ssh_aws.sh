ssh_command="ssh hamiri@cirrostratus.it.emory.edu"
remote_machine="hamiri@cirrostratus.it.emory.edu"
remote_path="/scratch/hamiri/Research/geolife_star/res01"
local_path=$(dirname $(dirname $(realpath $0)))
echo "local_path: $local_path"
where=$1
size=$2
if [ -z "$where" ]; then
    echo "Usage: $0 [local|remote|param] [size]"
    exit 1
fi
if [ -z "$size" ]; then
    size=100000
fi

remote_to_local() {
    size=$1
    echo "syncing remote to local "
    rsync -ruavx --max-size=$size\m --progress -e "$ssh_command" $remote_machine:$remote_path/geopol-dev $local_path
}

local_to_remote() {
    size=$1
    echo "syncing local to remote "
    rsync -ruavx --max-size=$size\m --progress -e "$ssh_command" $local_path/geopol-dev $remote_machine:$remote_path
}
scp_to_remote() {
    echo "scp to remote "
    # scp -r $local_path/geopol-dev $remote_machine:$remote_path
    # first make sure directory exists
    ssh $remote_machine "mkdir -p $remote_path"
    scp -r $local_path/geopol-dev/geostar.zip $remote_machine:$remote_path/geostar.zip
    # unzip the file
    ssh $remote_machine "unzip -o $remote_path/geostar.zip -d $remote_path"
}
zip_geostar() {
    echo "zip all"
    cd $local_path/geopol-dev
    rm -f geostar.zip
    # ignore hiden files
    zip -r geostar.zip * -x ".*"
}
run_remote() {
    echo "running remote"
    ssh $remote_machine "ls $remote_path && cd $remote_path && bash sh.sh aws64"
}
scp_to_local() {
    echo "scp to local "
    id=data_generation
    scp -r $remote_machine:$remote_path/params.pool.json $local_path/geopol-dev/params.pool.$id.json
    scp -r $remote_machine:$remote_path/results_score.log.txt $local_path/geopol-dev/results_score.$id.log.txt
    scp -r $remote_machine:$remote_path/pole/* $local_path/geopol-dev/pole_$id

}
if [ "$where" == "remote" ]; then
    echo "Disabled"
    # local_to_remote $size
    # echo "Disabled"
elif [ "$where" == "local" ]; then
    scp_to_local
    # remote_to_local $size
elif [ "$where" == "c00" ]; then
    scp_to_local
elif [ "$where" == "c01" ]; then
    echo "Disabled"
    # scp_to_remote
elif [ "$where" == "c02" ]; then
    echo "Disabled"
    # run_remote
elif [ "$where" == "c03" ]; then
    echo "Disabled"
    # zip_geostar
    # scp_to_remote
    # run_remote
else
    echo "Usage: $0 [local|remote]"
    exit 1
fi
