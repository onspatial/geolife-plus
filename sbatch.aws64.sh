#! /bin/bash
#SBATCH --mincpus=60
#SBATCH --mem=412000
#SBATCH --partition=c64-m512
directory=$1
if [ -z "$directory" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
echo "changing directory to $directory"
cd $directory
bash sh.run.sh
