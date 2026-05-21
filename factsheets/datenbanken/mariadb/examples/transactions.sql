-- Beispiel für eine Transaktion in MariaDB
START TRANSACTION;

INSERT INTO users (id, username, email) VALUES (10, 'alice', 'alice@example.com');
INSERT INTO users (id, username, email) VALUES (11, 'bob', 'bob@example.com');

-- Simuliere eine Bedingung für COMMIT oder ROLLBACK
-- COMMIT;
ROLLBACK; -- In diesem Beispiel machen wir alles rückgängig
