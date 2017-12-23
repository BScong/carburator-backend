# Script to schedule regularly using cron
rm PrixCarburants_instantane.xml
wget https://donnees.roulez-eco.fr/opendata/instantane
unzip instantane
rm instantane
python3 populate.py