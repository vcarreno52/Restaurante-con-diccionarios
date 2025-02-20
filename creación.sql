CREATE database menu;
use menu;

CREATE TABLE MenuItem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE menu_infantil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    figurita VARCHAR(255),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_adultos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    bebida VARCHAR(255),
    tamano VARCHAR(50),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_ancianos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    bebida VARCHAR(255),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_ansiosos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    ansiolítico INT,
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_alcólicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    alcohol VARCHAR(255),
    tipo VARCHAR(50),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_vegetariano (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    verduras VARCHAR(255),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);

CREATE TABLE menu_para_compartir (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    platillo VARCHAR(255),
    FOREIGN KEY (menu_id) REFERENCES MenuItem(id)
);
