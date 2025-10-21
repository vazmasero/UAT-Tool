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

## 🧭 Diagrama de Dependencias Verticales

```mermaid
graph TD

%% CAPAS %%
A[Presentation Layer\n(controllers, dialogs, views, models, UI)] --> B[Application Layer\n(services, DTOs, UoW, AppContext)]
B --> C[Domain Layer\n(entities, repository interfaces, exceptions)]
C --> D[Infrastructure Layer\n(repositorios concretos, database, ORM)]
B --> E[Shared Layer\n(logging, constants, utils)]
A --> E

%% ETIQUETAS %%
subgraph "Presentation Layer"
A1[Controllers]
A2[Dialogs & Views]
A3[Models & ProxyModels]
A4[UI (.ui y generados .py)]
end

subgraph "Application Layer"
B1[Services\n(BugService, RequirementService, etc.)]
B2[DTOs\n(FormDTO, TableDTO, ServiceDTO)]
B3[UnitOfWork\n(context manager con yield)]
B4[AppContext\n(inyección de dependencias)]
B5[Bootstrap\n(inicio y registro de dependencias)]
end

subgraph "Domain Layer"
C1[Entities / Models]
C2[Repository Interfaces\n(Protocols)]
C3[Exceptions]
C4[Associations y reglas de dominio]
end

subgraph "Infrastructure Layer"
D1[SQLAlchemy Repositories\n(implementan interfaces)]
D2[Database\n(engine, base, init_db, utils)]
D3[Fixtures / Alembic]
end

subgraph "Shared Layer"
E1[Logging]
E2[Constants]
E3[Utilities]
end



