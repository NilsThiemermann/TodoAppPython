CREATE TABLE IF NOT EXISTS tbl_Todo(
    id INTEGER not null PRIMARY KEY AUTOINCREMENT,
    todo varchar(255) not null,
    expenditure_of_time INTEGER,
    fk_importance INTEGER,
    create_date DATETIME
    CONSTRAINT df_create_date DEFAULT CURRENT_TIMESTAMP,
    expiry_date DATETIME,

    CONSTRAINT Fk_tbl_Todo_tbl_Importance
	Foreign Key (fk_importance) 
	REFERENCES tbl_Importance (id)
);

CREATE TABLE IF NOT EXISTS tbl_Importance(
    id INTEGER not null PRIMARY KEY AUTOINCREMENT,
    [name] varchar(50)
);

CREATE VIEW IF NOT EXISTS view_Todo
AS
SELECT t.todo, t.expenditure_of_time, i.[name], t.create_date, t.expiry_date FROM tbl_Todo as t LEFT JOIN tbl_Importance as i ON t.fk_importance = i.id ORDER BY expiry_date DESC;

INSERT INTO tbl_Todo(todo, expenditure_of_time, fk_importance, expiry_date)
VALUES("This App", 240, 2, CURRENT_TIMESTAMP);

INSERT INTO tbl_Importance([name])
VALUES("Not important");

INSERT INTO tbl_Importance([name])
VALUES("Important");

INSERT INTO tbl_Importance([name])
VALUES("Very important");