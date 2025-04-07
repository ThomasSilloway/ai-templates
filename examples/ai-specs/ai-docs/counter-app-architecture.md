# Counter App Technical Architecture Overview

## Core Technologies

### 1. Svelte 5
- Latest version of the reactive component framework
- Uses fine-grained reactivity through runes (new in Svelte 5)
- Compiles components into highly efficient vanilla JavaScript
- Zero virtual DOM, direct DOM manipulation for better performance

### 2. SvelteKit 2.x
- Full-stack application framework built on Svelte
- Provides routing, server-side rendering, and deployment infrastructure
- Version 2.16.0 includes latest features and optimizations

## Architecture Layers

### 1. Build System
- **Vite 6.x** serves as the dev server and build tool
  - Provides HMR (Hot Module Replacement)
  - Handles TypeScript transpilation
  - Bundles for production
  - ESM-first approach for modern JavaScript

- **TypeScript** integration
  - Strict type checking enabled
  - Custom type definitions in app.d.ts
  - Bundler-style module resolution

### 2. Application Framework (SvelteKit)
- **Routing**
  - File-based routing under src/routes
  - +page.svelte files for page components
  - +layout.svelte for shared layouts
  - Support for dynamic routes and route parameters

- **Rendering**
  - Static site generation through @sveltejs/adapter-static
  - Pre-renders all routes at build time
  - Client-side hydration for interactivity
  - No server-side rendering in production (static only)

- **Asset Handling**
  - Static assets served from /static directory
  - Built assets output to .svelte-kit/static
  - Automatic asset optimization during build

### 3. Docker Infrastructure
- **Development Environment**
  - docker-compose.dev.yaml for local development
  - Hot reloading enabled through volume mounts
  - Vite dev server on port 5173
  - HMR websocket on port 24678

- **Production Environment**
  - Multi-stage build process in Dockerfile
  - Node.js Alpine for build stage
  - Nginx Alpine for serving static files
  - Production server on port 80 (mapped to 3456)

### 4. Configuration System
- **Vite Config**
  - SvelteKit plugin configuration
  - Development server settings
  - File watching with polling for Docker compatibility

- **SvelteKit Config**
  - Static adapter configuration
  - Preprocessing setup
  - Build output settings

- **TypeScript Config**
  - Strict mode enabled
  - Path aliases
  - Module resolution settings

## Data Flow

1. **Development Flow**
   ```
   Source Files → Vite Dev Server → Browser
                     ↑
                 File Watcher
                     ↑
                Docker Volume
   ```

2. **Production Build Flow**
   ```
   Source Files → Vite Build → SvelteKit SSG → Static Files → Nginx → Browser
   ```

## Docker Container Architecture

### Development
```
┌─────────────────────────────────────┐
│ Docker Container                    │
│                                    │
│ ┌────────────────┐                 │
│ │  Vite Server   │← Volume Mount   │
│ │    (5173)      │    (src/*)     │
│ └────────────────┘                 │
│                                    │
│ ┌────────────────┐                 │
│ │  HMR WebSocket │                 │
│ │    (24678)     │                 │
│ └────────────────┘                 │
└─────────────────────────────────────┘
```

### Production
```
┌─────────────────────────────────────┐
│ Docker Container                    │
│                                    │
│ ┌────────────────┐                 │
│ │     Nginx      │                 │
│ │     (80)       │                 │
│ └────────────────┘                 │
│         ↑                          │
│ ┌────────────────┐                 │
│ │  Static Files  │                 │
│ │ (.svelte-kit/) │                 │
│ └────────────────┘                 │
└─────────────────────────────────────┘
```

## Building New Features

When implementing new features, consider:

1. **Routing**
   - Add new routes in src/routes
   - Use dynamic parameters for variable content
   - Implement layouts for shared UI elements

2. **Components**
   - Create reusable components in src/lib
   - Use Svelte 5 runes for state management
   - Implement proper TypeScript types

3. **Assets**
   - Place static assets in /static
   - Use $lib alias for component imports
   - Consider asset optimization needs

4. **Building**
   - Test in development with docker-compose.dev.yaml
   - Validate production build with docker-compose.yaml
   - Ensure static generation works as expected

5. **Type Safety**
   - Maintain strict TypeScript checking
   - Update app.d.ts for new types
   - Use proper type imports/exports

## Development Workflow

1. Start development server:
   ```bash
   ./start-counter.bat
   ```
   - Launches Docker container
   - Starts Vite dev server
   - Enables HMR

2. Make changes:
   - Edit files in src/
   - Changes reflect immediately
   - TypeScript errors show in real-time

3. Build for production:
   ```bash
   docker-compose up --build
   ```
   - Creates optimized static build
   - Outputs to .svelte-kit/static
   - Serves via Nginx

## Performance Considerations

1. **Build Optimization**
   - Static adapter pre-renders all routes
   - Vite optimizes asset bundling
   - Nginx serves static files efficiently

2. **Runtime Performance**
   - No server-side rendering overhead
   - Svelte's direct DOM updates
   - Minimal JavaScript payload

3. **Development Experience**
   - Fast HMR through volume mounts
   - TypeScript for code quality
   - Docker for environment consistency

## Extending the Architecture

To add new capabilities:

1. **New Dependencies**
   - Add to package.json
   - Update Docker builds
   - Consider bundle size impact

2. **Additional Services**
   - Modify docker-compose files
   - Update nginx configuration
   - Consider container networking

3. **Static Assets**
   - Add to /static directory
   - Update build process if needed
   - Consider caching strategies

4. **Type System**
   - Extend app.d.ts
   - Add new type declarations
   - Maintain strict checking