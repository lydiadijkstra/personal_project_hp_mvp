"""Add role column to users table

Revision ID: 8aef51c0c2cd
Revises: fad2f775af95
Create Date: 2024-11-22 00:28:11.515144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8aef51c0c2cd'
down_revision: Union[str, None] = 'fad2f775af95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add role column
    op.add_column('users', sa.Column('role', sa.Enum('user', 'admin', name='userrole'), nullable=True))

    # Update or remove unnecessary columns
    op.add_column('users', sa.Column('user_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(), nullable=True))

    # Alter column type for created_at (make sure it's TIMESTAMP if needed)
    op.alter_column('users', 'created_at',
                    existing_type=sa.DATETIME(),
                    type_=sa.TIMESTAMP(),
                    existing_nullable=True,
                    existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))

    # Create index for user_id
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)

    # Drop old columns if not needed anymore
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')


def downgrade() -> None:
    # Reverse the changes made in the upgrade
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(), nullable=True))

    op.drop_index(op.f('ix_users_user_id'), table_name='users')

    # Revert created_at column type if needed
    op.alter_column('users', 'created_at',
                    existing_type=sa.TIMESTAMP(),
                    type_=sa.DATETIME(),
                    existing_nullable=True,
                    existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))

    # Remove newly added columns
    op.drop_column('users', 'location')
    op.drop_column('users', 'name')
    op.drop_column('users', 'user_name')
    op.drop_column('users', 'role')  # Don't forget to remove the role column if rolling back
