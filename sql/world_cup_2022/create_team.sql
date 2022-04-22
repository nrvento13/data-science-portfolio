CREATE TABLE IF NOT EXISTS united_states (
	player_id  VARCHAR PRIMARY KEY,
	country_id CHAR,
	first_name CHAR,
	last_name CHAR,
	birth_date DATE,
	birth_country CHAR,
	height_cm INTEGER ,
	weight_kg INTEGER,
	club_team CHAR,
	club_league CHAR,
	position CHAR
	);
