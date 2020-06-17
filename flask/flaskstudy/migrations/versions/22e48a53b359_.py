"""empty message

Revision ID: 22e48a53b359
Revises: 
Create Date: 2020-06-03 17:03:04.412447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22e48a53b359'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('addressname', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('story_section')
    op.drop_table('story_title')
    op.drop_table('story_info')
    op.drop_table('story_queue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('story_queue',
    sa.Column('queue_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment='队列号'),
    sa.Column('section_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='栏目编号'),
    sa.Column('story_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='故事编号'),
    sa.Column('result', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='推送结果： 0-待推送 ，1-推送成功 ，2-推送失败'),
    sa.Column('count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='推送次数'),
    sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='创建日期'),
    sa.Column('update_time', mysql.DATETIME(), nullable=True, comment='修改日期'),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='是否已删除  0 - 未删除，1-已删除'),
    sa.Column('update_role', mysql.VARCHAR(length=64), nullable=True, comment='更新人'),
    sa.ForeignKeyConstraint(['section_id'], ['story_section.section_id'], name='story_queue_ibfk_1'),
    sa.ForeignKeyConstraint(['story_id'], ['story_title.story_id'], name='story_queue_ibfk_2'),
    sa.PrimaryKeyConstraint('queue_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('story_info',
    sa.Column('storyinfo_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment='编号'),
    sa.Column('story_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='故事编号'),
    sa.Column('comments', mysql.TEXT(), nullable=True, comment='正文'),
    sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='创建日期'),
    sa.Column('update_time', mysql.DATETIME(), nullable=True, comment='修改日期'),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='是否已删除  0 - 未删除，1-已删除'),
    sa.Column('update_role', mysql.VARCHAR(length=64), nullable=True, comment='更新人'),
    sa.ForeignKeyConstraint(['story_id'], ['story_title.story_id'], name='story_info_ibfk_1'),
    sa.PrimaryKeyConstraint('storyinfo_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('story_title',
    sa.Column('story_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment='故事编号'),
    sa.Column('section_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='栏目编号'),
    sa.Column('story_name', mysql.VARCHAR(length=128), nullable=True, comment='故事名称'),
    sa.Column('url', mysql.VARCHAR(length=128), nullable=True, comment='故事地址'),
    sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='创建日期'),
    sa.Column('update_time', mysql.DATETIME(), nullable=True, comment='修改日期'),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='是否已删除  0 - 未删除，1-已删除'),
    sa.Column('update_role', mysql.VARCHAR(length=64), nullable=True, comment='更新人'),
    sa.ForeignKeyConstraint(['section_id'], ['story_section.section_id'], name='story_title_ibfk_1'),
    sa.PrimaryKeyConstraint('story_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('story_section',
    sa.Column('section_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('section', mysql.VARCHAR(length=64), nullable=True, comment='栏目名称'),
    sa.Column('url', mysql.VARCHAR(length=128), nullable=True, comment='栏目地址'),
    sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='创建日期'),
    sa.Column('update_time', mysql.DATETIME(), nullable=True, comment='修改日期'),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='是否已删除  0 - 未删除，1-已删除'),
    sa.Column('update_role', mysql.VARCHAR(length=64), nullable=True, comment='更新人'),
    sa.PrimaryKeyConstraint('section_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('user')
    op.drop_table('address')
    # ### end Alembic commands ###