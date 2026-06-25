WITH good_days AS(
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    from Stadium
    WHERE people >= 100
)
 SELECT g1.id, g1.visit_date, g1.people FROM good_days g1 where g1.grp in (
    select grp
    from good_days
    group by grp
    having count(*) >= 3
 )
ORDER BY g1.visit_date;








