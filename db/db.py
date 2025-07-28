import os
import datetime
from typing import Any, Dict
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from .models import (Base, Bug, Campaign, Case, Block, Requirement, System, Step,
                    Section, Email, Operator, Drone, UasZone, UhubOrg, UhubUser, Uspace)
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
            'steps': Step,
            'emails': Email,
            'operators': Operator,
            'drones': Drone,
            'uas_zones': UasZone,
            'uhub_orgs': UhubOrg,
            'uhub_users': UhubUser,
            'uspaces': Uspace
        }
        self.session = Session()
    
    def get_all_data(self, key):
        """Obtains all items from a table."""
        model_class = self._model_map.get(key)
        if not model_class:
            return []

        try:
            query = self.session.query(model_class)
            results = []
            
            for item in query.all():
                item_dict = {c.name: getattr(item, c.name) for c in inspect(model_class).columns}
                
                # Manejar relaciones muchos-a-muchos
                if key == 'requirements':
                    if hasattr(item, 'systems'):
                        item_dict['systems'] = ", ".join([sys.name for sys in item.systems])
                    if hasattr(item, 'sections'):
                        item_dict['sections'] = ", ".join([sec.name for sec in item.sections])
                elif key == 'cases':
                    if hasattr(item, 'systems'):
                        item_dict['systems'] = ", ".join([sys.name for sys in item.systems])
                    if hasattr(item, 'sections'):
                        item_dict['sections'] = ", ".join([sec.name for sec in item.sections])
                    if hasattr(item, 'operators'):
                        item_dict['operators'] = ", ".join([op.name for op in item.operators])
                    if hasattr(item, 'drones'):
                        item_dict['drones'] = ", ".join([drone.name for drone in item.drones])
                    if hasattr(item, 'uhub_users'):
                        item_dict['uhub_users'] = ", ".join([user.username for user in item.uhub_users])
                    if hasattr(item, 'steps'):
                        item_dict['steps'] = len(item.steps)
                
                results.append(item_dict)
                
            return results
            
        except Exception as e:
            self.session.rollback()
            print(f"Error obtaining data from {key}: {e}")
            return []

     
    def create_register(self, key: str, data: Dict[str, Any]) -> int:
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
    
        model = self._model_map[key]
    
        # --- Caso especial para requirements ---
        if key == 'requirements':
            try:
                with self.session.no_autoflush:
                    requirement = model(
                        code=data.get('code'),
                        definition=data.get('definition')
                    )
                    self.session.add(requirement)
                    self.session.flush()
    
                    # Many-to-many: systems
                    if 'systems' in data and data['systems']:
                        systems = self.session.query(System).filter(
                            System.name.in_(data['systems'])
                        ).all()
                        requirement.systems = systems
    
                    # Many-to-many: sections
                    if 'sections' in data and data['sections']:
                        sections = self.session.query(Section).filter(
                            Section.name.in_(data['sections'])
                        ).all()
                        requirement.sections = sections
    
                    self.session.commit()
                    return requirement.id
            except Exception as e:
                self.session.rollback()
                raise e
    
        # --- Caso general para el resto de modelos ---
        obj = model()
        for field, value in data.items():
            if field in ("systems", "sections", "operators", "drones", "uhub_users", "affected_requirements"):
                continue
            if hasattr(obj, field):
                setattr(obj, field, value)
    
        self.session.add(obj)
        self.session.commit()
        obj_id = obj.id
    
        # Relaciones para CASES
        if key == "cases":
            # Systems
            if "systems" in data and data["systems"]:
                obj.systems.clear()
                for system_name in data["systems"]:
                    system = self.session.query(System).filter_by(name=system_name).first()
                    if system:
                        obj.systems.append(system)
            # Sections
            if "sections" in data and data["sections"]:
                obj.sections.clear()
                for section_name in data["sections"]:
                    section = self.session.query(Section).filter_by(name=section_name).first()
                    if section:
                        obj.sections.append(section)
            # Operators
            if "operators" in data and data["operators"]:
                obj.operators.clear()
                for operator_name in data["operators"]:
                    operator = self.session.query(Operator).filter_by(name=operator_name).first()
                    if operator:
                        obj.operators.append(operator)
            # Drones
            if "drones" in data and data["drones"]:
                obj.drones.clear()
                for drone_name in data["drones"]:
                    drone = self.session.query(Drone).filter_by(name=drone_name).first()
                    if drone:
                        obj.drones.append(drone)
            # Uhub users
            if "uhub_users" in data and data["uhub_users"]:
                obj.uhub_users.clear()
                for user_name in data["uhub_users"]:
                    user = self.session.query(UhubUser).filter_by(username=user_name).first()
                    if user:
                        obj.uhub_users.append(user)
            self.session.commit()
    
        # Relaciones para STEPS (many-to-many con requirements)
        if key == "steps" and "affected_requirements" in data and data["affected_requirements"]:
            obj.affected_requirements.clear()
            for req_code in data["affected_requirements"]:
                requirement = self.session.query(Requirement).filter_by(code=req_code).first()
                if requirement:
                    obj.affected_requirements.append(requirement)
            self.session.commit()
    
        return obj_id

        
        
    def edit_register(self, key, id, data):
        """Edita un registro existente en la tabla especificada."""
        if key not in self._model_map:
            available_keys = ', '.join(self._model_map.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
    
        model = self._model_map[key]
        current_time = datetime.datetime.now()
    
        try:
            record = self.session.query(model).get(id)
            if not record:
                return False
    
            # Si los datos vienen como tupla, convertirlos a diccionario
            if isinstance(data, (list, tuple)):
                inspector = inspect(model)
                column_names = [c.key for c in inspector.columns]
                data = dict(zip(column_names[1:], data[1:]))  # Excluimos el ID
    
            # Manejar relaciones muchos-a-muchos especiales
            if key == 'requirements':
                # Actualizar campos básicos (excluyendo relaciones)
                basic_fields = ['code', 'definition', 'last_update']
                for field in basic_fields:
                    if field in data:
                        setattr(record, field, data[field])
                
                # Manejar relación con systems
                if 'systems' in data:
                    record.systems.clear()  # Limpiar relaciones existentes
                    if data['systems']:
                        if isinstance(data['systems'], str):
                            # Si viene como string, dividir por comas
                            system_names = [name.strip() for name in data['systems'].split(',')]
                        elif isinstance(data['systems'], list):
                            system_names = data['systems']
                        else:
                            system_names = []
                        
                        # Obtener objetos System por nombre
                        for system_name in system_names:
                            system = self.session.query(System).filter_by(name=system_name).first()
                            if system:
                                record.systems.append(system)
                
                # Manejar relación con sections
                if 'sections' in data:
                    record.sections.clear()  # Limpiar relaciones existentes
                    if data['sections']:
                        if isinstance(data['sections'], str):
                            # Si viene como string, dividir por comas
                            section_names = [name.strip() for name in data['sections'].split(',')]
                        elif isinstance(data['sections'], list):
                            section_names = data['sections']
                        else:
                            section_names = []
                        
                        # Obtener objetos Section por nombre
                        for section_name in section_names:
                            section = self.session.query(Section).filter_by(name=section_name).first()
                            if section:
                                record.sections.append(section)
            
            else:
                # Para otros modelos, actualizar campos normalmente
                for field, value in data.items():
                    if hasattr(record, field):
                        setattr(record, field, value)
    
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
            record = self.session.query(model).get(id)
            if not record:
                return None
            
            # Convertir a diccionario incluyendo relaciones
            result = {}
            
            # Campos básicos
            for column in inspect(model).columns:
                result[column.name] = getattr(record, column.name)
            
            # Manejar relaciones muchos-a-muchos
            if key == 'requirements':
                if hasattr(record, 'systems'):
                    result['systems'] = [sys.name for sys in record.systems]
                if hasattr(record, 'sections'):
                    result['sections'] = [sec.name for sec in record.sections]

            elif key == 'cases':
                # Systems
                if hasattr(record, 'systems'):
                    result['systems'] = [sys.name for sys in record.systems]
                # Sections
                if hasattr(record, 'sections'):
                    result['sections'] = [sec.name for sec in record.sections]
                # Operators
                if hasattr(record, 'operators'):
                    result['operators'] = [op.name for op in record.operators]
                # Drones
                if hasattr(record, 'drones'):
                    result['drones'] = [drone.name for drone in record.drones]
                # Uhub users
                if hasattr(record, 'uhub_users'):
                    result['uhub_users'] = [user.username for user in record.uhub_users]
                
                # Associated steps
                if hasattr(record, 'steps'):
                    result['steps'] = []
                for step in record.steps:
                    step_dict = {
                        'id': step.id,
                        'action': step.action,
                        'expected_result': step.expected_result,
                        'comments': step.comments,
                        'affected_requirements': [req.code for req in step.affected_requirements] if hasattr(step, 'affected_requirements') else []
                    }
                    result['steps'].append(step_dict)
            
            return result
            
        except Exception as e:
            print(f"Error getting record by ID: {e}")
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
