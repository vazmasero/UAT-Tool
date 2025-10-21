# 🧩 UAT Tool — Arquitectura y Dependencias

Este documento describe la arquitectura actual del proyecto **UAT Tool**, sus capas principales, dependencias verticales y convenciones de diseño.

---

## 📘 Visión General

La aplicación sigue una arquitectura **en capas (Layered Architecture)**, con separación estricta entre:

- **Presentation Layer (presentación/UI)**
- **Application Layer (servicios, DTOs, contextos, UoW)**
- **Domain Layer (entidades, repositorios abstractos, reglas de negocio)**
- **Infrastructure Layer (implementaciones concretas, DB, ORM)**
- **Shared Layer (utilidades comunes)**

---

## 🧭 Diagrama de Dependencias Verticales (Mermaid)

```mermaid
graph TD

%% CAPAS %%
subgraph Presentation_Layer
PL1[Controllers]
PL2[Dialogs_Views]
PL3[Models_ProxyModels]
PL4[UI_Files]
end

subgraph Application Layer
AL1[Services (BugService, RequirementService, AuxiliaryService)]
AL2[DTOs (FormDTO, TableDTO, ServiceDTO)]
AL3[UnitOfWork (context manager con yield)]
AL4[AppContext (inyección de dependencias)]
AL5[Bootstrap (registro de dependencias)]
end

subgraph Domain Layer
DL1[Entities / Models]
DL2[Repository Interfaces (Protocols)]
DL3[Exceptions]
DL4[Associations y reglas de dominio]
end

subgraph Infrastructure Layer
IL1[SQLAlchemy Repositories (implementan interfaces)]
IL2[Database (engine, base, init_db, utils)]
IL3[Fixtures / Alembic]
end

subgraph Shared Layer
SL1[Logging]
SL2[Constants]
SL3[Utilities]
end

%% DEPENDENCIAS %%
PL1 --> AL1
PL2 --> AL2
PL3 --> AL3
PL4 --> AL3

AL1 --> DL1
AL2 --> DL1
AL3 --> DL2
AL1 --> SL1
PL1 --> SL1

