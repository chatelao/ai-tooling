SELECT u.username, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.username
HAVING post_count > 0
ORDER BY post_count DESC;
