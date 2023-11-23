# Welcome

This repository hosts a simple data engineering project.

In the realm of a bustling grocery store, data accumulates rapidly based on the store's scale and operations.

Analyzing this data becomes crucial as it holds the key to informed decision-making.

This project focuses on sales data analysis, utilizing a simplified dataset to derive insights.

Our primary objectives revolve around enhancing customer satisfaction and optimizing the work environment for the staff.

## Approach(Initial thoughts)

- Implementing a 5% incentive scheme for top-performing salespersons each month.
- Issuing special coupons to customers with high monthly purchases.
- And potentially exploring further strategies to enhance overall experience.


#### Project structure:
        sales_analysis/
        │   .env
        │   README.md   
        │               
        ├───resources
        │   │   config.ini.template
        │   │   constants.py
        │   │   __init__.py
        │   │   
        │   |───data
        │       │   
        │       ├───customer_data_mart
        │       │       .gitkeep
        │       │       
        │       ├───error_files
        │       │       .gitkeep
        │       │       
        │       ├───s3_files
        │       │       .gitkeep
        │       │       
        │       ├───sales_team_data_mart
        │       │       .gitkeep
        │       │       
        │       └───sales_team_data_mart_partitioned
        │               .gitkeep           
        │           
        └───sales_analysis
            │   __init__.py
            │   
            ├───common_utils
                    local_operations.py
                    logger.py
                    __init__.py

#### Tech stack
    -> we'll be using Spark,S3,mysql.