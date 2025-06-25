# Batch ETL to PostgreSQL Data Warehouse

## 📄 Project Summary
The data analyst team requires a table to support dashboard development related to order details from the `marketplace` production database. As a data engineer, you are tasked with creating a data migration script to transfer data from the source tables to the data warehouse. This will allow the analyst team to use the data warehouse tables for their reporting needs without placing additional load on the `marketplace` production database.

The data analyst team has also provided the required columns for the table. The target schema needed by the team is as follows:

![Session 15 - Project 3](https://github.com/user-attachments/assets/95273333-2b15-44f8-ad49-a0176f179088)

---
<br>

![Blank diagram - Page 1](https://github.com/user-attachments/assets/6d18febb-7266-448d-a6c4-0daf4a9ec810)

This project implements a batch ETL (Extract, Transform, Load) pipeline to migrate transactional order data from a PostgreSQL production database into a PostgreSQL-based data warehouse. The output of this pipeline is a cleaned and structured table, `dim_orders`, that serves as a basis for business reporting and dashboarding.

---

## 🎯 Objectives

* Develop a functional ETL pipeline using Python.
* Integrate with PostgreSQL databases for source and target storage.
* Normalize and transform raw transactional order data into a clean dimensional table.
* Enable data analysts to run dashboard queries without impacting production systems.

---

## 🧱 Output Table: `dim_orders`

| Column Name     | Data Type    | Description                  |
| --------------- | ------------ | ---------------------------- |
| order\_id       | INT          | Unique order identifier      |
| order\_date     | DATE         | Date when the order was made |
| user\_id        | INT          | User who placed the order    |
| payment\_name   | VARCHAR(255) | Payment method used          |
| shipper\_name   | VARCHAR(255) | Delivery service             |
| order\_price    | INT          | Total price before discounts |
| order\_discount | INT          | Discount applied             |
| voucher\_name   | VARCHAR(255) | Voucher code used (if any)   |
| voucher\_price  | INT          | Voucher discount amount      |
| order\_total    | INT          | Final amount paid            |
| rating\_status  | VARCHAR(255) | Post-order user rating       |

![Screenshot 2024-04-09 202742](https://github.com/user-attachments/assets/aa6b8a2b-69fb-40e0-9785-0e3dcc4dece8)

---

## 🛠️ Technologies Used

* **Language**: Python 3.7+
* **Databases**: PostgreSQL (source and target)
* **Libraries**:

  * `psycopg2-binary` for database connectivity
  * `SQLAlchemy` for ORM and queries
  * `sqlparse` for query formatting
  * `pandas` for data transformation
* **Environment**:

  * Docker (optional, for setting up Postgres)
  * DBeaver / PgAdmin (for database visualization)
  * VSCode / PyCharm (IDE)
  * Git & GitHub (version control)

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

## 🔄 Execution Flow

1. Define PostgreSQL database credentials in `connection.py`.
2. Create schema and sample data in source DB.
3. Use `main.py` to extract data from source DB, apply transformations, and load to data warehouse.
4. Final table `dim_orders` is used for reporting purposes.

---

## ✅ Key Results

* Successfully migrated transactional data into structured DWH format.
* ETL process runs without errors.
* Data is clean, complete, and queryable for analytics use cases.

---

## 📌 References

* [Project Brief PDF](https://drive.google.com/file/d/1SCh9ibnV4kWEowqClRUIZeVCnHtJo2bS/view?usp=sharing)
