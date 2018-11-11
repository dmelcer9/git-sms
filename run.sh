#/bin/bash

cp postreceive.py "${GIT_REPO_PATH}/hooks/post-receive"
chmod +x "${GIT_REPO_PATH}/hooks/post-receive"
python3 textlistener.py 
