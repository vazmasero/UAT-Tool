# 🔄 Flujo Horizontal — UAT Tool

Este diagrama muestra el **recorrido de una operación típica**  
(por ejemplo: “crear bug”, “editar requirement”, “cargar lista de bugs”),  
desde la capa de presentación hasta la base de datos.

---

## 🧭 Diagrama de Flujo de Ejecución (Horizontal)

```mermaid
sequenceDiagram
    participant UI as 🪟 UI / View (form_bug.ui)
    participant CTRL as 🎮 Controller (BugTabController)
    participant SRV as ⚙️ Service (BugService)
    participant APPCTX as 🧰 AppContext
    participant UOW as 🔄 UnitOfWork (context manager)
    participant REPO as 🧾 Repository (BugRepository)
    participant DB as 🗄️ Database (SQLAlchemy / Engine)

    Note over UI,SRV: 🧩 Capa de Presentación → Capa de Aplicación

    UI->>CTRL: Usuario hace clic en "Guardar bug"
    CTRL->>SRV: Llama a create_bug_from_form(form_dto)
    SRV->>APPCTX: Solicita get_unit_of_work_context()
    APPCTX->>UOW: Crea nueva sesión y UoW
    activate UOW
    SRV->>UOW: Usa uow.bug_repo.create(data)
    UOW->>REPO: Repositorio crea entidad SQLAlchemy
    REPO->>DB: INSERT INTO bugs (...)
    DB-->>REPO: Retorna instancia persistida
    REPO-->>UOW: Retorna entidad creada
    UOW-->>SRV: Retorna entidad Bug
    deactivate UOW
    SRV-->>CTRL: Devuelve BugServiceDTO
    CTRL-->>UI: Refresca tabla de bugs en la interfaz

    Note over SRV,REPO: 🔐 El servicio nunca conoce SQLAlchemy directamente
```
