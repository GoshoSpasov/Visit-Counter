\# Visit Counter



Прост уеб проект с брояч на посещения, контейнеризиран с Docker Compose.



\## Структура на проекта



visit-counter/

├── backend/

│   ├── app.py

│   ├── requirements.txt

│   └── Dockerfile

└── compose.yml



\## Компоненти



\*\*backend\*\* — Python/Flask уеб сървър. При всяко посещение записва ред в базата и връща броя посещения.



\*\*database\*\* — PostgreSQL база данни. Съхранява всяко посещение в таблица `visit`.



\## Комуникация между услугите



Двата контейнера са свързани чрез вътрешна Docker мрежа `app-network`. Бекендът се свързва с базата данни по име `database` на порт `5432`.



\## Как се стартира



docker compose up --build



После отвори браузъра на \*\*http://localhost:5000\*\*



\## Docker Hub



Образът на бекенда е публично достъпен на:

\[hub.docker.com/r/georgi8/visit-counter-backend](https://hub.docker.com/r/georgi8/visit-counter-backend)

