from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Many - to - many relationships
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
    id = Column(Integer, primary_key=True)
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

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    identifier = Column(String)
    name = Column(String)
    system = Column(String)
    assets = Column(String)
    steps = Column(String)

class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    identifier = Column(String)
    name = Column(String)
    system = Column(String)
    cases = Column(String)
    comments = Column(Text)

class Requirement(Base):
    __tablename__ = 'requirements'
    
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    definition = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships
    systems = relationship('System', secondary='requirement_systems', back_populates='requirements')
    sections = relationship('Section', secondary='requirement_sections', back_populates='requirements')

class System(Base):
    __tablename__ = 'systems'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship('Requirement', secondary='requirement_systems', back_populates='systems')

class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship('Requirement', secondary='requirement_sections', back_populates='sections')

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

class Uspace(Base):
    __tablename__ = 'uspaces'
    id = Column(Integer, primary_key=True)
    identification = Column(String)
    name = Column(String)
    sectors_number = Column(String)
    file = Column(String)