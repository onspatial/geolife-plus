#! /bin/bash
#SBATCH --mincpus=64
#SBATCH --mem=512000
#SBATCH --partition=c96-m768
directory=$1
if [ -z "$directory" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
echo "changing directory to $directory"
cd $directory
bash sh.test_env.sh
