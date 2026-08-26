# Base Node.js image for compiling Vue application
FROM node:18-slim

WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install Node modules
RUN npm install

# Copy application files
COPY . .

EXPOSE 5173

# Run development server
CMD ["npm", "run", "serve"]