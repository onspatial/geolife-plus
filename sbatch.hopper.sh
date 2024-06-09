#! /bin/bash
#SBATCH --mincpus=32
#SBATCH --mem=128GB
directory=$1
if [ -z "$directory" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
echo "changing directory to $directory"
cd $directory
bash sh.run.sh
