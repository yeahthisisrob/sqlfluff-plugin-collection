-- test_case_statements.sql

-- This CASE violates the rule: THEN is on the same line as WHEN.
SELECT
    CASE WHEN column_a = 'X' THEN 'Value is X'
         WHEN column_a = 'Y' THEN 'Value is Y'
         ELSE 'Unknown'
    END AS result_a
FROM your_table;

-- This CASE follows the rule: THEN is on a new line.
SELECT
    CASE
        WHEN column_b = 1
            THEN 'One'
        WHEN column_b = 2
            THEN 'Two'
        ELSE 'Other'
    END AS result_b
FROM your_table;
