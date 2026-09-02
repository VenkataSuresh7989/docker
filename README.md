===================================================================
                  DOCKERFILE LIFECYCLE PIPELINE
===================================================================

1. BASE SETUP & CONFIGURATION
   ├── ARG           (Build-time variables)
   ├── FROM          (Base image declaration)
   └── LABEL         (Image metadata & tags)

2. ENVIRONMENT & CONTEXT
   ├── WORKDIR       (Set working directory)
   ├── ENV           (Persistent environment variables)
   └── SHELL         (Override default shell interpreter)

3. ASSETS & DEPENDENCIES
   ├── COPY          (Copy host files to image)
   ├── ADD           (Copy/extract archives & URLs)
   └── RUN           (Execute build commands & layers)

4. SECURITY & INHERITANCE
   ├── USER          (Set non-root user/group)
   └── ONBUILD       (Triggers for downstream images)

5. CONTAINER METADATA & STORAGE
   ├── EXPOSE        (Document network ports)
   ├── VOLUME        (Mount persistent storage points)
   └── STOPSIGNAL    (Define exit signal, e.g., SIGTERM)

6. EXECUTION & HEALTH
   ├── HEALTHCHECK   (Container status probe)
   ├── ENTRYPOINT    (Main executable process)
   └── CMD           (Default arguments / execution)
===================================================================
