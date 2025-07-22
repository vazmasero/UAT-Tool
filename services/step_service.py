from db.db import DatabaseManager
from config.model_domains import Step
from typing import List, Dict, Any, Optional

class StepService:

    def __init__(self, db_manager: DatabaseManager, table_manager=None):
        self.db_manager = db_manager
        self.table_manager = table_manager
        
    def get_requirements(self):
        """Obtains all requirements for their selection in step"""
        requirements = self.db_manager.get_all_data("requirements")
        return [requirement["code"] for requirement in requirements] if requirements else []
    
    def create_step_data(self, step_form_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'action': step_form_data['action'],
            'expected_result': step_form_data['expected_result'],
            'affected_requirements': step_form_data['affected_requirements'], 
            'comments': step_form_data['comments'],
            'case_id': None  
        }
        
    def get_steps_by_case_id(self, case_id: int) -> List[Dict[str, Any]]:
        """Obtiene los steps existentes de un case desde BD"""
        steps_data = self.db_manager.get_filtered_data("steps", {"case_id": case_id})
        
        # Formatear los datos para incluir requirements como lista de códigos
        formatted_steps = []
        for step in steps_data:
            # Obtener requirements asociados al step
            step_requirements = self._get_step_requirements(step['id'])
            step['affected_requirements'] = step_requirements
            formatted_steps.append(step)
            
        return formatted_steps
    
    def _get_step_requirements(self, step_id: int) -> List[str]:
        """Obtiene los codes de requirements asociados a un step"""
        # Aquí necesitarías hacer una consulta a la tabla intermedia
        # Por ahora retorna lista vacía, implementar según tu lógica de BD
        return []
    
    def save_steps_for_case(self, case_id: int, steps_data: List[Dict[str, Any]]) -> None:
        """Guarda todos los steps de un case en la BD"""
        for step_data in steps_data:
            step_data['case_id'] = case_id
            
            # Separar requirements para manejar relación many-to-many
            requirements_codes = step_data.pop('affected_requirements', [])
            
            # Crear el step
            step_id = self.db_manager.create_register("steps", step_data)
            
            # Asociar requirements al step
            self._associate_requirements_to_step(step_id, requirements_codes)
            
    def _associate_requirements_to_step(self, step_id: int, requirement_codes: List[str]):
        """Asocia requirements a un step mediante la tabla intermedia"""
        # Obtener IDs de requirements por sus códigos
        for code in requirement_codes:
            requirement_data = self.db_manager.get_filtered_data("requirements", {"code": code})
            if requirement_data:
                requirement_id = requirement_data[0]['id']
                # Insertar en tabla intermedia step_requirements
                # Implementar según tu lógica de BD para tablas intermedias
                pass
            
    def update_steps_for_case(self, case_id: int, steps_data: List[Dict[str, Any]]) -> None:
        """Actualiza los steps de un case existente"""
        # Eliminar steps existentes del case
        self._delete_steps_by_case_id(case_id)
        
        # Crear los nuevos steps
        self.save_steps_for_case(case_id, steps_data)
        
    def _delete_steps_by_case_id(self, case_id: int):
        """Elimina todos los steps de un case"""
        # Implementar eliminación de steps por case_id
        pass

    def format_step_data(self, data):
        """Formatea datos de step para display en tabla"""
        if not data:
            return None
        
        if 'Id' in data:
            # Header as key (desde tabla):
            return {
                'id': data['Id'],
                'action': data['Action'],
                'expected_result': data['Expected result'],
                'affected_requirements': [r.strip() for r in data['Affected requirements'].split(',')] if data['Affected requirements'] else [],
                'comments': data['Comments'],
            }
        else:
            return data
            
            
