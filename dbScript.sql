CREATE TABLE IF NOT EXISTS tbl_Todo(
    id int not null
    CONSTRAINT pk_tbl_Todo PRIMARY KEY
    CONSTRAINT df_todo_id DEFAULT AUTO_INCREMENT,
    todo varchar(255) not null,
    expenditure_of_time int,
    fk_importance int,
    create_date DATETIME
    CONSTRAINT df_create_date DEFAULT CURRENT_TIMESTAMP,
    expiry_date DATETIME,

    CONSTRAINT Fk_tbl_Todo_tbl_Importance
	Foreign Key (fk_importance) 
	REFERENCES tbl_Importance (id)
);

CREATE TABLE IF NOT EXISTS tbl_Importance(
    id int not null
    CONSTRAINT pk_tbl_Todo PRIMARY KEY
    CONSTRAINT df_todo_id DEFAULT AUTO_INCREMENT,
    [name] varchar(50)
);