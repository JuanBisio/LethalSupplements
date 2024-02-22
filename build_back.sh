source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt
reflex init 
reflex export --backend-only 
rm -rf backend 
unzip backend.zip -d backend 
rm -f backend.zip 
desactivate