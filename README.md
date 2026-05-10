MoMo SMS app

Team Name
Dev Note

Team Members
- Rene Guido Kayigamba
- Elijah Kabatsi
- NYIRIHIRWE Yves

Project Description

This project handles XML-formatted Mobile Money (MoMo) SMS transaction data. The project will go ahead and store the date in SQLite database, and intends to be attractive so that the user feels a sense of belonging and quite easy to use.

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

<img width="1600" height="273" alt="image" src="https://github.com/user-attachments/assets/a2e02614-10c2-446c-b1e2-fb91cdfb8867" />


Scrum Board:
https://trello.com/b/UpaAck4A/momo-progress


Setup Instructions

git clonehttps://github.com/kguido798/Momo
cd Momo

Install Dependencies

pip install -r requirements.txt

Run ETL

python etl/run.py

