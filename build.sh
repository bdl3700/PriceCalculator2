./cleanup.sh

python -m nuitka --windows-disable-console --follow-imports --enable-plugin=tk-inter --onefile --output-filename="calculator.exe" app.py

./cleanup.sh