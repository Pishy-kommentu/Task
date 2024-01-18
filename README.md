## Task 2

```sql
UPDATE full_names
SET status = s.status
FROM short_names s
WHERE split_part(full_names.name, '.', 1) = s.name;
```

```sql
UPDATE full_names fn
SET status = sn.status
FROM short_names sn
WHERE fn.name LIKE sn.name || '.%';
```