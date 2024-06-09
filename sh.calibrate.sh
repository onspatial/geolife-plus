echo "running test_python.py"
python3 code/test_python.py
echo "running test_env.py"
python3 code/test_env.py
echo "running calibrate.py at: $(date)"
python3 code/calibrate.py
echo "running test_python.py"
python3 code/test_python.py
