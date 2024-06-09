ssh_command="ssh -o ProxyJump=hamiri@lab0z.mathcs.emory.edu"
remote_machine="hamiri@hopperlogin.mathcs.emory.edu"
remote_path="/local/hamirivolume10TB/Research/geolife_star/t04"
local_path="/home/emo/Research"
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
    rsync -ruavx --progress -e "$ssh_command" $remote_machine:$remote_path/geopol-dev/params.pool.json $local_path/geopol-dev/params.pool.hopper.json
}
if [ "$where" == "remote" ]; then
    # local_to_remote $size
    echo "Disabled"
elif [ "$where" == "local" ]; then
    remote_to_local $size
elif [ "$where" == "param" ]; then
    scp_to_local
else
    echo "Usage: $0 [local|remote]"
    exit 1
fi
