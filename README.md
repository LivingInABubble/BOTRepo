## Introduction 
API that accepts img and returns extracted PDF417 JSON data from license

## Build and Test
###1.	Clone the repo
   >  git clone https://socialrealm@dev.azure.com/socialrealm/MyMedCard.app/_git/BOTRepo && cd BOTRepo

###2.	Install java, pip and virtual environment.
   >  sudo apt install default-jre python3-pip python3.8-venv

###3.	Create virtual environment
   >  python3 -m venv venv

###4.	Activate virtual environment and update pip
   > source venv/bin/activate && pip install -U pip setuptools

###5.	Install wheel library
   > pip install wheel

###6.	Install dependencies
   > pip install -r requirements.txt

###7.	Copy service file into system directory
   > sudo cp MMCBotAndApi.service /lib/systemd/system/

###8.	Reload Deamon
   > sudo systemctl daemon-reload

###9.	Enable and start service
   > sudo systemctl enable MMCBotAndApi.service && systemctl start MMCBotAndApi.service
   
###*	Check service status
   > sudo systemctl status MMCBotAndApi.service
   
###**	Stop or restart service
   > sudo systemctl stop MMCBotAndApi.service
> 
   > sudo systemctl restart MMCBotAndApi.service
