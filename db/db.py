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
                elif key == 'blocks':
                    if hasattr(item, 'cases'):
                        item_dict['cases'] = len(item.cases)
                
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

        # --- Bugs ---
        if key == 'bugs':
            try:
                with self.session.no_autoflush:

                    system = None
                    if 'system_id' in data and data['system_id']:
                        system = self.session.query(System).filter_by(name=data['system_id']).first()
                    campaign = None
                    if 'campaign_id' in data and data['campaign_id']:
                        campaign = self.session.query(Campaign).filter_by(id=data['campaign_id']).first()
                    requirements = []
                    if 'requirements' in data and data['requirements']:
                        requirements = self.session.query(Requirement).filter(
                            Requirement.code.in_(data['requirements'])
                        ).all()

                    bug = model(
                        status=data.get('status'),
                        system=system,
                        campaign=campaign,
                        version=data.get('version'),
                        creation_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        last_update=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        service_now_id=data.get('service_now_id'),
                        short_desc=data.get('short_desc'),
                        definition=data.get('definition'),
                        urgency=data.get('urgency'),
                        impact=data.get('impact'),
                        comments=data.get('comments'),
                        file=data.get('file')
                    )
                    self.session.add(bug)
                    self.session.flush()
    
                    # Many-to-many: requirements
                    bug.requirements = requirements

                    # History log
                    bug.log = self.append_bug_log("", "Bug created")
    
                    self.session.commit()
                    return bug.id
            except Exception as e:
                self.session.rollback()
                raise e
    
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
            
        # --- Case for blocks and cases --- 
        if key == "blocks":
            try:
                with self.session.no_autoflush:
                    # Crear el bloque con los campos básicos
                    block = model(
                        identification=data.get('identification'),
                        name=data.get('name'),
                        system=data.get('system'),
                        comments=data.get('comments')
                    )
                    self.session.add(block)
                    self.session.flush()  # Para obtener block.id

                    # Relacionar casos (many-to-many)
                    if "cases" in data and data["cases"]:
                        block.cases.clear()
                        for case_id in data["cases"]:
                            case = self.session.query(Case).get(case_id)
                            if case:
                                block.cases.append(case)

                    self.session.commit()
                    return block.id
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

            # --- BUGS ---
            if key == 'bugs':
                basic_fields = [
                'status', 'version', 'service_now_id', 'short_desc', 'definition',
                'urgency', 'impact', 'comments', 'file'
                ]
                for field in basic_fields:
                    if field in data:
                        setattr(record, field, data[field])

                # Actualizar relaciones
                if 'system' in data and data['system']:
                    system = self.session.query(System).filter_by(name=data['system']).first()
                    record.system = system

                if 'campaign' in data and data['campaign']:
                    campaign = self.session.query(Campaign).filter_by(identifier=data['campaign']).first()
                    record.campaign = campaign

                if 'requirements' in data and data['requirements']:
                    requirements = self.session.query(Requirement).filter(
                        Requirement.code.in_(data['requirements'])
                    ).all()
                    record.requirements = requirements

                # History log
                record.log = self.append_bug_log(record.log, f"Bug edited (status: {record.status})")

            # --- REQUIREMENTS ---
            elif key == 'requirements':
                basic_fields = ['code', 'definition', 'last_update']
                for field in basic_fields:
                    if field in data:
                        setattr(record, field, data[field])
                
                # Many-to-many: systems
                if 'systems' in data: 
                    record.systems.clear()
                    if data['systems']:
                        system_names = data['systems'] if isinstance(data['systems'], list) else [s.strip() for s in data['systems'].split(',')]
                        for system_name in system_names:
                            system = self.session.query(System).filter_by(name=system_name).first()
                            if system:
                                record.systems.append(system)
                
                # Many-to-many: sections
                if 'sections' in data:
                    record.sections.clear()
                    if data['sections']:
                        section_names = data['sections'] if isinstance(data['sections'], list) else [s.strip() for s in data['sections'].split(',')]
                        for section_name in section_names:
                            section = self.session.query(Section).filter_by(name=section_name).first()
                            if section:
                                record.sections.append(section)

            # --- BLOCKS --- 
            elif key == 'blocks':
                basic_fields = ['identification', 'name', 'system', 'comments']
                for field in basic_fields:
                    if field in data:
                        setattr(record, field, data[field])

                # Relacionar casos (many-to-many)
                if "cases" in data:
                    record.cases.clear()
                    if data["cases"]:
                        for case_id in data["cases"]:
                            case = self.session.query(Case).get(case_id)
                            if case:
                                record.cases.append(case)

            # --- CASES ---
            elif key == 'cases':
                basic_fields = ['identification', 'name', 'comments']
                for field in basic_fields:
                    if field in data:
                        setattr(record, field, data[field])
            
                # Many-to-many: systems
                if 'systems' in data: 
                    record.systems.clear()
                    if data['systems']:
                        system_names = data['systems'] if isinstance(data['systems'], list) else [s.strip() for s in data['systems'].split(',')]
                        for system_name in system_names:
                            system = self.session.query(System).filter_by(name=system_name).first()
                            if system:
                                record.systems.append(system)

                # Many-to-many: sections
                if 'sections' in data:
                    record.sections.clear()
                    if data['sections']:
                        section_names = data['sections'] if isinstance(data['sections'], list) else [s.strip() for s in data['sections'].split(',')]
                        for section_name in section_names:
                            section = self.session.query(Section).filter_by(name=section_name).first()
                            if section:
                                record.sections.append(section)

                # Many-to-many: operators
                if 'operators' in data:
                    record.operators.clear()
                    if data['operators']:
                        operator_names = data['operators'] if isinstance(data['operators'], list) else [o.strip() for o in data['operators'].split(',')]
                        for operator_name in operator_names:
                            operator = self.session.query(Operator).filter_by(name=operator_name).first()
                            if operator:
                                record.operators.append(operator)

                # Many-to-many: drones
                if 'drones' in data:
                    record.drones.clear()
                    if data['drones']:
                        drone_names = data['drones'] if isinstance(data['drones'], list) else [d.strip() for d in data['drones'].split(',')]
                        for drone_name in drone_names:
                            drone = self.session.query(Drone).filter_by(name=drone_name).first()
                            if drone:
                                record.drones.append(drone)

                # Many-to-many: uhub_users
                if 'uhub_users' in data:
                    record.uhub_users.clear()
                    if data['uhub_users']:
                        user_names = data['uhub_users'] if isinstance(data['uhub_users'], list) else [u.strip() for u in data['uhub_users'].split(',')]
                        for user_name in user_names:
                            user = self.session.query(UhubUser).filter_by(username=user_name).first()
                            if user:
                                record.uhub_users.append(user)

                # --- STEPS ---
                if 'steps' in data:
                    existing_steps = {step.id: step for step in record.steps}
                    updated_step_ids = set()

                    for step_data in data['steps']:
                        step_id = step_data.get('id')
                        if step_id and step_id in existing_steps:
                            # Actualizar step existente
                            step = existing_steps[step_id]
                            step.action = step_data.get('action', step.action)
                            step.expected_result = step_data.get('expected_result', step.expected_result)
                            step.comments = step_data.get('comments', step.comments)
                            # Actualizar requirements asociados
                            if 'affected_requirements' in step_data:
                                step.affected_requirements.clear()
                                for req_code in step_data['affected_requirements']:
                                    req = self.session.query(Requirement).filter_by(code=req_code).first()
                                    if req:
                                        step.affected_requirements.append(req)
                            updated_step_ids.add(step_id)

                        else:
                            # Nuevo step
                            new_step = Step(
                                action=step_data.get('action'),
                                expected_result=step_data.get('expected_result'),
                                comments=step_data.get('comments'),
                                case=record
                            )
                            self.session.add(new_step)
                            # Asociar requirements
                            if 'affected_requirements' in step_data:
                                for req_code in step_data['affected_requirements']:
                                    req = self.session.query(Requirement).filter_by(code=req_code).first()
                                    if req:
                                        new_step.affected_requirements.append(req)

                    # Eliminar steps que ya no están
                    for step_id, step in existing_steps.items():
                        if step_id not in updated_step_ids:
                            self.session.delete(step)
            
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
        
    @staticmethod
    def append_bug_log(existing_log: str, action: str) -> str:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{action} at {now}"
        if existing_log:
            return existing_log + "\n" + entry
        else:   
            return entry


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

            elif key == 'blocks':
                # Associated cases
                if hasattr(record, 'cases'):
                    result['cases'] = []
                for case in record.cases:
                    case_dict = {
                        'id': case.id,
                        'identification': case.identification,
                        'name': case.name,
                        'comments': case.comments
                    }
                    result['cases'].append(case_dict)

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
