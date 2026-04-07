from sqlalchemy import create_engine, inspect, text
import pytest

db = "postgresql://postgres:123@localhost:5432/Yarch"
engine = create_engine(db)
inspector = inspect(engine)


def test_on_base():
    name = inspector.get_table_names()
    assert name[0] == "users"


def test_select():
    connection = engine.connect()
    result = connection.execute(text("SELECT * FROM users"))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1['user_id'] == 42568
    assert row1['user_email'] == "igorpetrov@mail.ru"
    connection.close()


def test__db_get_g():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("INSERT INTO users(\"user_email\",\"user_id\" ) VALUES (:new_email, :new_id)")
    connection.execute(result, {"new_email": "TESTMAIL", "new_id": 111111})
    transaction.commit()
    connection.close()


@pytest.mark.xfail
def test__db_get_b():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("INSERT INTO users(\"user_email", "user_id\") VALUES (:new_email, :new_id)")  # некоректно указаны маркеры для полей ввода
    connection.execute(result, {"new_email": "TESTMAIL", "new_id": "111111"})
    transaction.commit()
    connection.close()


def test_db_upd_g():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("UPDATE users SET subject_id = :sub_id WHERE user_id = :create_id")
    connection.execute(result, {"sub_id": 9, "create_id": 111111})
    transaction.commit()
    connection.close()


@pytest.mark.xfail
def test_db_upd_b():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("UPDATE users SET subject_id = :sub_id WHERE user_id = :create_id")
    connection.execute(result, {"sub_id": 9, "create_id": 1111112222})  # введен несуществующий id
    transaction.commit()
    connection.close()


def test_db_del_g():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("DELETE FROM users WHERE user_email = :create_mail")
    delete = connection.execute(result, {"create_mail": "TESTMAIL"})
    assert delete.rowcount == 1
    transaction.commit()
    connection.close()


@pytest.mark.xfail
def test_db_del_b():
    connection = engine.connect()
    transaction = connection.begin()
    result = text("DELETE FROM users WHERE user_email = :create_mail")
    delete = connection.execute(result, {"create_mail": "TESTMAI"})  # введен некоректный email
    assert delete.rowcount == 1  # проверка не проходится
    transaction.commit()
    connection.close()
