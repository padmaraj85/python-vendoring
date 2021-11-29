
## Steps to setup the enviornment.

### Listing the libraries to be bundled.

- **requirements.txt** -- file contains the library to be bundled. Update it according to your needs.

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

### Download the zip file

- In this repo, as an example auth.zip bundle will be created. You may change it by modifying the contents of build.sh
- Change the .json and .py files according to your needs.

- bundle will be created insdie /root/plugin folder of compose_tyk_build_1 container. User below command to copy it to you local machine.

```
docker cp compose_tyk_build_1:/root/plugin/auth.zip ~/<your-local-folder>
```
