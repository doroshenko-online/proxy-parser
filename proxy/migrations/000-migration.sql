DROP TABLE IF EXISTS proxies;
DROP TABLE IF EXISTS protocols;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS users;

CREATE TABLE protocols (
  id SERIAL NOT NULL PRIMARY KEY,
  protocol_name char(10) NOT NULL
);

CREATE TABLE resources (
  id SERIAL PRIMARY KEY,
  name varchar(50) NOT NULL,
  addr varchar(100) NOT NULL,
  available BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE proxies (
  ip varchar(16) NOT NULL,
  port int NOT NULL,
  protocol_id int REFERENCES protocols (id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  login varchar(100) DEFAULT NULL,
  pass varchar(32) DEFAULT NULL,
  from_resource_id int REFERENCES resources (id),
  work BOOLEAN NOT NULL,
  google_work BOOLEAN NOT NULL,
  country_iso char(3) DEFAULT NULL,
  last_response_time float DEFAULT 9999,
  PRIMARY KEY (ip, port)
);

CREATE TABLE user_roles (
  id SERIAL PRIMARY KEY,
  role_name varchar(10) NOT NULL UNIQUE,
  priority int NOT NULL
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username varchar(32) NOT NULL UNIQUE,
  password varchar(32) NOT NULL UNIQUE,
  role int REFERENCES user_roles(id),
  ip varchar(16) DEFAULT NULL,
  country_iso char(3) DEFAULT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO user_roles (role_name, priority)
VALUES
  ('superadmin', 0),
  ('admin', 1),
  ('api_user', 2),
  ('web_user', 3);

INSERT INTO protocols (protocol_name)
VALUES
  ('http'),
  ('https'),
  ('socks');