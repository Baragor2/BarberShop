"""Initial migration

Revision ID: 85ceacdb9065
Revises: b7c7a4811594
Create Date: 2024-10-17 21:00:06.677497

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '85ceacdb9065'
down_revision: Union[str, None] = 'b7c7a4811594'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('specialist_avatars',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('specialist_avatar', sa.Uuid(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('specialist_avatar')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('specialist_avatars')
    # ### end Alembic commands ###
