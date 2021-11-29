# python-vendoring
Vendoring libraries for Tyk python plugin
# Python plugin development notes


## Steps to setup the enviornment.

### Create the containers
```bash
cd compose
docker-compose up -d
```

This creates:

- compose_tyk_build_1 to build the bundles


### Update compose_tyk_build_1 to have the tools needed
```bash
docker container exec compose_tyk_build_1 apt-get update
docker container exec compose_tyk_build_1 apt-get install zip unzip -qy
docker container exec compose_tyk_build_1 /root/plugin/mkvendor.sh
```

### Build and serve the plugins
```bash
docker container exec -it compose_tyk_build_1 /root/plugin/build.sh
```


### Copy the bundle.zip to local directory

- You may change build.sh file according to you plugin (.json and py file)

- In this example we create two bunldes auth.zip and register.zip

-- bundle will be created insdie /root/plugin folder of compose_tyk_build_1 container. User below command to copy it to you local machine.

docker cp compose_tyk_build_1:/root/plugin/bundle.zip ~/<your folder>