MoMo SMS app

Team Name
Dev Note

Team Members
- Rene Guido Kayigamba
- Elijah Kabatsi
- NYIRIHIRWE Yves

Project Description

This project handles XML-formatted Mobile Money (MoMo) SMS transaction data.

The system:
- Parses XML transaction messages
- Cleans and normalizes data
- Categorizes transactions
- Stores data in SQLite
- Generates analytics data
- Displays insights on a frontend dashboard

 Technologies
- Python
- SQLite
- HTML/CSS/JavaScript
- FastAPI


Architecture Diagram:
https://miro.com/app/board/uXjVHV5oNv4=/?share_link_id=722346128313
 
Scrum Board:
https://trello.com/b/UpaAck4A/momo-progress


Setup Instructions

git clonehttps://github.com/kguido798/Momo
cd Momo

Install Dependencies

pip install -r requirements.txt

Run ETL

python etl/run.py

