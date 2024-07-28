from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='pedro2',
        email='pedro2@email.com',
        password='senha',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'pedro2@email.com')
    )

    assert result.id == 1
