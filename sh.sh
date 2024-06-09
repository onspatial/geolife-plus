target=$1
if [ -z $target ]; then
    echo "Usage: $0 <target>"
    exit 1
fi
working_directory=$(pwd)
# if target is not local  install packages
if [ $target != "local" ]; then
    echo "installing packages ..."
    bash sh.pip.sh
fi

if [ $target == "aws64" ]; then
    echo "running sbatch.aws64.sh"
    sbatch sbatch.aws64.sh $working_directory
elif [ $target == "aws96" ]; then
    echo "running sbatch.aws96.sh"
    sbatch sbatch.aws96.sh $working_directory
elif [ $target == "hopper" ]; then
    echo "running sbatch.hopper.sh"
    sbatch sbatch.hopper.sh $working_directory
elif [ $target == "test" ]; then
    echo "running sbatch.test.sbatch"
    sbatch sbatch.test.sbatch $working_directory
elif [ $target == "local" ]; then
    echo "running sh.run.sh"
    bash sh.run.sh
else
    echo "Unknown target: $target"
    exit 1
fi
