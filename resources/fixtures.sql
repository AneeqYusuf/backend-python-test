INSERT INTO users (username, password) VALUES
('user1', 'pbkdf2:sha256:150000$zBaLVyfI$cdf48098cff4aca4e12ef10415c959c721f79f23be495f37889f761fe67af76b'),
('user2', 'pbkdf2:sha256:150000$l1xXgMRn$fddad49b0cd190c71b8c64f3158ebdd286682862872cdb886d1d54e3bf9204ef'),
('user3', 'pbkdf2:sha256:150000$oeiyjylL$f8fe9215a67694ea007bd6e2d592ed5aac2fdc95259700eeef2f9605d3c791cb');

INSERT INTO todos (user_id, description, status) VALUES
(1, 'Vivamus tempus', 'complete'),
(1, 'lorem ac odio', 'incomplete'),
(1, 'Ut congue odio', 'complete'),
(1, 'Sodales finibus', 'incomplete'),
(1, 'Accumsan nunc vitae', 'incomplete'),
(2, 'Lorem ipsum', 'incomplete'),
(2, 'In lacinia est', 'complete'),
(2, 'Odio varius gravida', 'complete');
