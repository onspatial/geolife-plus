ssh_command="ssh -o ProxyJump=hamiri@lab0z.mathcs.emory.edu"
remote_machine="hamiri@hopperlogin.mathcs.emory.edu"
remote_path="/local/hamirivolume10TB/Research/geolife_star/r01"
local_path=$(dirname $(dirname $(realpath $0)))
where=$1
size=$2
if [ -z "$where" ]; then
    echo "Usage: $0 [local|remote]"
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
scp_to_local() {
    echo "scp to local scp should jump the proxy"
    rsync -ruavx --progress -e "$ssh_command" $remote_machine:$remote_path/params.pool.json $local_path/geopol-dev/params.pool.hopper.json
    rsync -ruavx --progress -e "$ssh_command" $remote_machine:$remote_path/results_score.log.txt $local_path/geopol-dev/results_score.hopper.log.txt
    rsync -ruavx --progress -e "$ssh_command" $remote_machine:$remote_path/pole/* $local_path/geopol-dev/pole_hopper
}

ssh_geostar() {
    echo "running ssh_geostar"
    # ssh $remote_machine "mkdir -p $remote_path"
    echo remote path created
    # echo "scp -r $local_path/geopol-dev/geostar.zip $remote_machine:$remote_path/geostar.zip"
    rsync -ruavx --progress -e "$ssh_command" $local_path/geopol-dev/geostar.zip $remote_machine:$remote_path/geostar.zip
    echo "sync to remote finished ..."
    # unzip the file
    echo "ssh $remote_machine "unzip -o $remote_path/geostar.zip -d $remote_path""
}
if [ "$where" == "remote" ]; then
    # local_to_remote $size
    echo "Disabled"
elif [ "$where" == "local" ]; then
    # remote_to_local $size
    echo "Disabled"
elif [ "$where" == "param" ]; then
    scp_to_local
elif [ "$where" == "c01" ]; then
    # ssh_geostar
    echo "Disabled"
else
    echo "Usage: $0 [local|remote]"
    exit 1
fi
