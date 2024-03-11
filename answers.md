1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.
answer = In the database, there are two main tables: "Product" and "Product_Category." These tables are related through a column in the "Product" table called "category_id." This column stores an integer value that acts as a reference to the "id" column in the "Product_Category" table.
This relationship implies that each product belongs to a single product category, but each product category can have multiple products associated with it. So, it's a one-to-many relationship, with "Product_Category" being the side with one category and "Product" being the side with many products.

2.How could you ensure that each product in the "Product" table has a valid category assigned to it?
answer= Database Constraint:
Use a foreign key constraint on the "category_id" column in the "Product" table, referencing the "id" column in the "Product_Category" table. This ensures that every value in the "category_id" column of the "Product" table corresponds to a valid category ID in the "Product_Category" table.

Application-Level Validation:
Before inserting or updating a product record, validate the "category_id" to ensure it exists in the "Product_Category" table. If the category ID is invalid, prevent the operation from proceeding.

Trigger Implementation:
Implement a trigger on the "Product" table to verify the validity of the "category_id" before any insert or update operation. If the category ID is not valid, the trigger can halt the operation, ensuring only valid category IDs are stored in the "Product" table.
