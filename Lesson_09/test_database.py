from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_conection_string = "postgresql://postgres:2821911@localhost:5432/postgres"

db = create_engine(db_conection_string)


def test_select_subject():
    db = create_engine(db_conection_string)
    subject = db.execute('select * from subject').fetchall()
    subject1 = subject[-1]
    assert subject1 == (16, 'Chinese')


def test_insert_subject():
    sql = text("INSERT INTO subject(subject_id, subject_title) VALUES (:new_id, :new_name)")
    new_subject = db.execute(sql, new_id=17, new_name='Suakhily')
    subject = db.execute('select * from subject').fetchall()
    new_subject = subject[-1]
    assert new_subject == (17, 'Suakhily')


def test_update_subject():
    sql = text("update subject set subject_title = 'Farsy' where subject_id = 17")
    update_subject = db.execute(sql)
    subject = db.execute('select * from subject').fetchall()
    update_subject = subject[-1]
    assert update_subject == (17, 'Farsy')


def test_delete_subject():
    sql = text("delete from subject where subject_title = 'Farsy'")
    delete_subject = db.execute(sql)
    subject = db.execute('select * from subject').fetchall()
    delete_subject = subject[-1]
    assert delete_subject != (17, 'Farsy')
