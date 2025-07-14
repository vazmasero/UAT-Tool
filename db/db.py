import os
from datetime import datetime
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from .models import Base, Bug, Campaign, Case, Block, Requirement, System, Section, Email, Operator, Drone, UasZone, UhubOrg, UhubUser, Uspace
from .initial_data import load_initial_data

DB_NAME = "uat_tool.db"
DATABASE_URL = f"sqlite:///{DB_NAME}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Defines SQLAlchemy Session object
Session = scoped_session(sessionmaker(bind=engine))

def init_db():
    
    # Creates all tables defined in models.py
    Base.metadata.create_all(engine)
    
    # Instantiates session
    session = Session()
    try:
        load_initial_data(session)
    finally:
        session.close()

def get_session():
    """Devuelve una nueva sesión de base de datos."""
    return Session()

class DatabaseManager:
    
    def __init__(self):
        self._model_map = {
            'bugs': Bug,
            'campaigns': Campaign,
            'cases': Case,
            'blocks': Block,
            'requirements': Requirement,
            'systems': System,
            'sections': Section,
            'emails': Email,
            'operators': Operator,
            'drones': Drone,
            'uas_zones': UasZone,
            'uhub_orgs': UhubOrg,
            'uhub_users': UhubUser,
            'uspaces': Uspace
        }
        self.session = Session()
    
    def get_all_data(self, key, custom_columns=None):
        """Obtains all items from a table."""
        if key not in self._model_map:
            raise ValueError(f"Key '{key}' not found. Available keys: {', '.join(self._model_map.keys())}")

        model = self._model_map[key]
        try:
            query = self.session.query(model)
            if custom_columns:
                try:
                    columns = [getattr(model, col.strip()) for col in custom_columns.split(',')]
                    query = self.session.query(*columns)
                except AttributeError as e:
                    raise ValueError(f"Invalid column name in {custom_columns}") from e
            
            results = query.all()
            
            if not custom_columns:
                inspector = inspect(model)
                columns = [c.key for c in inspector.columns]
                if key == 'requirements':
                    return [
                        {
                            **{col: getattr(obj,col) for col in columns},
                            'systems': ', '.join([s.name for s in obj.systems]),
                            'sections': ', '.join([s.name for s in obj.sections])
                        }
                        for obj in results
                    ]

                else:
                    return [
                        {col: getattr(obj, col) for col in columns}
                        for obj in results
                    ]
            
        except Exception as e:
            self.session.rollback()
            print(f"Error getting data: {e}")
            return []

     
    def create_register(self, key:str, data:dict):

        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")

        model = self._model_map[key]
        
        try: 
            with self.session.no_autoflush:
                if key == 'requirements':
                    requirement = model(
                        code=data['code'],
                        definition=data['definition']
                    )
                    self.session.add(requirement)
                    self.session.flush()
                    
                    if 'systems' in data and data['systems']:
                        systems = self.session.query(System).filter(
                            System.name.in_(data['systems'])
                        ).all()
                        requirement.systems = systems
                        
                    if 'sections' in data and data['sections']:
                        sections = self.session.query(Section).filter(
                            Section.name.in_(data['sections'])
                        ).all()
                        requirement.sections = sections
                
                    self.session.add(requirement)
                else:
                    new_record = model(**data)
                    self.session.add(new_record)
                
                self.session.commit()
            
        except Exception as e:
            self.session.rollback()
            raise e
        
    def edit_register(self, key, id, data):
        """Edita un registro existente en la tabla especificada."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")

        model = self._model_map[key]
        current_time = datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M")

        try:
            record = self.session.query(model).get(id)
            if not record:
                return False

            # Si los datos vienen como tupla, convertirlos a diccionario
            if isinstance(data, (list, tuple)):
                inspector = inspect(model)
                column_names = [c.key for c in inspector.columns]
                data = dict(zip(column_names[1:], data[1:]))  # Excluimos el ID

            # Actualizar campos
            for key, value in data.items():
                setattr(record, key, value)

            # Actualizar last_update si existe
            if hasattr(record, 'last_update'):
                record.last_update = current_time

            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error editing register: {e}")
            return False

    def get_by_id(self, key, id):
        """Obtiene un registro por su ID."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
        
        model = self._model_map[key]
        try:
            return self.session.query(model).get(id)
        except Exception as e:
            print(f"Error getting record: {e}")
            return None

    def filter_by(self, key, **kwargs):
        """Filtra registros por criterios específicos."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
        
        model = self._model_map[key]
        try:
            return self.session.query(model).filter_by(**kwargs).all()
        except Exception as e:
            print(f"Error filtering records: {e}")
            return []

    def delete_register(self, key, id):
        """Elimina un registro por su ID."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
        
        model = self._model_map[key]
        try:
            record = self.session.query(model).get(id)
            if not record:
                return False
            
            self.session.delete(record)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting record: {e}")
            return False

    def count(self, key, **kwargs):
        """Cuenta el número de registros que cumplen con los criterios especificados."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
        
        model = self._model_map[key]
        try:
            query = self.session.query(model)
            if kwargs:
                query = query.filter_by(**kwargs)
            return query.count()
        except Exception as e:
            print(f"Error counting records: {e}")
            return 0

    def __del__(self):
        """Cierra la sesión cuando se destruye el objeto."""
        self.session.close()
