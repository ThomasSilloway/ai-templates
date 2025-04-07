# Product Requirements Document: Svelte Counter App with Docker Setup

## 1. Introduction

This document outlines the requirements for setting up a basic Svelte application containerized with Docker to be deployed locally on a Windows machine. The initial application will be a simple counter that increments when a button is clicked. This setup will serve as the foundation for the more complex "Beard or Shave" interactive Twitch stream application.

## 2. Goals

* Establish a working Docker environment for Svelte development on Windows.
* Create a minimal Svelte application (a counter) to verify the setup.
* Implement hot-reloading within the Docker container for an efficient development workflow.

## 3. Scope

This initial phase focuses solely on setting up the development environment with a basic Svelte counter app. It includes:

* Creating a basic Svelte application.
* Writing a `Dockerfile` for containerizing the Svelte app.
* Creating a `docker-compose.dev.yaml` file for managing the development environment with hot-reloading.
* Configuring Svelte/Vite for hot-reloading within Docker.
* Documenting the steps to run the application locally using Docker.

## 4. Technical Requirements

* **Svelte:** The front-end framework for building the user interface.
* **Vite:** The build tool and development server for Svelte.
* **Docker:** The containerization platform.
* **Docker Compose:** A tool for defining and managing multi-container Docker applications.
* **Operating System:** Windows (local development environment).

## 5. Functional Requirements

1.  **Basic Svelte Counter App:**
    * Display a numerical counter, initialized to 0.
    * Include a button labeled "Increment".
    * Clicking the "Increment" button should increase the counter value by 1.
    * The counter value should be displayed on the page.
2.  **Docker Containerization:**
    * The Svelte application should be containerized using Docker.
    * The Docker image should be based on a minimal Node.js Alpine image.
    * The Dockerfile should follow best practices for containerizing Svelte applications, including setting up a development environment.
3.  **Hot-Reloading:**
    * Changes made to the Svelte application code on the host machine should be automatically reflected in the running Docker container without a full rebuild or manual refresh.
    * Hot Module Replacement (HMR) should be configured to update the browser with code changes.
4.  **Local Deployment:**
    * The application should be deployable and accessible locally on the Windows machine using Docker Compose.

## 6. Docker Setup Details (Based on Provided Best Practices)

### 6.1. `Dockerfile.dev`

```dockerfile
FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000
EXPOSE 24678

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

6.2. docker-compose.dev.yaml
```
version: '3.8'
services:
  svelte-app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
      - "24678:24678"
    volumes:
      - ./src:/app/src:delegated
      - ./static:/app/static:delegated
      - ./svelte.config.js:/app/svelte.config.js:delegated
      - ./vite.config.js:/app/vite.config.js:delegated
      - ./package.json:/app/package.json:delegated
      - ./package-lock.json:/app/package-lock.json:delegated
    command: npm run dev -- --host 0.0.0.0

```

6.3. svelte.config.js (Vite Configuration for Hot-Reloading)
```
import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: vitePreprocess(),
    kit: {
        adapter: adapter(),
        vite: {
            server: {
                host: '0.0.0.0',
                watch: {
                    usePolling: true
                }
            }
        }
    }
};

export default config;
```

## 7. Development Steps

1.  **Initialize Svelte Project:** Create a new Svelte project using your preferred method (e.g., `npm create svelte@latest counter-app`).
2.  **Implement Counter App:** Modify the `src/App.svelte` file to include the basic counter functionality with a button.
3.  **Create Docker Files:** Create `Dockerfile.dev` and `docker-compose.dev.yaml` in the root of your Svelte project, using the configurations provided in Section 6.
4.  **Configure Vite:** Ensure your `svelte.config.js` includes the necessary Vite server configurations for hot-reloading within Docker as shown in Section 6.3.
5.  **Run with Docker Compose:** Open a terminal in the root of your Svelte project and run the command: `docker-compose -f docker-compose.dev.yaml up --build`.
6.  **Access the Application:** Once the containers are running, access the Svelte counter application in your web browser at `http://localhost:3000`.
7.  **Verify Hot-Reloading:** Make changes to the `src/App.svelte` file and confirm that the changes are automatically reflected in the browser without a manual refresh.

## 8. Success Criteria

* A basic Svelte counter application is running within a Docker container on the local Windows machine.
* The counter increments correctly when the button is clicked.
* Hot-reloading is functional, allowing for rapid development within the containerized environment.
