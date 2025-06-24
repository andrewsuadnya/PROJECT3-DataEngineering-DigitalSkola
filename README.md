# ETL Order Data to PostgreSQL Data Warehouse

## 📌 Project Overview

This project is part of the DigitalSkola SIB Batch 6 program, focusing on batch processing and foundational data engineering tasks. The goal is to implement a simple ETL pipeline using Python to migrate order data from a production PostgreSQL database into a data warehouse (DWH) for analytical use.

The final data warehouse table (`dim_orders`) will be used by data analysts to create dashboards without impacting the production system.

---

## 🧠 Learning Objectives

* Understand and apply the ETL (Extract, Transform, Load) process.
* Strengthen skills in:

  * Python programming
  * SQL and schema design
  * PostgreSQL
  * Git & GitHub
  * Docker (optional for DB setup)

---

## 🛠️ Tech Stack & Tools

* **Language**: Python 3.7+
* **Database**: PostgreSQL
* **Libraries**:

  * `psycopg2-binary==2.9.3`
  * `SQLAlchemy==1.4.40`
  * `sqlparse==0.4.2`
  * `pandas==1.4.3`
* **SQL GUI**: DBeaver / PgAdmin
* **IDE**: VSCode / PyCharm
* **Version Control**: Git + GitHub

---

## 🗃️ Schema Overview

The `dim_orders` table in the data warehouse includes:

| Column Name     | Data Type    |
| --------------- | ------------ |
| order\_id       | INT          |
| order\_date     | DATE         |
| user\_id        | INT          |
| payment\_name   | VARCHAR(255) |
| shipper\_name   | VARCHAR(255) |
| order\_price    | INT          |
| order\_discount | INT          |
| voucher\_name   | VARCHAR(255) |
| voucher\_price  | INT          |
| order\_total    | INT          |
| rating\_status  | VARCHAR(255) |

---

## 📁 Project Structure

```
├── query/
│   ├── dwh_design.sql         # DWH schema creation script
│   └── query.sql              # Custom SQL queries (ETL logic)
├── connection.py              # DB connection config (source and DWH)
├── main.py                    # ETL process orchestrator
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
```

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. Set up PostgreSQL databases (source & warehouse) manually or using Docker.

3. Update DB credentials in `connection.py`.

4. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the ETL process:

   ```bash
   python main.py
   ```

---

## 📝 Notes

* Sample data and schema are available in the shared Google Drive folder (see project brief).
* Make sure both source and DWH databases are accessible.

---

## 📌 Reference

* [Project Brief (PDF)](https://drive.google.com/file/d/1SCh9ibnV4kWEowqClRUIZeVCnHtJo2bS/view?usp=sharing)
