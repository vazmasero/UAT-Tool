from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

"""Many - to - many relationships"""

# Requirements
requirement_systems = Table(
    'requirement_systems',
    Base.metadata,
    Column('requirement_id', Integer, ForeignKey('requirements.id'), primary_key=True),
    Column('system_id', Integer, ForeignKey('systems.id'), primary_key=True)
)

requirement_sections = Table(
    'requirement_sections',
    Base.metadata,
    Column('requirement_id', Integer, ForeignKey('requirements.id'), primary_key=True),
    Column('section_id', Integer, ForeignKey('sections.id'), primary_key=True)
)

# Cases
case_systems = Table(
    'case_systems',
    Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('system_id', Integer, ForeignKey('systems.id'), primary_key=True)
)

case_sections = Table(
    'case_sections',
    Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('section_id', Integer, ForeignKey('sections.id'), primary_key=True)
)

case_operators = Table(
    'case_operators',
    Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('operator_id', Integer, ForeignKey('operators.id'), primary_key=True)
)

case_drones = Table(
    'case_drones',
    Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('drone_id', Integer, ForeignKey('drones.id'), primary_key=True)
)

case_uhub_users = Table(
    'case_uhub_users',
    Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('uhub_user_id', Integer, ForeignKey('uhub_users.id'), primary_key=True)
)

# Steps
step_requirements = Table(
    'step_requirements',
    Base.metadata,
    Column('step_id', Integer, ForeignKey('steps.id'), primary_key=True),
    Column('requirement_id', Integer, ForeignKey('requirements.id'), primary_key=True)
)

# Tabla intermedia para la relación many-to-many Block <-> Case
block_cases = Table(
    'block_cases',
    Base.metadata,
    Column('block_id', Integer, ForeignKey('blocks.id'), primary_key=True),
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True)
)

class Bug(Base):
    __tablename__ = 'bugs'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    system = Column(String)
    version = Column(String)
    creation_time = Column(String)
    last_update = Column(String)
    service_now_id = Column(String)
    campaign = Column(String)
    requirements = Column(String)
    short_desc = Column(String)
    definition = Column(Text)
    urgency = Column(String)
    impact = Column(String)
    comments = Column(Text)

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True, autoincrement=True)
    identifier = Column(String)
    description = Column(Text)
    system = Column(String)
    version = Column(String)
    test_blocks = Column(String)
    passed = Column(String)
    success = Column(String)
    creation_time = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    last_update = Column(String)
    comments = Column(Text)

class Step(Base):
    __tablename__ = 'steps'
    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(Text)
    expected_result = Column(Text)
    comments = Column(Text)

    # Foreign key to Case
    case_id = Column(Integer, ForeignKey('cases.id'))
    case = relationship('Case', back_populates='steps')

    affected_requirements = relationship('Requirement', secondary=step_requirements, back_populates='steps')

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True, autoincrement=True)
    identification = Column(String)
    name = Column(String)
    comments = Column(Text)

    # Relationships many to many
    systems = relationship('System', secondary=case_systems, back_populates='cases')
    operators = relationship('Operator', secondary=case_operators, back_populates='cases')
    drones = relationship('Drone', secondary=case_drones, back_populates='cases')
    uhub_users = relationship('UhubUser', secondary=case_uhub_users, back_populates='cases')
    sections = relationship('Section', secondary=case_sections, back_populates='cases')

    # Relationship one to many
    steps = relationship('Step', back_populates='case', cascade='all, delete-orphan')

    # Relación inversa many-to-many con Block
    blocks = relationship('Block', secondary=block_cases, back_populates='cases')

class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    identification = Column(String)
    name = Column(String)
    system = Column(String)
    comments = Column(Text)

    # Relación many-to-many con Case
    cases = relationship('Case', secondary=block_cases, back_populates='blocks')

class Requirement(Base):
    __tablename__ = 'requirements'
    
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    definition = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships
    systems = relationship('System', secondary=requirement_systems, back_populates='requirements')
    sections = relationship('Section', secondary=requirement_sections, back_populates='requirements')
    steps = relationship('Step', secondary=step_requirements, back_populates='affected_requirements')

class System(Base):
    __tablename__ = 'systems'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship('Requirement', secondary=requirement_systems, back_populates='systems')
    cases = relationship('Case', secondary=case_systems, back_populates='systems')

class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship('Requirement', secondary=requirement_sections, back_populates='sections')
    cases = relationship('Case', secondary=case_sections, back_populates='sections')

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Operator(Base):
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    easa_id = Column(String)
    verification_code = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)

    # Relationships
    cases = relationship('Case', secondary=case_operators, back_populates='operators')

class Drone(Base):
    __tablename__ = 'drones'
    id = Column(Integer, primary_key=True)
    operator = Column(String)
    name = Column(String)
    sn = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    tracker_type = Column(String)
    transponder_id = Column(String)

    # Relationships
    cases = relationship('Case', secondary=case_drones, back_populates='drones')

class UasZone(Base):
    __tablename__ = 'uas_zones'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reason = Column(String)
    cause = Column(String)
    restriction_type = Column(String)
    activation_time = Column(String)
    authority = Column(String)

class UhubOrg(Base):
    __tablename__ = 'uhub_orgs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    jurisdiction = Column(String)
    aoi = Column(String)
    email = Column(String)
    phone = Column(String)

class UhubUser(Base):
    __tablename__ = 'uhub_users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    organization = Column(String)
    role = Column(String)
    jurisdiction = Column(String)
    aoi = Column(String)

    # Relationships
    cases = relationship('Case', secondary=case_uhub_users, back_populates='uhub_users')

class Uspace(Base):
    __tablename__ = 'uspaces'
    id = Column(Integer, primary_key=True, autoincrement=True)
    identification = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sectors_number = Column(String, nullable=False)
    file = Column(Text, nullable=True)