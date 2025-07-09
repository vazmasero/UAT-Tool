from sqlalchemy.orm import Session
from db.models import System, Section

def load_initial_data(session: Session):
    # Predefined systems
    systems = ["USSP", "CISP", "AUDI", "EXCHANGE", "NA"]
    
    # Predefined sections 
    sections = [
        "General", "Regulation", "Testing environment", "HMI", "GCS API",
        "User management", "NID", "Geo-awareness", "UAS flight authorization",
        "Traffic info", "DAIM", "Weather", "Conformance monitoring",
        "Tracking", "Conflict management", "ATM/U-space", "Billing",
        "Emergency management", "NA"
    ]
    
    for system_name in systems: 
        if not session.query(System).filter_by(name=system_name).first():
            session.add(System(name=system_name))
    
    for section_name in sections: 
        if not session.query(Section).filter_by(name=section_name).first():
            session.add(Section(name=section_name))
            
    session.commit()