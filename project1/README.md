### Docker File Structure:
* FROM base-image:tag              # Start point (REQUIRED)
* LABEL key=value                  # Metadata
* ENV VAR=value                    # Environment variables
* RUN command                      # Execute during build
* COPY source destination          # Copy from host
* ADD source destination           # Copy + extract tar
* WORKDIR /path                    # Working directory
* USER username                    # Switch user
* EXPOSE port                      # Document port
* HEALTHCHECK ...                  # Health check
* CMD ["executable", "param"]      # Default command

### Stop and Remove running images
* docker compose down -v

### Rebuild images and running
* docker compose up --build -d

### MySQL 
* docker exec -it mysql_db mysql -u appuser -papppassword demo -e "SHOW DATABASES;"
* docker exec -it mysql_db mysql -u appuser -papppassword demo -e "SHOW TABLES;"
* docker exec -it mysql_db mysql -u appuser -papppassword demo -e "SELECT * FROM userinfo;"

### Run all kubernetes  
* minikube service --all        :   Run all services
* kubectl get pods              :   Get all running pods
