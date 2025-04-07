# Streamer.bot Production Setup Guide

## Required Changes

### 1. Update Nginx Configuration in Dockerfile

The nginx configuration needs to be updated to support websocket connections. Update the nginx configuration in `twitch-app-prototype/Dockerfile` to include:

```nginx
server {
    listen 80;
    
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
        index index.html;
        
        # Add websocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

### 2. Update Docker Compose Configuration

The `twitch-app-prototype/docker-compose.yaml` needs to be updated to expose the Streamer.bot websocket port:

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3456:80"  # Web application
      - "8080:8080"  # Streamer.bot websocket
    restart: unless-stopped
```

### 3. Update README Instructions

Add the following sections to `twitch-app-prototype/README.md`:

#### Streamer.bot Integration Setup

1. First, install and set up Streamer.bot:
   - Download Streamer.bot from https://streamer.bot
   - Install and run the application
   - Go to Servers tab and ensure WebSocket Server is enabled
   - Default port is 8080 (this should match the port exposed in docker-compose.yaml)

2. Configure the connection in the app:
   - Go to Settings tab
   - Enter host: `127.0.0.1` (or your machine's IP if accessing from another device)
   - Enter port: `8080`
   - Click Connect

#### Troubleshooting Streamer.bot Connection

If you can't connect to Streamer.bot:
1. Check that Streamer.bot is running and its WebSocket Server is enabled
2. Verify the host and port match your Streamer.bot settings
3. If accessing from another device, make sure to use the machine's IP instead of localhost
4. Check that port 8080 is not blocked by firewall

## Implementation Steps

1. Switch to code mode to implement the Dockerfile changes
2. Update the docker-compose.yaml file
3. Update the README.md with the new instructions
4. Test the setup by:
   - Building and running the production container
   - Connecting to Streamer.bot
   - Verifying websocket communication works